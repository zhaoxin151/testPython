#!/user/bin/python
#-*- coding:utf-8 -*-
#author wanghaibo

from reportlab.graphics.shapes import *
from reportlab.lib import colors
from reportlab.graphics import renderPDF

d = Drawing(100, 100)
d.add(PolyLine([(20, 20), (30, 30), (30, 20), (20, 30)], strokeColor = colors.blue))

renderPDF.drawToFile(d, 'PolyLine.pdf', 'A line PDF file')