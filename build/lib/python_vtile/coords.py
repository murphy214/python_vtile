import numpy as np
import mercantile as m

def single_point(row,bound,deltax,deltay):
	factorx = (row[0] - bound.west) / deltax
	factory = (bound.north - row[1]) / deltay

	xval = int(factorx * 4096)
	yval = int(factory * 4096)

	return [xval,yval]

def get_convert_values(key):
	z,x,y = str.split(key,'/')[1:]

	bound = m.bounds(m.Tile(int(x), int(y), int(z)))
	deltax,deltay = (bound.east - bound.west),(bound.north - bound.south)

	return bound,deltax,deltay


def convert_all(key,coordss):
	#newlist = []
	bound,deltax,deltay = get_convert_values(key)
	#for coords in coordss:
	return [[single_point(i,bound,deltax,deltay) for i in coords] for coords in coordss]
	#return newlist
