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

  if length > 0:
    partitionBlock(color, length)


def partitionBlock(color, length):

  piece_lengths = {1, 2, 3, 4, 6, 8}

  length_splits = {
      14: 6,
      18: 6,
      20: 6,
      22: 6,
      24: 8,
      }

  if color not in dist:
    newdict = {}
    for l in piece_lengths:
      newdict[l] = 0
    dist[color] = newdict

  while length > 0:
    if length > 3 and length & 1:
      dist[color][3] += 1   # 3-length pieces are special
      length -= 3
    elif length in piece_lengths:
      dist[color][length] += 1
      length = 0
    elif length in length_splits:
      largest_smallest_length = length_splits[length]
      dist[color][largest_smallest_length] += 1
      length -= largest_smallest_length
    else:
      dist[color][8] += 1
      length -= 8



def main():
  portrait = Image.open(sys.argv[1])
  analyzeRows(portrait)

  total = 0
  for color in dist:
    print "color", color
    print dist[color]
    for size in dist[color]:
      total += dist[color][size] * size

  print "total pixels ", total

if __name__ == "__main__": main()

