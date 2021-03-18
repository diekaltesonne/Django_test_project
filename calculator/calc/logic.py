from shapely.strtree import STRtree
from shapely.geometry import Polygon, Point
import shapely.wkt

# # this is the grid. It includes a point for each rectangle center. 
# points = [Point(i, j) for i in range(10) for j in range(10)]
# points.append(Point(0.5,-1))
# tree = STRtree(points) # create a 'database' of points

# # this is one of the polygons. 
# #p = Polygon([[0.5, 0], [2, 0.2], [3, 4], [0.8, 0.5], [0.5, 0]])
# #res = tree.query(p) # run the query (a single shot). 
# # do something with the results
# #print([o.wkt for o in res])

p = shapely.wkt.loads('POLYGON ((0.5 0, 2 0.2, 3 4, 0.8 0.5, 0.5 0))')
# print(p)
# res = tree.query(p) # run the query (a single shot). 
# # do something with the results
# print([o.wkt for o in res])

# P = shapely.wkt.loads('POLYGON ((51.0 3.0, 51.3 3.61, 51.3 3.0, 51.0 3.0))')
# print(P)