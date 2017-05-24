# python_vtile
Purely prototyping and debugging for a soon to be module.

# What it is

This module is for easy prototyping of how typical webgl modules like mapbox gl interpret vector tile geometry. There are two main modes of debugging one of which being a bulk input that will be built for go more rigorously later and a single tile debugging mode that spins up a flask instance with a simple html page to view the geometry of a specific tile input for either polygons or lines. So essentially this mode you just give coordinates of a homogenous geometry type and view the output on every tile loaded up in the viewing window. 

The other mode is for bulk output and works alot like my current attempts in go. 

** The main goal of this module is to hack out something that can accurately debug and interpret how geometries are drawn in mapbox-gl. Its still an afternoon day project so far.**

# Example Line 

```python
import python_vtile
line = [[[200,200],[200,1000],[1000,1000],[2000,2000],[3000,1000]]]
python_vtile.make_test_line(line)
```
![](https://cloud.githubusercontent.com/assets/10904982/26421205/2aa31ec0-4093-11e7-8a1c-f55d6841a80b.png)

# Example Polygon
```python
import python_vtile
polygon = [[(300,600),(800,1200),(2000,3400),(300,600)]]
python_vtile.make_test_polygon(polygon)
```
![](https://cloud.githubusercontent.com/assets/10904982/26421202/28b03724-4093-11e7-85c4-fa5cf75e8a65.png)
