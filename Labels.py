#!/usr/bin/env python3
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

# =========================
# Label configuration
# =========================
LABEL_WIDTH = 1 * inch
LABEL_HEIGHT = 1 * inch

PAGE_WIDTH, PAGE_HEIGHT = letter

#MARGIN_X = 0.37 * inch
#MARGIN_Y = 0.4 * inch

#LABELS_PER_ROW = int((PAGE_WIDTH - 2*MARGIN_X) // LABEL_WIDTH)
#LABELS_PER_COL = int((PAGE_HEIGHT - 2*MARGIN_Y) // LABEL_HEIGHT)

LEFT_MARGIN   = 0.34 * inch        # 2/8 in
RIGHT_MARGIN  = 0.05 * inch        # 2/8 in

TOP_MARGIN    = 0.46 * inch      # 4/8 + 1/16 in
BOTTOM_MARGIN = 0.32 * inch         # 4/8 in

LABELS_PER_ROW = int(
    (PAGE_WIDTH - LEFT_MARGIN - RIGHT_MARGIN) // LABEL_WIDTH
)

LABELS_PER_COL = int(
    (PAGE_HEIGHT - TOP_MARGIN - BOTTOM_MARGIN) // LABEL_HEIGHT
)




# =========================
# Example resistor entries
# =========================
labels = [
    {'module': 1, 'board': 'J', 'channel': 1, 'date': '05/29/26', 'resistance': '5.188 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'J', 'channel': 2, 'date': '05/29/26', 'resistance': '5.160 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'J', 'channel': 3, 'date': '05/29/26', 'resistance': '5.094 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'J', 'channel': 4, 'date': '05/29/26', 'resistance': '5.111 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'J', 'channel': 5, 'date': '05/29/26', 'resistance': '5.123 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'J', 'channel': 6, 'date': '05/29/26', 'resistance': '5.152 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'J', 'channel': 7, 'date': '05/29/26', 'resistance': '5.095 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'J', 'channel': 8, 'date': '05/29/26', 'resistance': 'nan', 'Bin': '_____'},
    {'module': 1, 'board': 'K', 'channel': 1, 'date': '05/29/26', 'resistance': '5.158 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'K', 'channel': 2, 'date': '05/29/26', 'resistance': '5.095 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'K', 'channel': 3, 'date': '05/29/26', 'resistance': '5.081 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'K', 'channel': 4, 'date': '05/29/26', 'resistance': '5.128 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'K', 'channel': 5, 'date': '05/29/26', 'resistance': '5.199 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'K', 'channel': 6, 'date': '05/29/26', 'resistance': '5.144 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'K', 'channel': 7, 'date': '05/29/26', 'resistance': 'nan', 'Bin': '_____'},
    {'module': 1, 'board': 'K', 'channel': 8, 'date': '05/29/26', 'resistance': '5.118 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'L', 'channel': 1, 'date': '05/29/26', 'resistance': '5.100 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'L', 'channel': 2, 'date': '05/29/26', 'resistance': '5.107 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'L', 'channel': 3, 'date': '05/29/26', 'resistance': '5.076 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'L', 'channel': 4, 'date': '05/29/26', 'resistance': '5.089 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'L', 'channel': 5, 'date': '05/29/26', 'resistance': '5.143 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'L', 'channel': 6, 'date': '05/29/26', 'resistance': '5.106 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'L', 'channel': 7, 'date': '05/29/26', 'resistance': '5.105 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'L', 'channel': 8, 'date': '05/29/26', 'resistance': 'nan', 'Bin': '_____'},
    {'module': 1, 'board': 'A', 'channel': 1, 'date': '05/29/26', 'resistance': '5.080 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'A', 'channel': 2, 'date': '05/29/26', 'resistance': '5.156 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'A', 'channel': 3, 'date': '05/29/26', 'resistance': '5.102 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'A', 'channel': 4, 'date': '05/29/26', 'resistance': '5.087 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'A', 'channel': 5, 'date': '05/29/26', 'resistance': '5.095 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'A', 'channel': 6, 'date': '05/29/26', 'resistance': '5.094 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'A', 'channel': 7, 'date': '05/29/26', 'resistance': '5.109 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'A', 'channel': 8, 'date': '05/29/26', 'resistance': '5.183 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'B', 'channel': 1, 'date': '05/29/26', 'resistance': '5.166 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'B', 'channel': 2, 'date': '05/29/26', 'resistance': '5.063 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'B', 'channel': 3, 'date': '05/29/26', 'resistance': '5.060 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'B', 'channel': 4, 'date': '05/29/26', 'resistance': '5.087 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'B', 'channel': 5, 'date': '05/29/26', 'resistance': '5.098 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'B', 'channel': 6, 'date': '05/29/26', 'resistance': '5.159 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'B', 'channel': 7, 'date': '05/29/26', 'resistance': 'nan', 'Bin': '_____'},
    {'module': 1, 'board': 'B', 'channel': 8, 'date': '05/29/26', 'resistance': '5.076 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'C', 'channel': 1, 'date': '05/29/26', 'resistance': '5.124 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'C', 'channel': 2, 'date': '05/29/26', 'resistance': '5.154 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'C', 'channel': 3, 'date': '05/29/26', 'resistance': '5.117 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'C', 'channel': 4, 'date': '05/29/26', 'resistance': '5.062 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'C', 'channel': 5, 'date': '05/29/26', 'resistance': '5.126 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'C', 'channel': 6, 'date': '05/29/26', 'resistance': '5.093 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'C', 'channel': 7, 'date': '05/29/26', 'resistance': '5.087 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'C', 'channel': 8, 'date': '05/29/26', 'resistance': 'nan', 'Bin': '_____'},
    {'module': 1, 'board': 'D', 'channel': 1, 'date': '05/29/26', 'resistance': '5.143 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'D', 'channel': 2, 'date': '05/29/26', 'resistance': '5.120 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'D', 'channel': 3, 'date': '05/29/26', 'resistance': '5.079 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'D', 'channel': 4, 'date': '05/29/26', 'resistance': '5.130 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'D', 'channel': 5, 'date': '05/29/26', 'resistance': '5.142 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'D', 'channel': 6, 'date': '05/29/26', 'resistance': '5.136 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'D', 'channel': 7, 'date': '05/29/26', 'resistance': '5.062 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'D', 'channel': 8, 'date': '05/29/26', 'resistance': '5.074 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'E', 'channel': 1, 'date': '05/29/26', 'resistance': '5.097 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'E', 'channel': 2, 'date': '05/29/26', 'resistance': '5.097 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'E', 'channel': 3, 'date': '05/29/26', 'resistance': '5.106 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'E', 'channel': 4, 'date': '05/29/26', 'resistance': '5.027 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'E', 'channel': 5, 'date': '05/29/26', 'resistance': '5.152 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'E', 'channel': 6, 'date': '05/29/26', 'resistance': '5.090 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'E', 'channel': 7, 'date': '05/29/26', 'resistance': '5.063 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'E', 'channel': 8, 'date': '05/29/26', 'resistance': '5.154 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'F', 'channel': 1, 'date': '05/29/26', 'resistance': '5.157 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'F', 'channel': 2, 'date': '05/29/26', 'resistance': '5.080 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'F', 'channel': 3, 'date': '05/29/26', 'resistance': '5.117 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'F', 'channel': 4, 'date': '05/29/26', 'resistance': '5.070 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'F', 'channel': 5, 'date': '05/29/26', 'resistance': '5.125 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'F', 'channel': 6, 'date': '05/29/26', 'resistance': '5.095 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'F', 'channel': 7, 'date': '05/29/26', 'resistance': 'nan', 'Bin': '_____'},
    {'module': 1, 'board': 'F', 'channel': 8, 'date': '05/29/26', 'resistance': '5.061 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'G', 'channel': 1, 'date': '05/29/26', 'resistance': '5.140 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'G', 'channel': 2, 'date': '05/29/26', 'resistance': '5.130 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'G', 'channel': 3, 'date': '05/29/26', 'resistance': '5.128 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'G', 'channel': 4, 'date': '05/29/26', 'resistance': '5.147 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'G', 'channel': 5, 'date': '05/29/26', 'resistance': '5.098 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'G', 'channel': 6, 'date': '05/29/26', 'resistance': '5.134 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'G', 'channel': 7, 'date': '05/29/26', 'resistance': '5.134 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'G', 'channel': 8, 'date': '05/29/26', 'resistance': 'nan', 'Bin': '_____'},
    {'module': 1, 'board': 'H', 'channel': 1, 'date': '05/29/26', 'resistance': '5.121 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'H', 'channel': 2, 'date': '05/29/26', 'resistance': '5.147 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'H', 'channel': 3, 'date': '05/29/26', 'resistance': '5.090 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'H', 'channel': 4, 'date': '05/29/26', 'resistance': '5.142 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'H', 'channel': 5, 'date': '05/29/26', 'resistance': '5.088 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'H', 'channel': 6, 'date': '05/29/26', 'resistance': '5.143 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'H', 'channel': 7, 'date': '05/29/26', 'resistance': '5.092 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'H', 'channel': 8, 'date': '05/29/26', 'resistance': '5.149 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'I', 'channel': 1, 'date': '05/29/26', 'resistance': '5.153 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'I', 'channel': 2, 'date': '05/29/26', 'resistance': '5.178 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'I', 'channel': 3, 'date': '05/29/26', 'resistance': '5.096 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'I', 'channel': 4, 'date': '05/29/26', 'resistance': '5.113 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'I', 'channel': 5, 'date': '05/29/26', 'resistance': '5.113 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'I', 'channel': 6, 'date': '05/29/26', 'resistance': '5.187 GΩ', 'Bin': '_____'},
    {'module': 1, 'board': 'I', 'channel': 7, 'date': '05/29/26', 'resistance': 'nan', 'Bin': '_____'},
    {'module': 1, 'board': 'I', 'channel': 8, 'date': '05/29/26', 'resistance': '5.131 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'J', 'channel': 1, 'date': '05/29/26', 'resistance': '5.149 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'J', 'channel': 2, 'date': '05/29/26', 'resistance': '5.040 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'J', 'channel': 3, 'date': '05/29/26', 'resistance': '5.152 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'J', 'channel': 4, 'date': '05/29/26', 'resistance': '5.096 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'J', 'channel': 5, 'date': '05/29/26', 'resistance': '5.115 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'J', 'channel': 6, 'date': '05/29/26', 'resistance': '5.086 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'J', 'channel': 7, 'date': '05/29/26', 'resistance': '5.113 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'J', 'channel': 8, 'date': '05/29/26', 'resistance': '5.090 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'K', 'channel': 1, 'date': '05/29/26', 'resistance': '5.073 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'K', 'channel': 2, 'date': '05/29/26', 'resistance': '5.176 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'K', 'channel': 3, 'date': '05/29/26', 'resistance': '5.038 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'K', 'channel': 4, 'date': '05/29/26', 'resistance': '5.128 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'K', 'channel': 5, 'date': '05/29/26', 'resistance': '5.138 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'K', 'channel': 6, 'date': '05/29/26', 'resistance': '5.127 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'K', 'channel': 7, 'date': '05/29/26', 'resistance': 'nan', 'Bin': '_____'},
    {'module': 2, 'board': 'K', 'channel': 8, 'date': '05/29/26', 'resistance': '5.083 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'L', 'channel': 1, 'date': '05/29/26', 'resistance': '5.128 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'L', 'channel': 2, 'date': '05/29/26', 'resistance': '5.083 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'L', 'channel': 3, 'date': '05/29/26', 'resistance': '5.078 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'L', 'channel': 4, 'date': '05/29/26', 'resistance': '5.157 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'L', 'channel': 5, 'date': '05/29/26', 'resistance': '5.066 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'L', 'channel': 6, 'date': '05/29/26', 'resistance': '5.120 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'L', 'channel': 7, 'date': '05/29/26', 'resistance': '5.076 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'L', 'channel': 8, 'date': '05/29/26', 'resistance': 'nan', 'Bin': '_____'},
    {'module': 2, 'board': 'A', 'channel': 1, 'date': '05/29/26', 'resistance': '5.697 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'A', 'channel': 2, 'date': '05/29/26', 'resistance': '5.506 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'A', 'channel': 3, 'date': '05/29/26', 'resistance': '5.177 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'A', 'channel': 4, 'date': '05/29/26', 'resistance': 'nan', 'Bin': '_____'},
    {'module': 2, 'board': 'A', 'channel': 5, 'date': '05/29/26', 'resistance': '5.732 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'A', 'channel': 6, 'date': '05/29/26', 'resistance': '5.640 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'A', 'channel': 7, 'date': '05/29/26', 'resistance': '5.615 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'A', 'channel': 8, 'date': '05/29/26', 'resistance': '5.401 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'B', 'channel': 1, 'date': '05/29/26', 'resistance': '5.023 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'B', 'channel': 2, 'date': '05/29/26', 'resistance': '5.469 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'B', 'channel': 3, 'date': '05/29/26', 'resistance': '5.637 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'B', 'channel': 4, 'date': '05/29/26', 'resistance': '5.612 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'B', 'channel': 5, 'date': '05/29/26', 'resistance': '5.586 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'B', 'channel': 6, 'date': '05/29/26', 'resistance': '5.877 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'B', 'channel': 7, 'date': '05/29/26', 'resistance': 'nan', 'Bin': '_____'},
    {'module': 2, 'board': 'B', 'channel': 8, 'date': '05/29/26', 'resistance': '5.400 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'C', 'channel': 1, 'date': '05/29/26', 'resistance': '5.774 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'C', 'channel': 2, 'date': '05/29/26', 'resistance': '5.528 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'C', 'channel': 3, 'date': '05/29/26', 'resistance': '5.743 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'C', 'channel': 4, 'date': '05/29/26', 'resistance': '5.938 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'C', 'channel': 5, 'date': '05/29/26', 'resistance': '5.329 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'C', 'channel': 6, 'date': '05/29/26', 'resistance': 'nan', 'Bin': '_____'},
    {'module': 2, 'board': 'C', 'channel': 7, 'date': '05/29/26', 'resistance': '5.655 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'C', 'channel': 8, 'date': '05/29/26', 'resistance': 'nan', 'Bin': '_____'},
    {'module': 2, 'board': 'D', 'channel': 1, 'date': '05/29/26', 'resistance': '5.068 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'D', 'channel': 2, 'date': '05/29/26', 'resistance': '5.065 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'D', 'channel': 3, 'date': '05/29/26', 'resistance': '5.083 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'D', 'channel': 4, 'date': '05/29/26', 'resistance': '5.044 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'D', 'channel': 5, 'date': '05/29/26', 'resistance': '5.080 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'D', 'channel': 6, 'date': '05/29/26', 'resistance': '5.062 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'D', 'channel': 7, 'date': '05/29/26', 'resistance': '5.065 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'D', 'channel': 8, 'date': '05/29/26', 'resistance': '5.078 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'E', 'channel': 1, 'date': '05/29/26', 'resistance': '5.106 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'E', 'channel': 2, 'date': '05/29/26', 'resistance': '5.108 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'E', 'channel': 3, 'date': '05/29/26', 'resistance': '5.064 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'E', 'channel': 4, 'date': '05/29/26', 'resistance': '5.061 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'E', 'channel': 5, 'date': '05/29/26', 'resistance': '5.103 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'E', 'channel': 6, 'date': '05/29/26', 'resistance': '5.091 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'E', 'channel': 7, 'date': '05/29/26', 'resistance': 'nan', 'Bin': '_____'},
    {'module': 2, 'board': 'E', 'channel': 8, 'date': '05/29/26', 'resistance': '5.061 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'F', 'channel': 1, 'date': '05/29/26', 'resistance': '5.107 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'F', 'channel': 2, 'date': '05/29/26', 'resistance': '5.105 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'F', 'channel': 3, 'date': '05/29/26', 'resistance': '5.092 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'F', 'channel': 4, 'date': '05/29/26', 'resistance': '5.081 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'F', 'channel': 5, 'date': '05/29/26', 'resistance': '5.118 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'F', 'channel': 6, 'date': '05/29/26', 'resistance': '5.080 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'F', 'channel': 7, 'date': '05/29/26', 'resistance': '5.035 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'F', 'channel': 8, 'date': '05/29/26', 'resistance': 'nan', 'Bin': '_____'},
    {'module': 2, 'board': 'G', 'channel': 1, 'date': '05/29/26', 'resistance': '5.059 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'G', 'channel': 2, 'date': '05/29/26', 'resistance': '5.040 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'G', 'channel': 3, 'date': '05/29/26', 'resistance': '5.073 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'G', 'channel': 4, 'date': '05/29/26', 'resistance': '5.045 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'G', 'channel': 5, 'date': '05/29/26', 'resistance': '5.081 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'G', 'channel': 6, 'date': '05/29/26', 'resistance': '5.059 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'G', 'channel': 7, 'date': '05/29/26', 'resistance': '5.062 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'G', 'channel': 8, 'date': '05/29/26', 'resistance': '5.065 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'H', 'channel': 1, 'date': '05/29/26', 'resistance': '5.108 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'H', 'channel': 2, 'date': '05/29/26', 'resistance': '5.123 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'H', 'channel': 3, 'date': '05/29/26', 'resistance': '5.015 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'H', 'channel': 4, 'date': '05/29/26', 'resistance': '5.063 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'H', 'channel': 5, 'date': '05/29/26', 'resistance': '5.128 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'H', 'channel': 6, 'date': '05/29/26', 'resistance': '5.073 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'H', 'channel': 7, 'date': '05/29/26', 'resistance': 'nan', 'Bin': '_____'},
    {'module': 2, 'board': 'H', 'channel': 8, 'date': '05/29/26', 'resistance': '5.049 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'I', 'channel': 1, 'date': '05/29/26', 'resistance': '5.110 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'I', 'channel': 2, 'date': '05/29/26', 'resistance': '5.058 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'I', 'channel': 3, 'date': '05/29/26', 'resistance': '5.103 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'I', 'channel': 4, 'date': '05/29/26', 'resistance': '5.099 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'I', 'channel': 5, 'date': '05/29/26', 'resistance': '5.118 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'I', 'channel': 6, 'date': '05/29/26', 'resistance': '5.120 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'I', 'channel': 7, 'date': '05/29/26', 'resistance': '5.078 GΩ', 'Bin': '_____'},
    {'module': 2, 'board': 'I', 'channel': 8, 'date': '05/29/26', 'resistance': 'nan', 'Bin': '_____'},
    {'module': 3, 'board': 'J', 'channel': 1, 'date': '05/29/26', 'resistance': '5.066 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'J', 'channel': 2, 'date': '05/29/26', 'resistance': '5.013 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'J', 'channel': 3, 'date': '05/29/26', 'resistance': '5.005 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'J', 'channel': 4, 'date': '05/29/26', 'resistance': '4.960 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'J', 'channel': 5, 'date': '05/29/26', 'resistance': '4.979 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'J', 'channel': 6, 'date': '05/29/26', 'resistance': '4.984 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'J', 'channel': 7, 'date': '05/29/26', 'resistance': '5.002 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'J', 'channel': 8, 'date': '05/29/26', 'resistance': 'nan', 'Bin': '_____'},
    {'module': 3, 'board': 'K', 'channel': 1, 'date': '05/29/26', 'resistance': '5.060 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'K', 'channel': 2, 'date': '05/29/26', 'resistance': '4.989 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'K', 'channel': 3, 'date': '05/29/26', 'resistance': '5.015 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'K', 'channel': 4, 'date': '05/29/26', 'resistance': '5.019 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'K', 'channel': 5, 'date': '05/29/26', 'resistance': '5.017 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'K', 'channel': 6, 'date': '05/29/26', 'resistance': '5.008 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'K', 'channel': 7, 'date': '05/29/26', 'resistance': 'nan', 'Bin': '_____'},
    {'module': 3, 'board': 'K', 'channel': 8, 'date': '05/29/26', 'resistance': '4.976 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'L', 'channel': 1, 'date': '05/29/26', 'resistance': '5.041 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'L', 'channel': 2, 'date': '05/29/26', 'resistance': '5.013 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'L', 'channel': 3, 'date': '05/29/26', 'resistance': '4.991 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'L', 'channel': 4, 'date': '05/29/26', 'resistance': '4.999 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'L', 'channel': 5, 'date': '05/29/26', 'resistance': '4.993 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'L', 'channel': 6, 'date': '05/29/26', 'resistance': '4.992 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'L', 'channel': 7, 'date': '05/29/26', 'resistance': '4.962 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'L', 'channel': 8, 'date': '05/29/26', 'resistance': 'nan', 'Bin': '_____'},
    {'module': 3, 'board': 'A', 'channel': 1, 'date': '05/29/26', 'resistance': '5.110 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'A', 'channel': 2, 'date': '05/29/26', 'resistance': '5.042 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'A', 'channel': 3, 'date': '05/29/26', 'resistance': '4.979 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'A', 'channel': 4, 'date': '05/29/26', 'resistance': '4.951 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'A', 'channel': 5, 'date': '05/29/26', 'resistance': '4.968 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'A', 'channel': 6, 'date': '05/29/26', 'resistance': '4.997 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'A', 'channel': 7, 'date': '05/29/26', 'resistance': 'nan', 'Bin': '_____'},
    {'module': 3, 'board': 'A', 'channel': 8, 'date': '05/29/26', 'resistance': '4.976 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'B', 'channel': 1, 'date': '05/29/26', 'resistance': '5.121 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'B', 'channel': 2, 'date': '05/29/26', 'resistance': '5.061 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'B', 'channel': 3, 'date': '05/29/26', 'resistance': '5.033 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'B', 'channel': 4, 'date': '05/29/26', 'resistance': '4.981 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'B', 'channel': 5, 'date': '05/29/26', 'resistance': '4.981 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'B', 'channel': 6, 'date': '05/29/26', 'resistance': '4.988 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'B', 'channel': 7, 'date': '05/29/26', 'resistance': '4.979 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'B', 'channel': 8, 'date': '05/29/26', 'resistance': 'nan', 'Bin': '_____'},
    {'module': 3, 'board': 'C', 'channel': 1, 'date': '05/29/26', 'resistance': '5.095 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'C', 'channel': 2, 'date': '05/29/26', 'resistance': '5.067 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'C', 'channel': 3, 'date': '05/29/26', 'resistance': '4.998 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'C', 'channel': 4, 'date': '05/29/26', 'resistance': '4.979 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'C', 'channel': 5, 'date': '05/29/26', 'resistance': '4.990 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'C', 'channel': 6, 'date': '05/29/26', 'resistance': '4.993 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'C', 'channel': 7, 'date': '05/29/26', 'resistance': '4.988 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'C', 'channel': 8, 'date': '05/29/26', 'resistance': '4.982 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'D', 'channel': 1, 'date': '05/29/26', 'resistance': '5.126 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'D', 'channel': 2, 'date': '05/29/26', 'resistance': '5.075 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'D', 'channel': 3, 'date': '05/29/26', 'resistance': '5.080 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'D', 'channel': 4, 'date': '05/29/26', 'resistance': '5.031 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'D', 'channel': 5, 'date': '05/29/26', 'resistance': '5.000 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'D', 'channel': 6, 'date': '05/29/26', 'resistance': '4.993 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'D', 'channel': 7, 'date': '05/29/26', 'resistance': '5.021 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'D', 'channel': 8, 'date': '05/29/26', 'resistance': '4.959 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'E', 'channel': 1, 'date': '05/29/26', 'resistance': '5.073 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'E', 'channel': 2, 'date': '05/29/26', 'resistance': '5.118 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'E', 'channel': 3, 'date': '05/29/26', 'resistance': '5.062 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'E', 'channel': 4, 'date': '05/29/26', 'resistance': '5.019 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'E', 'channel': 5, 'date': '05/29/26', 'resistance': '5.033 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'E', 'channel': 6, 'date': '05/29/26', 'resistance': '5.019 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'E', 'channel': 7, 'date': '05/29/26', 'resistance': 'nan', 'Bin': '_____'},
    {'module': 3, 'board': 'E', 'channel': 8, 'date': '05/29/26', 'resistance': '4.983 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'F', 'channel': 1, 'date': '05/29/26', 'resistance': '5.160 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'F', 'channel': 2, 'date': '05/29/26', 'resistance': '5.119 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'F', 'channel': 3, 'date': '05/29/26', 'resistance': '5.054 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'F', 'channel': 4, 'date': '05/29/26', 'resistance': '5.064 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'F', 'channel': 5, 'date': '05/29/26', 'resistance': '5.014 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'F', 'channel': 6, 'date': '05/29/26', 'resistance': '5.010 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'F', 'channel': 7, 'date': '05/29/26', 'resistance': '4.992 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'F', 'channel': 8, 'date': '05/29/26', 'resistance': 'nan', 'Bin': '_____'},
    {'module': 3, 'board': 'G', 'channel': 1, 'date': '05/29/26', 'resistance': '5.111 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'G', 'channel': 2, 'date': '05/29/26', 'resistance': '5.075 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'G', 'channel': 3, 'date': '05/29/26', 'resistance': '5.041 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'G', 'channel': 4, 'date': '05/29/26', 'resistance': '4.991 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'G', 'channel': 5, 'date': '05/29/26', 'resistance': '4.992 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'G', 'channel': 6, 'date': '05/29/26', 'resistance': '4.965 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'G', 'channel': 7, 'date': '05/29/26', 'resistance': '4.974 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'G', 'channel': 8, 'date': '05/29/26', 'resistance': '4.960 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'H', 'channel': 1, 'date': '05/29/26', 'resistance': '5.108 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'H', 'channel': 2, 'date': '05/29/26', 'resistance': '5.044 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'H', 'channel': 3, 'date': '05/29/26', 'resistance': '4.984 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'H', 'channel': 4, 'date': '05/29/26', 'resistance': '4.982 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'H', 'channel': 5, 'date': '05/29/26', 'resistance': '5.007 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'H', 'channel': 6, 'date': '05/29/26', 'resistance': '4.991 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'H', 'channel': 7, 'date': '05/29/26', 'resistance': 'nan', 'Bin': '_____'},
    {'module': 3, 'board': 'H', 'channel': 8, 'date': '05/29/26', 'resistance': '4.950 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'I', 'channel': 1, 'date': '05/29/26', 'resistance': '5.090 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'I', 'channel': 2, 'date': '05/29/26', 'resistance': '5.089 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'I', 'channel': 3, 'date': '05/29/26', 'resistance': '5.016 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'I', 'channel': 4, 'date': '05/29/26', 'resistance': '4.994 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'I', 'channel': 5, 'date': '05/29/26', 'resistance': '4.984 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'I', 'channel': 6, 'date': '05/29/26', 'resistance': '4.978 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'I', 'channel': 7, 'date': '05/29/26', 'resistance': '4.949 GΩ', 'Bin': '_____'},
    {'module': 3, 'board': 'I', 'channel': 8, 'date': '05/29/26', 'resistance': '4.964 GΩ', 'Bin': '_____'}
]
# =========================
# Create PDF
# =========================
c = canvas.Canvas("resistor_labels.pdf", pagesize=letter)
c.setFont("Helvetica", 8)

#x = MARGIN_X
#y = PAGE_HEIGHT - MARGIN_Y - LABEL_HEIGHT

x = LEFT_MARGIN
y = PAGE_HEIGHT - TOP_MARGIN - LABEL_HEIGHT

label_count = 0

for item in labels:
    # Draw label border (optional, helps alignment)
    c.rect(x, y, LABEL_WIDTH, LABEL_HEIGHT)

    #text_x = x + 0.1 * inch
    #text_y = y + LABEL_HEIGHT - 0.3 * inch

    text_x = x + 0.08 * inch
    top_y = y + LABEL_HEIGHT - 0.14 * inch
    line_gap = 9.5

    c.setFont("Helvetica", 7.5)

    lines = [
    f"Module: {item['module']}",
    f"Board: {item['board']}",
    f"Channel: {item['channel']}",
    f"R = {item['resistance']}",
    f"Date: {item['date']}",
    f"Bin: {item.get('Bin', '_____')}",
    ]

    for j, line in enumerate(lines):
        c.drawString(text_x, top_y - j * line_gap, line)

    #c.drawString(text_x, text_y,       f"Module: {item['module']}")
    #c.drawString(text_x, text_y - 6,   f"Board: {item['board']}")
    #c.drawString(text_x, text_y - 12,   f"Channel: {item['channel']}")
    #c.drawString(text_x, text_y - 24,   f"R = {item['resistance']}")
    #c.drawString(text_x, text_y - 36,   f"Date: {item['date']}")
    #c.drawString(text_x, text_y - 48,   f"Bin: _____")

    label_count += 1
    x += LABEL_WIDTH

    #if label_count % LABELS_PER_ROW == 0:
    #    x = MARGIN_X
    #    y -= LABEL_HEIGHT

    #if y < MARGIN_Y:
    #    c.showPage()
    #    c.setFont("Helvetica", 8)
    #    x = MARGIN_X
    #    y = PAGE_HEIGHT - MARGIN_Y - LABEL_HEIGHT

    if label_count % LABELS_PER_ROW == 0:
        x = LEFT_MARGIN
        y -= LABEL_HEIGHT
    
    if y < BOTTOM_MARGIN:
        c.showPage()
        c.setFont("Helvetica", 8)
        x = LEFT_MARGIN
        y = PAGE_HEIGHT - TOP_MARGIN - LABEL_HEIGHT

c.save()
print("PDF created: resistor_labels.pdf")