#!/usr/bin/python

import sys
from PIL import Image

dist = {}

def analyzeRows(image):
  width, height = image.size
  pixels = image.load()
  length = 0
  color = -1
  for y in range(height):
    for x in range(width):
      cpixel = pixels[x, y]
      if (color != cpixel) or (x == 0):
        if length > 0:
          partitionBlock(color, length)
        color = cpixel  
        length = 1
      else:
        length += 1


def partitionBlock(color, length):
  if color not in dist:
    dist[color] = {
      1: 0,
      2: 0,
      3: 0,
      4: 0,
      6: 0,
      8: 0,
      10: 0,
      12: 0,
      16: 0,
      }    

  print length, color
 
  while length > 0:
    print "current ", length
    if length == 1:
      dist[color][1] += 1
      length = 0
    elif length == 2:
      dist[color][2] += 1
      length = 0
    elif length == 3:
      dist[color][3] += 1
      length = 0
    elif length == 4:
      dist[color][4] += 1
      length = 0
    elif length & 1:
      dist[color][3] += 1
      length -= 3
    elif length == 6:
      dist[color][6] += 1
      length = 0
    elif length == 8:
      dist[color][8] += 1
      length = 0
    elif length == 10:
      dist[color][10] += 1
      length = 0
    elif length == 12:
      dist[color][12] += 1
      length = 0
    elif length == 14:
      dist[color][6] += 1
      dist[color][8] += 1
      length = 0
    elif length == 16:
      dist[color][16] += 1
      length = 0

    print dist[color]


def main():
  portrait = Image.open(sys.argv[1])
  analyzeRows(portrait)

if __name__ == "__main__": main()

