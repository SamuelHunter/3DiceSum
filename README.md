# 3DiceSum
Geometric explanation for most probable sum of three dice

My plot
-------

A matplotlib figure to determine the most frequently occuring sum when 3 fair dice are rolled.\
While it would be simpler to enumerate all possible events and find the most frequent sum (which my program does behind the scenes),
a geometric understanding of the question makes predicting larger dice sums possible.

The plane x + y + z = k, where x, y, z are the individual dice rolls and k is their sum, intersects the sample space\
Ω = {{1, 2, 3, 4, 5, 6} x {1, 2, 3, 4, 5, 6} x {1, 2, 3, 4, 5, 6}}, represented by a 3D lattice of points.

- The three axes represent the rolls the dice, each lattice point being an event
- The sums are color coded, with the similarly colored points lining up in planes parallel to x + y + z = k
- The slider for k offsets the plane to a new sum k
- The number of intersections (stars) directly determines the probability of the sum.\
(P = intersections / 6^3 since all lattice points are equally likely)
- The plane cross sections form triangles for k ≤ 8 and k ≥ 13; hexagons in between
- The most intersections occur on the planes where k = 10 or k = 11

This spaghetti code was written to illustrate the problem, not as an example of good coding practices.\
Feel free to run the program and view the plot from plenty of angles to understand why the cross section takes on different shapes for different values of k.

*For a more detailed explanation, see below...*

![](https://github.com/SamuelHunter/3DiceSum/blob/master/k_range_anim.gif)

Geometric Explanation
---------------------

### 2 Dice

If you've ever played Catan, you would know that the most probable sum is 7, since it can be occur the most ways.
However, a geometric argument would be that the line

x + y = 7

intersects the sample space Ω = {{1, 2, 3, 4, 5, 6} x {1, 2, 3, 4, 5, 6}}\
at the most lattice points (6 out of 6^2, where each is equally likely for fair dice).

![](https://github.com/SamuelHunter/3DiceSum/blob/master/2_dice_sample_space.PNG)\
[Image credit: Professor Hanbaek Lyu](https://ccle.ucla.edu/pluginfile.php/2659609/mod_resource/content/0/lecturenote1.pdf)

### 3 Dice

A seemingly likely solution would be the plane

x + y + z = 8

which intersects the sample space at three vertices of the cube (1, 1, 6), (1, 6, 1), (6, 1, 1): a sum of 8,\
The cross section forms a triangle with maximum area. For k < 8, the triangles are of lesser area, implying that they contain less lattice points than when k = 8.

![](https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Cube-vertex-figure-middle.svg/220px-Cube-vertex-figure-middle.svg.png)
![](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Cube-vertex-figure-large.svg/200px-Cube-vertex-figure-large.svg.png)

[Image credit: Wikipedia](https://en.wikipedia.org/wiki/Vertex_figure)

However, according to [Wolfram Alpha](http://mathworld.wolfram.com/Dice.html), 10 and 11 are the most likely sums for 3 dice!

![](http://mathworld.wolfram.com/images/eps-gif/DicePlots_770.gif)

I created this plot to determine why the seemingly symmetrical and logical answer of 8 was incorrect.
After observing the plot from many angles, I realized why a hexagonal cross section intersects more lattice points than a triangle. Edges are more important to capturing lattice points than maximizing area. The 6 edges of the hexagon line up better with the grid than the triangle's 3.

![](http://mathworld.wolfram.com/images/eps-gif/CubeHexagon1_800.gif)

[Image credit: Wolfram Alpha](http://mathworld.wolfram.com/Cube.html)
