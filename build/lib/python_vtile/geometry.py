from vect import vector_tile_pb2
vector_tile = vector_tile_pb2

cmd_bits = 3

CMD_MOVE_TO = 1
CMD_LINE_TO = 2
CMD_SEG_END = 7
CMD_FAKE = 0


def encode_cmd_length(cmd, length):
	return (cmd & 0x7) | (length << 3)

def zigzag(delta):
    return (delta << 1) ^ (delta >> 31)

def moveto(count):
	return encode_cmd_length(1, count)

def lineto(count):
	return encode_cmd_length(2, count)

def moverow(row,f):
	f.geometry.append(moveto(1))
	f.geometry.append(zigzag(row[0]))
	f.geometry.append(zigzag(row[1]))
	return f

def linerow(row,f):
	f.geometry.append(zigzag(row[0]))
	f.geometry.append(zigzag(row[1]))
	return f

# coordlines expects the coordinates to be long,lat syntax
# coord lines is the list of line coordinates
def make_tile_lines(x,y,z,coordss,write=False):
	tile = vector_tile.Tile()
	tile_feature = vector_tile.Tile().Feature()
	layer = tile.layers.add()
	layer.extent = 4096
	layer.name = 'lines'
	layer.version = 15
	f = layer.features.add()

	f.type = 2
	f.id = 10

	oldrow = [0,0]
	for coords in coordss:
		#print coords
		linetocount = len(coords) -1
		#print linetocount
		count = 0
		for row in coords:
			addrow = [row[0]-oldrow[0],row[1]-oldrow[1]]
			print addrow
			if count == 0:
				count = 1
				f.geometry.append(moveto(1))

				f.geometry.append(zigzag(addrow[0]))
				f.geometry.append(zigzag(addrow[1]))
				#moverow([row[0]-oldrow[0],row[1]-oldrow[1]],f)
				f.geometry.append(lineto(linetocount))
			else:
				f.geometry.append(zigzag(addrow[0]))
				f.geometry.append(zigzag(addrow[1]))
			
				#linerow([row[0]-oldrow[0],row[1]-oldrow[1]],f)

			oldrow = row

	return tile.SerializeToString()


# coordlines expects the coordinates to be long,lat syntax
# coord lines is the list of line coordinates
def make_tile_polygons(x,y,z,coordss,write=False):
	tile = vector_tile.Tile()
	tile_feature = vector_tile.Tile().Feature()
	layer = tile.layers.add()
	layer.extent = 4096
	layer.name = 'polygons'
	layer.version = 15
	f = layer.features.add()

	f.type = 3
	f.id = 10

	oldrow = [0,0]
	for coords in coordss:
		#print coords
		linetocount = len(coords) - 2
		coords = coords[:len(coords) - 1]
		#print linetocount
		count = 0
		for row in coords:
			addrow = [row[0]-oldrow[0],row[1]-oldrow[1]]
			if count == 0:
				count = 1
				f.geometry.append(moveto(1))

				f.geometry.append(zigzag(addrow[0]))
				f.geometry.append(zigzag(addrow[1]))
				#moverow([row[0]-oldrow[0],row[1]-oldrow[1]],f)
				f.geometry.append(lineto(linetocount))
			else:
				f.geometry.append(zigzag(addrow[0]))
				f.geometry.append(zigzag(addrow[1]))
			
				#linerow([row[0]-oldrow[0],row[1]-oldrow[1]],f)

			oldrow = row
		f.geometry.append(encode_cmd_length(7,1))
	return tile.SerializeToString()



