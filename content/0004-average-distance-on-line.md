Title: Average Distance on a Line
Author: Michael Jacobsen
Date: 2008-09-02
Tags: math

As warm-up to the question of average distance between two points on a
circle I'll start out finding the average distance between two points
on a line.

For one particular point x we have an average distance to n other
points as

$$ \sum_{i=1}^n | x - y_i | \frac{1}{n} $$

where we sum each distance times its probability (1/n). If take ``all
points'' on line of unit length we get a [Rieman
Integral](http://en.wikipedia.org/wiki/Riemann_integral "Wikipedia
article on the Rieman Integral"), that is

$$ \int_0^1 | x - y | dy $$

The absolute value is ``bad'' for integration so we split the
intergral in two around x we get

$$ \int_0^x ( x - y ) dy + \int_x^1 ( y-x) dy $$

and now we just go with the usual rules

$$
\begin{eqnarray} 
\left[ xy - \frac{1}{2} y ^ 2 \right]_0^x +  \left[ \frac{1}{2} y ^ 2 - xy \right]_x^1 
& = & x^2-\frac{1}{2}x^2 + \frac{1}{2} - x - (\frac{1}{2}x^2-x^2) \\ 
& = & x^2 - x - \frac{1}{2} 
\end{eqnarray}
$$ 

Hereby we get the unsurprising result that average distance from 0 to
another point in [0;1] is 1/2 (likewise for 1). The average distance
for the point 1/2 is 1/4. But that is just three samples. What about
the average for all points?

Let us integrate once more

$$
\begin{eqnarray} 
\int_0^1 \frac{1}{2}x^2 - x + \frac{1}{2} 
& = &  \left[ \frac{1}{3} x^3 - \frac{1}{2}x^2 + \frac{1}{2}x \right]_0^1 \\
& = & \frac{1}{3} - \frac{1}{2} + \frac{1}{2} - 0 \\
& = & \frac{1}{3}. 
\end{eqnarray}
$$ 

That is, the average distance between two random points on a straight
line of unit length is 1/3.
