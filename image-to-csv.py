#!/usr/bin/python

import sys
from PIL import Image

portrait = Image.open(sys.argv[1])

pixels = portrait.load()

width, height = portrait.size

for y in range(height):
  row = []
  for x in range(width):
    cpixel = pixel[x, y]
    row.append(cpixel)
  print row


