Title: Heat - Remote Sensing of Temperature
Author: Michael Jacobsen
Date: 2008-03-01
Tags: math, applet

The problem is to deduce how the temperature changes (we will call
this a temperature profile) at one place from measurements at another
place.
 
We restrict ourselves to a 1-D problem. Assume that we can apply a
temperature profile (f(t)) to the end of a rod (at the position x =
0).  We now define the forward problem that gives the temperature
profile at any point by means of a Partial Differential Equation
(PDE):
 
<center> 
<IMG  WIDTH="274" HEIGHT="76" BORDER="0"
 SRC="/images/Heat/heatpde.gif"
 ALT=" 
  u_t = \kappa^2 u_{xx}, \quad 0 &lt; x &lt; \infty, \quad 0 &lt; t &lt; ...
...0 \le x \le \infty, \\
&amp; u(0,t) = f(t), \quad 0 \le t &lt; \infty "> 
</center> 

We have assumed that the rod is isolated such that no energy escapes
through the top and bottom. Furthermore we assume that the rod has
initial temperature 0 everywhere. The solution is

<center> 
<IMG
 WIDTH="355" HEIGHT="46" BORDER="0"
 SRC="/images/Heat/heatsolution.gif"
 ALT=" 
u(x,t) = \frac{x}{2 \kappa \sqrt{\pi}}
\int_0^t \frac{f(\...
... \left(
\frac{-x^2}{4 \kappa^2 (t - \tau )}
\right) d\tau ."> 
</center> 

Hereby we can find the temperature at any point at any point in time
using the above formula. This was the forward problem. </p> 
 
The inverse problem is when we have a temperature profile g(t) at some
point x = l <= 0 and wish to find the temperature profile f(t) at end
of the rod. This occurs in practice when the end of the rod is
inaccessible.
 
<center> 
<IMG
 WIDTH="660" HEIGHT="182" ALIGN="BOTTOM" BORDER="0"
 SRC="/images/Heat/heatsetupfigure.gif"> 
    <br> 
    <b> Figure 1: Illustration of forward and backward (inverse)
 problem. </b> 
</center>
 
From the previous we see that the forward problem poses no problems as
we have a closed form solution. The inverse is on the other hand much
more difficult. One can imagine that many different temperature
profiles f(t) will yield the same measurements g(t) at least when we
also include measurement accuracy. The forward operation smoothens the
temperature profile as we travel down the rod. Therefor the inverse
operation must desmooth as we go towards x = 0, but it the operation
will also be applied on the noise and errors made in the
measurements.
 
In this case an many others a naive solution of the inverse problem
will yield unusable results due to the influence from the
noise. Regularization is a technique to stabilize the inverse problem
such that some information can be extracted. The applet is constructed
to demonstrate this.
 
# <a name="applet">The Regularization Applet</a>

Last update of applet 2001-07-31.
 
The problem is discretized to have 128 points. Therefor you can use
the integers from 0 to 128 as argument for T-SVD. Tikhonov accepts
all values greater than or equal to zero. CGLS accepts integers
greater than 0.
 
 You can read more details on the algorithms and methods if you follow
the links
 
* T-SVD, Truncated SVD: <a
  href="http://www.imm.dtu.dk/~pch/Projekter/tsvd.html">From a project
  description</a>
 
* <a
  href="http://en.wikipedia.org/wiki/Tikhonov_regularization">Tikhonov
  Regularization</a>
 
* CGLS, Conjugate Gradient Least Squares - an adoption of the
  iterative <a
  href="http://en.wikipedia.org/wiki/Conjugate_gradient_method">conjugate
  gradient/CG method</a> for least squares methods.
 

## Instructions

You can change the source (solution) by dragging the points with the
mouse. The parameter kappa controls how difficult (ill-posed) the
problem is, a value of 1 gives an ill-posed problem while a value of 5
makes a fairly easy problem (well-posed). You can increase the noise
level and the number of outliers to hide information.
 
To see the naive solution select k = 128 for T-SVD or lambda = 0 for
Tikhonov. Notice that even with very little noise we get very bad
results.
 
<center> 
<applet archive="/java/RegularizationDemoApplet.jar"
code="RegularizationDemoApplet"
width=730 height=450> </applet> 
</center>
 
Observe that outliers makes it very hard to find a good solution. Also
sources with discontinuities are hard to reconstruct using these
regularization techniques.