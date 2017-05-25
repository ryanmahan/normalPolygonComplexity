# normalPolygonComplexity
An algorithm designed to find the "complexity" of a normal polygon

Works well for normal polygons, but breaks on irregular polygons, working on a fix for that, but seeing how my data is input as a geoJSON and Im just learning how thats all formatted as well this may take a while.

Tested using geoJSON data of United States Districts from github.com/unitedstates, this test works for the most part, but like mentioned above weighs any district with islands or properties that classify it as an irregular polygon too heavily. Works great for my general polygons listed, since they are all controlled and normal polygons.

The algorithim works by using the shoelace formula to find the area of the polygon, and then using the geoJSON points to find the perimeter, then calculates weights based on area/perimeter. The goal here is the more "complex" (a definition I totally and arbitrarily made up) a polygon is the higher it will be on the list (in this case, 1 is higher).

For example, a 23-pointed star will rank higher than a square because it is seen as more complex.

Another simpler way of doing this would be by number of verticies, but I felt as if that would punish something like a circle more than necessary, because a circle is usually seen as a "simple" shape, but would have hundreds of vertices depending on its circular-ness.
