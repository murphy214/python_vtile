import os

def make_html_line():
	here = '''
<html>
<head>
<meta charset=utf-8 />
<title>PipeLeaflet</title>
<meta name='viewport' content='initial-scale=1,maximum-scale=1,user-scalable=no' />
<script src="http://code.jquery.com/jquery-1.11.3.min.js"></script>

 <link rel="stylesheet" href="https://npmcdn.com/leaflet@1.0.0-rc.3/dist/leaflet.css" />
 <script src="https://api.tiles.mapbox.com/mapbox-gl-js/v0.15.0/mapbox-gl.js"></script>


 <div id="map"></div>


<style> #map {
 position: relative;
 width: auto;
 height: 650px;
 overflow:visible;
}
</style>

<style>
 body { margin:0; padding:0; }
</style>
<style> #map {
 position: relative;
 width: auto;
 height: 650px;
 overflow:visible;
}
</style>

<style>
body {
 font-family: Arial, sans-serif;
 background-size: cover;
 height: 100vh;
}

h1 {
 text-align: center;
 font-family: Tahoma, Arial, sans-serif;
 color: #06D85F;
 margin: 10px 0;
}

.box {
 width: 40%;
 margin: 0 auto;
 background: rgba(255,255,255,0.2);
 padding: 35px;
 border: 2px solid #fff;
 border-radius: 10px/10px;
 background-clip: padding-box;
 text-align: center;
}

.button {
 font-size: 1em;
 padding: 10px;
 color: #fff;
 border: 2px solid #06D85F;
 border-radius: 10px/10px;
 text-decoration: none;
 cursor: pointer;
}
.button:hover {
 background: #06D85F;
}

.overlay {
 position: fixed;
 top: 0;
 bottom: 0;
 left: 0;
 right: 0;
 background: rgba(0, 0, 0, 0.7);
 visibility: hidden;
 opacity: 0;
}
.overlay:target {
 visibility: visible;
 opacity: 1;
}

.mapboxgl-popup {
 margin: 20px auto;
 padding: 20px;
 background: #fff;
 border-radius: 5px;
 width: 40%;
 position: relative;
}

.mapboxgl-popup h2 {
 margin-top: 0;
 color: #333;
 font-family: Tahoma, Arial, sans-serif;
}
.mapboxgl-popup .close {
 position: absolute;
 top: 20px;
 right: 30px;
 font-size: 30px;
 font-weight: bold;
 text-decoration: none;
 color: #333;
}
.mapboxgl-popup .close:hover {
 color: #06D85F;
}
.mapboxgl-popup .content {
 max-height: 70%;
 overflow: auto;
}

</style>


<script>
mapboxgl.accessToken = 'pk.eyJ1IjoicnNiYXVtYW5uIiwiYSI6IjdiOWEzZGIyMGNkOGY3NWQ4ZTBhN2Y5ZGU2Mzg2NDY2In0.jycgv7qwF8MMIWt4cT0RaQ';

//style: 'mapbox://styles/mapbox/dark-v8'
var map = new mapboxgl.Map({
  container: 'map',
  zoom: 13,
  center: [-122.45, 37.79],
  style:'mapbox://styles/mapbox/dark-v8'
,
  hash: false
});

map.on('load', function loaded() {
  map.addSource('custom-go-vector-tile-source', {
      type: 'vector',
      tiles: ['http://localhost:5000/tiles/{z}/{x}/{y}']
  });

  map.addLayer({
      "id": "custom-go-vector-tile-layer",
      "type": "line",
      "source": "custom-go-vector-tile-source",
      "source-layer": "lines",
      'paint': {
         'line-color': '#0053E4',
         'line-width':3
      }
  });
});

</script>
'''
	with open('index.html','w') as f:
		f.write(here)

def make_line_test(coords):
	here = '''

from flask import Flask
import python_vtile
app = Flask(__name__)


global coords
global a
a = python_vtile
coords = %s


@app.route('/tiles/<int:z>/<int:x>/<int:y>')
def profile(x,y,z):

    return a.make_tile_lines(x,y,z,coords)


if __name__ == '__main__':
    app.run()

''' % (str(coords))
	with open('line_test.py','w') as f:
		f.write(here)



def make_html_polygon():
  here = '''
<html>
<head>
<meta charset=utf-8 />
<title>PipeLeaflet</title>
<meta name='viewport' content='initial-scale=1,maximum-scale=1,user-scalable=no' />
<script src="http://code.jquery.com/jquery-1.11.3.min.js"></script>

 <link rel="stylesheet" href="https://npmcdn.com/leaflet@1.0.0-rc.3/dist/leaflet.css" />
 <script src="https://api.tiles.mapbox.com/mapbox-gl-js/v0.15.0/mapbox-gl.js"></script>


 <div id="map"></div>


<style> #map {
 position: relative;
 width: auto;
 height: 650px;
 overflow:visible;
}
</style>

<style>
 body { margin:0; padding:0; }
</style>
<style> #map {
 position: relative;
 width: auto;
 height: 650px;
 overflow:visible;
}
</style>

<style>
body {
 font-family: Arial, sans-serif;
 background-size: cover;
 height: 100vh;
}

h1 {
 text-align: center;
 font-family: Tahoma, Arial, sans-serif;
 color: #06D85F;
 margin: 10px 0;
}

.box {
 width: 40%;
 margin: 0 auto;
 background: rgba(255,255,255,0.2);
 padding: 35px;
 border: 2px solid #fff;
 border-radius: 10px/10px;
 background-clip: padding-box;
 text-align: center;
}

.button {
 font-size: 1em;
 padding: 10px;
 color: #fff;
 border: 2px solid #06D85F;
 border-radius: 10px/10px;
 text-decoration: none;
 cursor: pointer;
}
.button:hover {
 background: #06D85F;
}

.overlay {
 position: fixed;
 top: 0;
 bottom: 0;
 left: 0;
 right: 0;
 background: rgba(0, 0, 0, 0.7);
 visibility: hidden;
 opacity: 0;
}
.overlay:target {
 visibility: visible;
 opacity: 1;
}

.mapboxgl-popup {
 margin: 20px auto;
 padding: 20px;
 background: #fff;
 border-radius: 5px;
 width: 40%;
 position: relative;
}

.mapboxgl-popup h2 {
 margin-top: 0;
 color: #333;
 font-family: Tahoma, Arial, sans-serif;
}
.mapboxgl-popup .close {
 position: absolute;
 top: 20px;
 right: 30px;
 font-size: 30px;
 font-weight: bold;
 text-decoration: none;
 color: #333;
}
.mapboxgl-popup .close:hover {
 color: #06D85F;
}
.mapboxgl-popup .content {
 max-height: 70%;
 overflow: auto;
}

</style>


<script>
mapboxgl.accessToken = 'pk.eyJ1IjoicnNiYXVtYW5uIiwiYSI6IjdiOWEzZGIyMGNkOGY3NWQ4ZTBhN2Y5ZGU2Mzg2NDY2In0.jycgv7qwF8MMIWt4cT0RaQ';

//style: 'mapbox://styles/mapbox/dark-v8'
var map = new mapboxgl.Map({
  container: 'map',
  zoom: 13,
  center: [-122.45, 37.79],
  style:'mapbox://styles/mapbox/dark-v8'
,
  hash: false
});

map.on('load', function loaded() {
  map.addSource('custom-go-vector-tile-source', {
      type: 'vector',
      tiles: ['http://localhost:5000/tiles/{z}/{x}/{y}']
  });

  map.addLayer({
      "id": "custom-go-vector-tile-layer",
      "type": "fill",
      "source": "custom-go-vector-tile-source",
      "source-layer": "polygons",
      'paint': {
         'fill-color': '#0053E4',
      }
  });
});

</script>
'''
  with open('index.html','w') as f:
    f.write(here)

def make_polygon_test(coords):
  here = '''

from flask import Flask
import python_vtile
app = Flask(__name__)


global coords
global a
a = python_vtile
coords = %s


@app.route('/tiles/<int:z>/<int:x>/<int:y>')
def profile(x,y,z):

    return a.make_tile_polygons(x,y,z,coords)


if __name__ == '__main__':
    app.run()

''' % (str(coords))
  with open('polygon_test.py','w') as f:
    f.write(here)





def make_test_line(coords):
  make_html_line()
  os.system("open -a Safari index.html")
  make_line_test(coords)
  os.system("python line_test.py")


def make_test_polygon(coords):
  make_html_polygon()
  os.system("open -a Safari index.html")
  make_polygon_test(coords)
  os.system("python polygon_test.py")





