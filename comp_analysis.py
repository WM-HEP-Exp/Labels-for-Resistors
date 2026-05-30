import glob
import json
import os
import sys
import time

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
# plt.rc('text', usetex=True)
import pandas as pd
from scipy.optimize import curve_fit
from concurrent.futures import ThreadPoolExecutor, as_completed

mpl.rc('xtick', direction='in', top=True)
mpl.rc('ytick', direction='in', right=True)
mpl.rc('xtick.minor', visible=True)
mpl.rc('ytick.minor', visible=True)
hv_conversion = 1 / 0.00111

HV_CHISQ_ACCEPTANCE = 0.5
data_path=""
FIGURES_DIR = None
def line_model(x, a, b):
    """
       Linear model function.

       Parameters
       ----------
       x : array-like
           Input variable.
       a : float
           Slope of the line.
       b : float
           Intercept of the line.

       Returns
       -------
       array-like
           Computed linear model values.
       """
    return a * x + b


def pert_diff(a, b):
    """
       Calculate percent difference between two values.

       Parameters
       ----------
       a, b : float or array-like
           Values to compare.

       Returns
       -------
       float or array-like
           Percent difference.
       """
    return np.abs(a - b) / ((a + b) / 2) * 100


def heatmap(data, row_labels, col_labels, ax=None,
            cbar_kw=None, cbarlabel="", **kwargs):
    """
      Create a heatmap from a numpy array and two lists of labels.

      Parameters
      ----------
      data : np.ndarray
          2D array of shape (M, N).
      row_labels : list
          Labels for rows.
      col_labels : list
          Labels for columns.
      ax : matplotlib.axes.Axes, optional
          Axes to plot on.
      cbar_kw : dict, optional
          Colorbar arguments.
      cbarlabel : str, optional
          Colorbar label.

      Returns
      -------
      im : AxesImage
          The image object.
      cbar : Colorbar
          The colorbar object.
      """

    if ax is None:
        ax = plt.gca()

    if cbar_kw is None:
        cbar_kw = {}

    # Plot the heatmap
    im = ax.imshow(data, **kwargs)

    # Create colorbar
    cbar = ax.figure.colorbar(im, ax=ax, **cbar_kw)
    cbar.ax.set_ylabel(cbarlabel, rotation=-90, va="bottom")

    # Show all ticks and label them with the respective list entries.
    ax.set_xticks(range(data.shape[1]), labels=col_labels,
                  rotation=0, ha="right", rotation_mode="anchor")
    ax.set_yticks(range(data.shape[0]), labels=row_labels)

    # Let the horizontal axes labeling appear on top.
    ax.tick_params(top=True, bottom=False,
                   labeltop=True, labelbottom=False)

    # Turn spines off and create white grid.
    ax.spines[:].set_visible(False)

    ax.set_xticks(np.arange(data.shape[1] + 1) - .5, minor=True)
    ax.set_yticks(np.arange(data.shape[0] + 1) - .5, minor=True)
    ax.grid(which="minor", color="w", linestyle='-', linewidth=3)
    ax.tick_params(which="minor", bottom=False, left=False)

    return im, cbar


def annotate_heatmap(im, data=None, valfmt="{x:.2f}",
                     textcolors=("black", "white"),
                     threshold=None, **textkw):
    """
    Annotate a heatmap.

    Parameters
    ----------
    im : AxesImage
        The image to annotate.
    data : np.ndarray, optional
        Data to annotate.
    valfmt : str, optional
        Value format.
    textcolors : tuple, optional
        Colors for text.
    threshold : float, optional
        Threshold for color change.

    Returns
    -------
    texts : list
        List of text annotations.
    """

    if not isinstance(data, (list, np.ndarray)):
        data = im.get_array()

    # Normalize the threshold to the images color range.
    if threshold is not None:
        threshold = im.norm(threshold)
    else:
        threshold = im.norm(data.max()) / 2.

    # Set default alignment to center, but allow it to be
    # overwritten by textkw.
    kw = dict(horizontalalignment="center",
              verticalalignment="center")
    kw.update(textkw)

    # Get the formatter in case a string is supplied
    if isinstance(valfmt, str):
        valfmt = mpl.ticker.StrMethodFormatter(valfmt)

    # Loop over the data and create a `Text` for each "pixel".
    # Change the text's color depending on the data.
    texts = []
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            kw.update(color=textcolors[int(im.norm(data[i, j]) > threshold)])
            text = im.axes.text(j, i, valfmt(data[i, j], None), **kw)
            texts.append(text)

    return texts


def load_data_file(file):
    """
    Load a data file (CSV or JSON) and return a DataFrame and board ID.

    Parameters
    ----------
    file : str
        Path to the data file.

    Returns
    -------
    board_frame : pd.DataFrame
        Data for all channels.
    board_id : str
        Identifier for the board.
    """
    if file.endswith(".csv"):
        df = pd.read_csv(file)
        board_id = df.keys()[1] if len(df.keys()) > 1 else f"Board_{os.path.basename(file)}"
        board_frame = pd.read_csv(file, skiprows=[0, 1]).sort_values("CHANNEL")
        name= ''
    elif file.endswith(".json"):
        with open(file, "r") as f:
            jsonfile = json.load(f)
        board_id = jsonfile["Id"]
        rows = []
        name=jsonfile["User"]
        for ch_name, ch_data in jsonfile["Data"].items():
            channel_num = int(ch_name.replace("CH", ""))
            for i in range(len(ch_data["Voltage"])):
                rows.append({
                    "CHANNEL": channel_num,
                    "HV Index": jsonfile["HV INDEX"][i],
                    "Voltage": ch_data["Voltage"][i],
                    "Error": ch_data["Error"][i]
                })
        board_frame = pd.DataFrame(rows).sort_values("CHANNEL")
    else:
        raise ValueError(f"Unsupported file format: {file}")
    return board_frame, board_id,name


def perform_calibration(HV_file):
    """
    Perform HV calibration and return calibration parameters.

    Parameters
    ----------
    HV_file : str
        Path to HV calibration file.

    Returns
    -------
    p_hvcal : np.ndarray
        Fit parameters.
    sigp_hvcal : np.ndarray
        Fit errors.
    hv_cal_id : str
        Calibration ID.
    hv_conversion : float
        Conversion factor.
    hvFromIndex : function
        Lambda for HV conversion.
    hv_cal_frame : pd.DataFrame
        Calibration data.
    """
    hv_conversion =1000# 1 / 0.00111
    if "csv" in HV_file:
        hv_cal_id = pd.read_csv(HV_file, ).keys()[1]
        hv_cal_frame = pd.read_csv(HV_file, skiprows=1)
        hv_cal_frame.drop(columns=['Unnamed: 3'], inplace=True)
    elif "json" in HV_file:
        with open(HV_file, "r") as f:
            jsonfile = json.load(f)
        hv_cal_id = jsonfile["Id"]
        if jsonfile["Division Factor"] != 0:
            hv_conversion = jsonfile["Division Factor"]
        hv_cal_frame = pd.DataFrame(jsonfile["DATA"])
    else:
        raise ValueError("No HV files found in folder that is json or csv")
    p_hvcal, C_hvcal = curve_fit(line_model, hv_cal_frame["HV Index"], hv_cal_frame["Voltage"],
                                 sigma=hv_cal_frame["Error"], absolute_sigma=True)
    sigp_hvcal = np.sqrt(np.diag(C_hvcal))
    hvFromIndex = lambda i: line_model(i, *p_hvcal) * hv_conversion
    chisq_hvcal = np.sum(

        ((hv_cal_frame["Voltage"] - line_model(hv_cal_frame["HV Index"], *p_hvcal)) / hv_cal_frame["Error"]) ** 2)
    return p_hvcal, sigp_hvcal, hv_cal_id, hv_conversion, hvFromIndex, hv_cal_frame
def analyze_board(board, file, pickoff_frame, hvFromIndex, p_hvcal, sigp_hvcal, hv_cal_id, anylisTime):
    board_frame, board_id,name = load_data_file(file)
    result_id_val = board_id
    result_value_val = np.zeros((8, 2))
    result_error_val = np.zeros((8, 3))
    channels_frame = board_frame.groupby('CHANNEL')
    for channel, channel_data in channels_frame:
        try:
            popt, perr, rsq, mask, data = analyze_channel(channel_data, pickoff_frame, channel, hvFromIndex)
        except RuntimeError as e:
            print(f"Fit did not converge for board {board_id}, channel {channel}: {e}")
            continue
        result_value_val[channel - 1, 0] = 1 / popt[0] * 1e-6
        result_value_val[channel - 1, 1] = popt[1]
        result_error_val[channel - 1, 0] = 1 / perr[0] * 1e-6
        result_error_val[channel - 1, 1] = perr[1]
        result_error_val[channel - 1, 2] = rsq
        if showResPlot:
            plot_fit_results(hvFromIndex, channel_data, mask, data, popt, perr, board_id, channel)
        if showErrorPlot:
            plot_residuals(hvFromIndex, channel_data, mask, data, popt, board_id, channel)
        if saveOutput:
            save_results_to_json(board_id, channel, popt, perr, p_hvcal, sigp_hvcal, hv_cal_id, channel_data, hvFromIndex, anylisTime,name)
    return board, result_id_val, result_value_val, result_error_val

def analyze_channel(channel_data, pickoff_frame, channel, hvFromIndex):
    """
    Analyze a single channel and return fit results.

    Parameters
    ----------
    channel_data : pd.DataFrame
        Data for the channel.
    pickoff_frame : pd.DataFrame
        Pickoff calibration data.
    channel : int
        Channel number.
    hvFromIndex : function
        Lambda for HV conversion.

    Returns
    -------
    popt : np.ndarray
        Fit parameters.
    perr : np.ndarray
        Fit errors.
    rsq : float
        R squared value.
    mask : np.ndarray
        Mask used for fitting.
    data : np.ndarray
        Current data.
    """
    channel_data = channel_data.sort_values("HV Index")
    channel_data.loc[channel_data["Error"] == 0, "Error"] = 0.03
    res_val = pickoff_frame.loc[pickoff_frame["CHANNEL"] == channel, "Res"].values[0] * 1e6
    data = -channel_data["Voltage"].to_numpy() / res_val
    mask = np.logical_and(np.diff(data, append=0) > 0, np.diff(data, append=0) < 1)
    popt, pcov = curve_fit(
        line_model,
        hvFromIndex(channel_data["HV Index"]).to_numpy()[mask],
        data[mask],
        p0=[1 / 5000 * 1e-6, 0],
        sigma=(channel_data["Error"].to_numpy()[mask]) / res_val,
        absolute_sigma=True,
        method="lm"
    )
    perr = np.sqrt(np.diag(pcov))
    fit_vals = line_model(hvFromIndex(channel_data["HV Index"]).to_numpy(), *popt)
    residuals = data - fit_vals
    rsq = 1 - np.sum(residuals[mask] ** 2) / np.sum((data[mask] - np.mean(data[mask])) ** 2)
    return popt, perr, rsq, mask, data


def plot_fit_hv(p_hvcal, sigp_hvcal, hv_cal_id, hv_conversion, hvFromIndex, hv_cal_frame):
    """
    Plot the fit results for a channel.
    """
    fighv, axhv = plt.subplots()

    axhv.plot(hv_cal_frame["HV Index"], hv_cal_frame["Voltage"], "k.", label="Data")

    axhv.plot(hv_cal_frame["HV Index"], line_model(hv_cal_frame["HV Index"], *p_hvcal), "r--", label="Fit")

    axhv.set_ylabel("Voltage/1000")

    axhv.set_xlabel("HV Index")

    axhv.set_title(f'High Voltage Calibration: {hv_cal_id}')
    rsq = 1 - np.sum((hv_cal_frame["Voltage"] - line_model(hv_cal_frame["HV Index"], *p_hvcal)) ** 2) / np.sum(

        (hv_cal_frame["Voltage"] - np.mean(hv_cal_frame["Voltage"])) ** 2)
    axhv.text(0.05, 0.95,
               f"HV Conversion = {hv_conversion:.2f}\n"
               f"Slope = {p_hvcal[0]:.4f} ± {sigp_hvcal[0]:.4f}\n"
               f"Intercept = {p_hvcal[1]:.4f} ± {sigp_hvcal[1]:.4f}\n"
               f"R^2 = {rsq:.5f}",)

    axhv.legend(loc="best")
    if FIGURES_DIR:
        out = os.path.join(FIGURES_DIR, f"HVcal_{hv_cal_id}.png")
    else:
        out = f"HVcal_{hv_cal_id}.png"
    fighv.tight_layout()
    fighv.savefig(out)
    plt.close(fighv)


def plot_fit_results(hvFromIndex, channel_data, mask, data, popt, perr, board_id, channel):
    """
    Plot the fit results for a channel.

    Parameters
    ----------
    hvFromIndex : function
        Lambda for HV conversion.
    channel_data : pd.DataFrame
        Data for the channel.
    mask : np.ndarray
        Mask used for fitting.
    data : np.ndarray
        Current data.
    popt : np.ndarray
        Fit parameters.
    perr : np.ndarray
        Fit errors.
    board_id : str
        Board identifier.
    channel : int
        Channel number.
    """
    fig1, ax1 = plt.subplots()
    ax1.plot(hvFromIndex(channel_data["HV Index"]).to_numpy()[mask],
             data[mask], "k.", label="Data")
    ax1.set_ylabel("Current [A]")
    ax1.set_xlabel("HV Voltage [V]")
    ax1.set_title(f'Best fit of Component: {board_id} Channel: {channel}')
    ax1.plot(hvFromIndex(channel_data["HV Index"]).to_numpy(),
             line_model(hvFromIndex(channel_data["HV Index"]).to_numpy(), *popt), "r", label="Fit")
    ax1.legend()
    ax1.text(1200, 0.1e-7,
             f"Resistance = {1 / popt[0] * 1e-6:.4f} ± \n {perr[0] * (1e-6 / (popt[0] ** 2)):.4f} Mega Ohm")
    #print(f"Board {board_id} Channel {channel} Resistance: {1 / popt[0] * 1e-6:.4f} ± {perr[0] * (1e-6 / (popt[0] ** 2)):.4f} Mega Ohm ")
    if FIGURES_DIR:
        out = os.path.join(FIGURES_DIR, f"Fit_{board_id}_CH{channel}.png")
    else:
        out = f"Fit_{board_id}_CH{channel}.png"
    fig1.tight_layout()
    fig1.savefig(out)
    plt.close(fig1)


def plot_residuals(hvFromIndex, channel_data, mask, data, popt, board_id, channel):
    """
    Plot the residuals for a channel.

    Parameters
    ----------
    hvFromIndex : function
        Lambda for HV conversion.
    channel_data : pd.DataFrame
        Data for the channel.
    mask : np.ndarray
        Mask used for fitting.
    data : np.ndarray
        Current data.
    popt : np.ndarray
        Fit parameters.
    board_id : str
        Board identifier.
    channel : int
        Channel number.
    """
    fig2, ax2 = plt.subplots()
    ax2.set_title(f'Residual: {board_id} Channel: {channel}')
    ax2.set_ylabel("Residual [A]")
    ax2.set_xlabel("HV Voltage [V]")
    ax2.plot(hvFromIndex(channel_data["HV Index"]).to_numpy()[mask],
             (data - line_model(hvFromIndex(channel_data["HV Index"]).to_numpy(), *popt))[mask],
             "ko", label="Residuals")
    if FIGURES_DIR:
        out = os.path.join(FIGURES_DIR, f"Residuals_{board_id}_CH{channel}.png")
    else:
        out = f"Residuals_{board_id}_CH{channel}.png"
    fig2.tight_layout()
    fig2.savefig(out)
    plt.close(fig2)


def save_results_to_json(board_id, channel, popt, perr, p_hvcal, sigp_hvcal, hv_cal_id, channel_data, hvFromIndex,
                         analysis_time,name):
    """
    Save the results to a JSON file.

    Parameters
    ----------
    board_id : str
        Board identifier.
    channel : int
        Channel number.
    popt : np.ndarray
        Fit parameters.
    perr : np.ndarray
        Fit errors.
    p_hvcal : np.ndarray
        HV calibration parameters.
    sigp_hvcal : np.ndarray
        HV calibration errors.
    hv_cal_id : str
        HV calibration ID.
    channel_data : pd.DataFrame
        Data for the channel.
    hvFromIndex : function
        Lambda for HV conversion.
    analysis_time : int
        Timestamp for the analysis.
    """
    preJson = {
        "id": board_id,
        "hvid": hv_cal_id,
        "testBy": name,
        "channel": channel,
        "hvSlope": p_hvcal[0],
        "hvIntercept": p_hvcal[1],
        "hvSlopeError": sigp_hvcal[0],
        "hvInterceptError": sigp_hvcal[1],
        "resSlope": popt[0],
        "resIntercept": popt[1],
        "resSlopeError": perr[0],
        "resInterceptError": perr[1],
        "hvindex": channel_data["HV Index"].tolist(),
        "rawValues": channel_data["Voltage"].tolist(),
        "rawError": channel_data["Error"].tolist(),
        "fittedValues": line_model(hvFromIndex(channel_data["HV Index"]).to_numpy(), *popt).tolist(),
    }
    output_dir = os.path.abspath(f"WM_Output_{board_id}_{analysis_time}")
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f"WM_Output_{board_id}_{channel}_{analysis_time}.json")
    with open(output_file, mode="w", encoding="utf-8") as write_file:
        json.dump(preJson, write_file, indent=4)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python comp_analysis.py <Data_Folder> [Cal_folder]\n"
              "\tThis script will analyze the data produce from the resistor and varistor component testing\n"
              "\tThe Data should be house in a folder passed in as <Data_Folder>\n"
              "\tThis Data should be formated according to data_format_spec/WM_Comp_test_template.csv or json equivilent\n"
              "\tCalibration data such as HV and Pickoff values can either be in the <Data_Folder> or"
              "[Cal_folder](only the first of each type is taken) and\n"
              "\tshould be in the format specify in json_format_spec\n"
              "I also highly recommend to pipe the output of this script into a text file: python comp_analysis.py "
              "<Data_Folder> [Cal_folder] >> <Data_Folder>/output.txt\n "
              )
        sys.exit(1)
    if len(sys.argv) == 2:
        data_path = sys.argv[1]

        data_files_csv = glob.glob(data_path + "/*Comp*.csv")
        data_files_json = glob.glob(data_path + "/*Comp*.json")
        if len(data_files_csv) < 1 and len(data_files_json) < 1:
            print("No data files found, exiting")
            sys.exit(1)
        try:
            HV_file = (glob.glob(data_path + "/*HV*.json") + glob.glob(data_path + "/*HV*.csv"))[0]
            pickoff_file = glob.glob(data_path + "/*Pickoff*.csv")[0]
        except IndexError:
            print("No HV or Pickoff files found in folder " + data_path)
            sys.exit(1)
        # Should implenent check for null
        # Assume all files are in <Data_folder>
    if len(sys.argv) == 3:
        data_path = sys.argv[1]

        data_files_csv = glob.glob(data_path + "/*Comp*.csv")
        data_files_json = glob.glob(data_path + "/*Comp*.json")
        if len(data_files_csv) < 1:
            print("No data files found, exiting")
            sys.exit(1)
        data_path = sys.argv[2]
        try:
            HV_file = (glob.glob(data_path + "/*HV*.json") + glob.glob(data_path + "/*HV*.csv"))[0]
            pickoff_file = glob.glob(data_path + "/*Pickoff*.csv")[0]
        except IndexError:
            print("No HV or Pickoff files found in folder " + data_path)
            sys.exit(1)
        # Should implenent check for null
        # Assume all files are in <Data_folder>

    elif len(sys.argv) > 3:
        print("No Implemented Yet")
        sys.exit(1)
        # this needs to do a bit of file jumping

    showHVPlot = 0
    showResPlot = 0
    showErrorPlot =0
    saveOutput = 0
    # Calibration
    p_hvcal, sigp_hvcal, hv_cal_id, hv_conversion, hvFromIndex, hv_cal_frame = perform_calibration(HV_file)

    # Pickoff
    pickoff_frame = pd.read_csv(pickoff_file, skiprows=1).rename(
        columns={"Pick Off Resistence Mega Ohm": "Res"}).sort_values("CHANNEL")

    # Results arrays
    all_files = data_files_csv + data_files_json
    anylisTime = int(time.time())
    FIGURES_DIR = os.path.abspath(os.path.join(data_path, f"WM_Figures_{anylisTime}"))
    os.makedirs(FIGURES_DIR, exist_ok=True)
    result_value = np.zeros((len(all_files), 8, 2))
    result_id = np.zeros((len(all_files), 3), dtype=object)
    result_error = np.zeros((len(all_files), 8, 3))

    # Main analysis loop
    with ThreadPoolExecutor() as executor:
        futures = [
            executor.submit(
                analyze_board, board, file, pickoff_frame, hvFromIndex, p_hvcal, sigp_hvcal, hv_cal_id, anylisTime
            )
            for board, file in enumerate(all_files)
        ]
        for future in as_completed(futures):
            try:
                board, result_id_val, result_value_val, result_error_val = future.result()
                result_id[board, 0] = result_id_val
                result_value[board] = result_value_val
                result_error[board] = result_error_val
            except Exception as e:
                print(f"Error processing board {board}: {e}")
    fig, ax = plt.subplots()
    custom_colors = ['white', 'red', 'blue']
    base_cmap = plt.get_cmap('cividis')  # or 'plasma', 'inferno', 'cividis', etc.
    colors = base_cmap(np.linspace(0, 1, 29))
    cmap = mpl.colors.ListedColormap(colors)
    
    bounds = [0, 1, 4.85, 4.875, 4.9, 4.925, 4.95, 4.975, 5., 5.025, 5.05,
              5.075, 5.1, 5.125, 5.15, 5.175, 5.2, 5.225, 5.25, 5.275]  # ,
    # 5.3  , 5.325, 5.35 , 5.375, 5.4  , 5.425, 5.45 , 5.475, 5.5  ,10]
    norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
    im, cbar = heatmap(result_value[:, :, 0] / 1000, result_id[:, 0], range(1, 9), cmap=cmap, ax=ax,
                       cbarlabel="Resistance")#, norm=norm)
    texts = annotate_heatmap(im, valfmt="{x:.3f}", threshold=5.4)

    for i in range(8):
        # value=result_value[3,i,0]/1000-result_value[0,i,0]/1000
        value = np.std((result_value[:, i, 0] / 1000)[np.where(result_value[:, i, 0] / 1000 > 3)])/np.mean((result_value[:, i, 0] / 1000)[np.where(result_value[:, i, 0] / 1000 > 3)])*100
        print((result_value[:, i, 0] / 1000)[np.where((result_value[:, i, 0] / 1000) > 3)])
        plt.text(i, len(result_value[:, 0, 0]), f"{value:.4f}", ha="center", va="center", rotation="vertical")
    plt.text(-4.5, len(result_value[:, 0, 0]) + 0.3, "% Std Dev of Ch") #Here I need to print the side of the label in which will be saved or not
    fig.tight_layout(pad=2)
    fig.show()

plt.show()

# =========================
# CREATE LABEL LIST
# =========================

labels = []

module_number = 3         # <-- change if needed
date_str = "05/29/26"       # <-- change or make dynamic
print(result_id[:, 0])

for i, board in enumerate(result_id[:, 0]):   # loop over boards
    for ch in range(8):                       # channels 1–8
        
        resistance = result_value[i, ch, 0] / 1000  # convert to GΩ
        
        board_str = str(board)
        #print(str(board))
        parts = board_str.split("_")
        board_num = int(parts[1])
        
        board_letter = chr(ord('A') + board_num - 1)
        #print(board_letter)
        # skip empty / bad values if needed
        
        labels.append({
            "module": module_number,
            "board": board_letter,  # optional cleanup
            #"board": str(board).replace("_Cold", ""), # optional cleanup
            "channel": ch + 1,
            "date": date_str,
             "resistance": f"{resistance:.3f} GΩ" if 3 <= resistance <= 6 else "nan",
            "Bin": "_____"
        })

# =========================
# PRINT NICELY
# =========================

print("\nlabels = [")
for item in labels:
    print(f'    {item},')
print("]")


# =========================
# SAVE LABEL LIST TO CSV
# =========================

output_csv = "resistance_labels.csv"

df_labels = pd.DataFrame(labels)

# If file exists, append without header
# If file does not exist, create it with header
df_labels.to_csv(
    output_csv,
    mode="a",
    header=not os.path.exists(output_csv),
    index=False
)

print(f"Saved {len(df_labels)} rows to {output_csv}")
