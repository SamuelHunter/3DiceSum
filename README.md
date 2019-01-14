# 3DiceSum
Geometric explanation for most probable sum of three dice

---
This program is interactive and was written in python with matplotlib.

The plane x + y + z = k (where x, y, z are the individual dice rolls and k is their sum) intersects the sample space\
Ω = {{1, 2, 3, 4, 5, 6} x {1, 2, 3, 4, 5, 6} x {1, 2, 3, 4, 5, 6}}, represented by a 3D lattice of points.

- Each lattice point is an event (x, y, z)
- Sums are color coded, with the similarly colored points lining up in planes parallel to x + y + z = k
- k has a slider to offset the plane to a new sum
- Number of intersections (stars) directly determines the probability of the sum\
(P(k) = intersections / 6<sup>3</sup> since all lattice points are equally likely)
- Plane cross sections form triangles for k ≤ 8 and k ≥ 13; hexagons in between
- The most intersections occur on the planes where k = 10 or k = 11

Feel free to run the program and view the plot from plenty of angles to understand why the cross section takes on different shapes for different values of k.

*For a more detailed explanation, see below . . .*

**Preview**

![](https://github.com/SamuelHunter/3DiceSum/blob/master/k_range_anim.gif)

Geometric Explanation
---------------------

<details>
  <summary>Click to expand!</summary>

### 2 Dice

If you've ever played Catan, you would know that the most probable sum is 7, since it can occur the most ways.
However, a geometric argument would be that the line

x + y = 7

intersects the sample space Ω = {{1, 2, 3, 4, 5, 6} x {1, 2, 3, 4, 5, 6}}\
at the most lattice points (6 out of 6<sup>2</sup>, where each is equally likely for fair dice).

![](https://github.com/SamuelHunter/3DiceSum/blob/master/2_dice_sample_space.PNG)\
[Image credit: Professor Hanbaek Lyu](https://ccle.ucla.edu/pluginfile.php/2659609/mod_resource/content/0/lecturenote1.pdf)

### 3 Dice

A seemingly likely solution would be the plane

x + y + z = 8

because it intersects the sample space at three vertices of the cube (1, 1, 6), (1, 6, 1), (6, 1, 1): a sum of 8,\
The cross section forms a triangle with maximum area. For k < 8, the triangles are closer to the vertex (1, 1, 1), and therefore contain less area, implying that they contain less lattice points than when k = 8.

![](https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Cube-vertex-figure-middle.svg/220px-Cube-vertex-figure-middle.svg.png)
![](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Cube-vertex-figure-large.svg/200px-Cube-vertex-figure-large.svg.png)

[Image credit: Wikipedia](https://en.wikipedia.org/wiki/Vertex_figure)

However, according to [Wolfram Alpha](http://mathworld.wolfram.com/Dice.html), 10 and 11 are the most likely sums for 3 dice!

![](http://mathworld.wolfram.com/images/eps-gif/DicePlots_770.gif)

I created this plot to determine why the seemingly symmetrical answer of 8 was incorrect.\
After observing the plot from many angles, I concluded that a hexagonal cross section intersects more lattice points than a triangular one. The 6 edges of the hexagon connect lattice points better than the triangle's 3. Where the k = 8 triangle had a vertex, the k = 10 and k = 11 hexagons have sides that cross the top and bottom faces of the box.

![](http://mathworld.wolfram.com/images/eps-gif/CubeHexagon1_800.gif)

[Image credit: Wolfram Alpha](http://mathworld.wolfram.com/Cube.html)
</details>

Algebraic Interpretation
------------------------

<details>
  <summary>Click to expand!</summary>

In the corresponding homework question, [Professor Lyu](https://hanbaeklyu.com/) introduced an alternative approach to this question, which generalizes well for n dice.\
This method is computationally feasible and does not involve higher dimensional geometry.

Consider the following identity
(x + x<sup>2</sup> + x<sup>3</sup> + x<sup>4</sup> + x<sup>5</sup> + x<sup>6</sup>)<sup>3</sup>\
= x<sup>18</sup> + 3x<sup>17</sup> + 6x<sup>16</sup> + 10x<sup>15</sup> + 15x<sup>14</sup> + 21x<sup>13</sup> + 25x<sup>12</sup> + 27x<sup>11</sup> + 27x<sup>10</sup> + 25x<sup>9</sup> + 21x<sup>8</sup> + 15x<sup>7</sup> + 10x<sup>6</sup> + 6x<sup>5</sup> + 3x<sup>4</sup> + x<sup>3</sup>

The following are equivalent:
- coefficient of x<sup>k</sup>
- number of intersections between Ω and the plane x + y + z = k
- number of 3 dice arrangements that sum to k

*To connect the polynomial expansion to the geometric interpretation (and therefore the dice arrangements) . . .*

Compute the cube of (x + x<sup>2</sup> + x<sup>3</sup> + x<sup>4</sup> + x<sup>5</sup> + x<sup>6</sup>) by summing the products on a 3D grid with each axis labeled with ticks from x to x<sup>6</sup>. Recall the power rule: x<sup>m</sup> * x<sup>n</sup> = x<sup>m+n</sup>\
e.g. point (x, x<sup>3</sup>, x<sup>2</sup>) becomes the product x<sup>1+3+2</sup> = x<sup>6</sup>

Finally, group like terms (same power of x), analogous to counting the intersections with matching sums. Note that the coefficients of the expansion sum to 216 (6<sup>3</sup>) as expected.\
Thus, the algebraic and geometric interpretations are equivalent.

For a general n, expand the generating function (x + x<sup>2</sup> + x<sup>3</sup> + x<sup>4</sup> + x<sup>5</sup> + x<sup>6</sup>)<sup>n</sup>\
To learn more, look [here](https://www.qc.edu.hk/math/Advanced%20Level/Dice.htm), [here](http://mathforum.org/library/drmath/view/52207.html), or [here](https://eventuallyalmosteverywhere.wordpress.com/2014/02/02/generating-functions-for-dice/)
</details>
