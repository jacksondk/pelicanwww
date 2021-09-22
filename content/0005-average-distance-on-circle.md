Title: Average Distance on a Circle
Author: Michael Jacobsen
Date: 2008-09-03
Tags: math

<SCRIPT SRC="/js/raphael.js"></SCRIPT>

What is the average distance between two points on a circle?

We define the distance as going through the circle as going around the
circle reduces the problem to the problem of average distance on a
line, see [Average Distance on a
Line](/average-distance-on-a-line.html).

The circle as one of the most symmetric shapes we can thing of. Thus
we can select the (1,0) on the unit circle and compute the average
distance to any other point. If you use a browser supporting the
"canvas" tag you should see an animated illustration of the problem
below

<div class="center">
<table>
<tr><th style="text-align: center">Figure</th><th style="text-align: center" colspan="2">Statistics</th></tr>
<tr><td rowspan="5">
<div id="canvas"></div>
</td>
<th>Iterations</th><td id="iteration_count"></td></tr>
<tr><th>Current</th>     <td id="current_length" class="numeric"></td></tr>
<tr><th>Average</th>     <td id="average" class="numeric"></td></tr>
<tr><th>"True value"</th><td id="truevalue" class="numeric"></td></tr>
<tr><th>Error</th>       <td id="error" class="numeric"></td></tr>
</table>
</p>
<style>
td.numeric {
  font-family: monospace;
  text-align: right;
}
</style>
<script type="text/javascript">
  var elem = document.getElementById( "canvas" );
  var c = Raphael( elem, 300, 200 );
  var width = 300;
  var height = 200;
  var iterations = 0;
  var sum = 0.0;

      function update_stats( n, sum, c )
      {
         document.getElementById( "iteration_count" ).innerHTML = n;
         document.getElementById( "current_length" ).innerHTML = c.toFixed(8);
         document.getElementById( "average" ).innerHTML = (sum/n).toFixed(8);
         document.getElementById( "truevalue" ).innerHTML = (4.0 / Math.PI).toFixed(8);
         document.getElementById( "error" ).innerHTML = (sum/n - 4.0 / Math.PI).toFixed(8);
      }
  
  function draw()
  {
       var a = Math.random()*Math.PI;
       var cy = 0.9*height;
       var cx = width / 2;
       var r = 0.95*( cx > cy ? cy : cx );
       c.clear();
       c.circle( cx, cy, r );
       c.path({stroke: "#036"}).moveTo(0, cy).lineTo( width, cy );
       c.path({stroke: "#536"}).moveTo( cx, 0).lineTo( cx, height );
       var line = c.path({stroke: "#00f"}).moveTo( cx + r, cy ).lineTo( cx+r*Math.cos( a ), cy-r*Math.sin( a ) );
 
       iterations = iterations + 1; 
       var current_length = Math.sqrt( (1-Math.cos(a))*(1-Math.cos(a)) + Math.sin( a )*Math.sin( a ) );
       sum = sum + current_length;
       update_stats( iterations, sum, current_length );
       setTimeout( "draw()", 1000 );
  }
  
  draw();
</script>
</div>

The problem is to determine the average length of the blue line.

The unit circle is described by the function

$$
  p( \theta ) = \sqrt{ (1-cos \theta )^2 + sin^2 \theta }
$$

where we get our reference point when $$\theta = 0$$

Going through the circle we have the distance function

$$
  d(x_0, p( \theta ) ) = \sqrt{ (1-\cos \theta )^2 + \sin^2 \theta }
$$

Due to symmetry we can look at the circle in the upper plane, that is,
for \\( \theta \in [0;\pi] \\). We are now ready to
integrate the distance function

$$
  \frac{1}{\pi} \int_{0}^{\pi} d(x_0, p( \theta ) d\theta  
$$

Using the free collection of mathematical software
[Sage](http://www.sagemath.org/) we get that


$$
\int d(x_0, p( \theta ) d\theta = 
\frac{-4}{ \sqrt{ \frac{\sin^2\theta}{(\cos \theta + 1)^2} + 1}}
$$

However, if we use this indefinite integral to compute the result of
the definite integral we get

$$
\frac{-4}{\pi} \left[  
  \frac{1}{ \sqrt{ \frac{\sin^2\pi}{(\cos \pi + 1)^2} + 1}} - \frac{1}{ \sqrt{ \frac{\sin^2 0}{(\cos 0 + 1)^2} + 1}}
\right]
$$

and a division with zero in the first term within the
parenthethis. Bummer, we need to get a bit more creative.

If we approach \\( \pi \\) that is we get limit and using L'Hospitals
rule once ([L'Hospital on
Mathworld](http://mathworld.wolfram.com/LHospitalsRule.html) we get

$$
 \lim_{x \leftarrow \pi} \frac{\sin^2 x}{(\cos x + 1)^2} = \lim_{x \leftarrow \pi} \frac{- \cos x}{\cos x + 1} = 0
$$

because the denominator goes to zero while the nominator goes to -1.

Thus ``we set the first term to zero'' we get the result that the
average distance is

$$
  \frac{-4}{\pi} (-1) = \frac{4}{\pi}
$$


Monte-Carlo integration seems to verify the result - if the Javascript
of this page is running you will see the Monte-Carlo estimate next to
the animation above.
