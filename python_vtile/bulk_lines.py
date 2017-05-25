import pandas as pd
import json
import mercantile as m
import numpy as np
import os
from coords import convert_all
from single_tile_test import make_html_line
from geometry import make_tile_lines

def get_cords_json(coords):
	data = '{"a":%s}' % coords
	data = json.loads(data)	
	return data['a']

def applyfunc(x):
	return x.tolist()

def merge_dicts(*dict_args):
    '''
    Given any number of dicts, shallow copy and merge into a new dict,
    precedence goes to key value pairs in latter dicts.
    '''
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result

def makemydir(whatever):
  try:
    os.makedirs(whatever)
  except OSError:
    pass

# takes a dataframe of lines from a csv file and creates a cohesive outpput that
# is automatically opened in browser with a simple httpserver to view output
def make_vtile_lines(data,zoomrange,html=True,both=False):

	# getting coord header
	for i in data.columns.values:
		if 'coord' in i.lower():
			coorheader = i

	# getting median coordinate fuck the average
	zoomlist = []
	coordlist = []
	folders = []
	for i  in data[coorheader].values:
		i = get_cords_json(i)
		coordlist.append(i)
		medcoord = i[len(i)/2]

		zooms = []

		for zoom in zoomrange:
			tile = m.tile(medcoord[0],medcoord[1],zoom)

			tilestr = 'tiles/%s/%s/%s' % (tile.z,tile.x,tile.y)
			tilestr2 = 'tiles/%s/%s' % (tile.z,tile.x)
			folders.append(tilestr2)
			zooms.append(tilestr)

		zoomlist.append(zooms)

	# getting and creating folders
	folders = np.unique(folders).tolist()
	[makemydir(i) for i in folders]
	
	# creating the new headers
	newheader = ['ZOOMSTR' + str(i)for i in zoomrange]

	# adding the data
	add = pd.DataFrame(zoomlist,columns=newheader)
	data[newheader] = add
	del add

	# resetting index for reference shit
	data = data.reset_index()

	# iterating through each newhader
	dicts = []
	for row in newheader:
		tempdict = data[[row,'index']].groupby(row)['index'].apply(applyfunc).to_dict()
		dicts.append(tempdict)

	# creating the total dictionary
	totaldict = merge_dicts(*dicts)
	del dicts

	# returning data and totalddict if applicable
	if both == True:
		return data,totaldict
	del data

	# making each tile
	for key,value in totaldict.items():
		coords = convert_all(key,[coordlist[i] for i in value])
		make_tile_lines(coords,write=key)

	# creating and opening html file if applicable
	if html == True:
		os.system("freeport 5000")
		make_html_line(coords=medcoord)		
		os.system("open -a Safari index.html")
		os.system("python -m SimpleHTTPServer 5000")
#mk.make_map([data,'lines'])