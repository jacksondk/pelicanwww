Author: Michael Jacobsen
Date: 2012-04-09
Updated: 2012-10-14
Title: Interactive Main and Variance
Tags: math, statistics, demo
Category: math

This article tries to explain multiple concepts from statistics using
a small Javascript illustration of the correlation of two variables.

The <a href="http://en.wikipedia.org/wiki/Normal_distribution">normal
distribution</a> in one dimension is described by the probability
distribution 

$$ f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}} $$ 

where \\( \mu \\) is the mean and
\\( \\sigma \\) is the standard deviation. While the mean is easily
understood, the standard deviation measures how spread out the
distribution is. A large \\( \\sigma \\) implies that numbers further from
the mean are more likely.

## The Interactive Experiment
        
You can add points to the 'canvas' below by clicking with the
mouse. After adding a point the mean and variation is recomputed and
displayed. In the image you can see the mean displayed as a red
dot. Around the mean there is two ellipsis showing the 'iso-bar' for
\(\sigma\) and \(2\sigma\) - something I'll explain in more details
below.

The numerical values of the mean are shown in the first table next to
the canvas.  The second table shows the computed covariance.

<div style="height: 500px">
  <div style="float: left">
    <h3>Points</h3>
    <canvas id="gfx" width="600" height="400">
       You must use a browser which supports the canvas element.
    </canvas>
  </div>
  <div style="float: right; width: 230px;">
  <h3>Mean and covariance</h3>
  <p>You may edit the mean and covariance before clicking generate. However, there is no checks to detect if the data is invallid.</p>
  <style>
  td input.value
  {
    text-align: right;
    width: 4em;
  }
  </style>
  <table>
    <thead>
      <tr><th style="width: 1ex"></th><th>x</th><th>y</th></tr>
    </thead>
    <tbody>
      <tr><td>&nbsp;</td>
        <td><input type="text" id="avgx" class="value" /></td>
        <td><input type="text" id="avgy" class="value" /></td>
      </tr>
    </tbody>
  </table>
  <table>
    <tbody>
      <tr><td></td><th>x</th><th>y</th></tr>
      <tr><th>x</th>
         <td><input type="text" id="xx" class="value" /></td>
         <td><input type="text" id="xy" class="value" /></td>
      </tr>
      <tr><th>y</th>
         <td><input id="yx" type="text" class="value" /></td>
         <td><input id="yy" type="text" class="value" /></td>
      </tr>
    </tbody>
   </table>
   <button id="generate">Generate points</button>
   <button id="clear">Clear all points</button>
 </div>
</div>
        
## Computations
        
The mean can be computed as 

$$\bar{x} = \frac{1}{n} \sum_{i=1}^n x_i,$$ and $$\bar{y} = \frac{1}{n} \sum_{i=1}^n y_i.$$ 

However, we use an updating formula. 

The elements of the covariance matrix
are computed using the means via the following formulas 

$$
C_{11} = \frac{1}{n} \sum_{i=1}^n (x_i-\bar{x})^2
$$ 

$$ C_{22} = \frac{1}{n} \sum_{i=1}^n (y_i-\bar{x})^2$$ 

$$C_{12} = C_{21} = \frac{1}{n} \sum_{i=1}^n (x_i-\bar{x})(y_i-\bar{y}).
$$ 

However, for illustration purposes I need something that corresponds
to the standard deviation. Thus, I need to compute the square root of
\\(C\\). For an 2 by 2 matrix as \\(C\\) there exists an easy formula, see
e.g. <a
href="http://en.wikipedia.org/wiki/Square_root_of_a_2_by_2_matrix">
this Wikipedia article and square root(s) of 2 by 2 matrices</a>. If
we define the square root of the determinant of \\( C \\) as \\( s =
\sqrt{C_{11}C_{22}-C_{12}^2} \\).  Observe that \\( C \\) is positive
definite which implies that the determinant is positive and that \\( s \\)
is a positive real number. Furthermore, define \\(t =
\sqrt{C_{11}+C_{22}+2s}\\).  Then we have 

$$
S = \frac{1}{t} \left[
\begin{array}{cc} C_{11}+s & C_{12} \\ C_{12} & C_{22}+s
\end{array}\right] 
$$

The 'standard deviation' matrix is used to draw the
ellipses. Essentially, the matrix is used to transform a unit
circle. It is also used for the 'add points' functionality where
random two numbers are taken from \\( N(0,1) \\) to generate a random
point \\( [x \, y ]\\) and then transformed by multiplicatilon by \\( S
\\).


<script type="text/javascript" src="/static/js/sylvester/sylvester.js"></script>
<script type="text/javascript" src="/static/js/sylvester/matrix.js"></script>
<script type="text/javascript" src="/static/js/sylvester/vector.js"></script>
<script type="text/javascript" src="/static/js/data_analysis/dataanalysis.js"></script>
<script type="text/javascript" src="/static/js/data_analysis/covariance.js"></script>
<script type="text/javascript">
  $(document).ready(function () {
     initialize("gfx");
       });
</script>
