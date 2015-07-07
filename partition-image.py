#!/usr/bin/python

import sys
from PIL import Image

dist = {}

def analyzeRows(image):
  width, height = image.size
  pixels = image.load()
  length = 0
  color = -1

  sum = 0

  for y in range(height):
    for x in range(width):
      cpixel = pixels[x, y]
      if (color != cpixel) or (x == 0):
        if length > 0:
          sum += length
          partitionBlock(color, length)
        color = cpixel  
        length = 1
      else:
        length += 1

  print "sum ", sum


def partitionBlock(color, length):

  if color not in dist:
    print "ADDING ", color
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
    elif length == 18:
      dist[color][8] += 1
      length -= 8
    elif length == 20:
      dist[color][10] += 1
      length -= 10
    elif length == 22:
      dist[color][10] += 1
      length -= 10
    elif length == 24:
      dist[color][12] += 1
      length -= 12
    elif length == 26:
      dist[color][10] += 1
      length -= 10
    elif length == 28:
      dist[color][12] += 1
      length -= 12
    elif length == 30:
      dist[color][8] += 1
      length -= 8
    else:
      dist[color][16] += 1
      length -= 16

  print dist[color]


def main():
  portrait = Image.open(sys.argv[1])
  analyzeRows(portrait)
  print dist

  total = 0 
  for color in dist:
    for size in dist[color]:
      total += dist[color][size]

  print "total pixels ", total

if __name__ == "__main__": main()

