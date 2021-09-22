Title: Blur - Deblurring an Atmospheric Blurred Image
Author: Michael Jacobsen
Date: 2011-08-03
Tags: math, applet

During my Ph.D. I made a java applet demonstrating an inverse problem.
This article brings the applet back.

When light passes throug e.g. air it gets blurred. That is why
telescopes are built on top of mountains so that the weak light from
the stars travels through less air.
 
The extreme case is the Hubble telescope placed in orbit around
the earhth without any atmosphere to distort, i.e., blur the
image. However, when Hubble was first put into service a construction
error showed up which unfortunately distored the image. This
construction defect was later corrected by giving the telescope
glases.
  
This example shows how a nearsighted Hubble telescope or a
telescope placed on earth can be helped by means of mathematics.
 
## <a name="simple">A simple blurring function</a>
 
In this example we assume that the blurring is the same everywhere
in the detected picture --- it is spatial invariant. To illustrate how
the blurring works the pictures below show how an picture of a point
is blurred.
 
 
<center> 
<table> 
<tr> <td align="center"> Point </td> 
     <td align="center">Blurred Point</td> </tr> 
<tr> <td> <img src="/images/Blur/point.png"> </td> 
     <td> <img src="/images/Blur/psf.png"> </td> </tr> 
</table> 
</center>
 
 
Goint from the left picture to the right is easy, but the inverse
operation going back from the right to the left is much harder. It is
a socalled ill-posed inverse problem, and regularization is called
for.
 
# <a name="applet">The Deblurring Applet</a>

Last update of applet 2001-12-18.
 
A number of parameters control the generation of the example problem:
 
 
* n: The number of pixels in each direction. Keep this small for
  fast calculations. The maximum is 200.
 
* blur: The "degree" of blur. A large number yeilds a wide point
  spread function and thus an very ill-conditioned problem.
 
* noise: To each measurement we add a gaussian distributed random
  number with standard deviation noise to simulate measurement
  inaccuracies.
 
* outliers: A number of outliers (extremely false) measurements can be
  added to further complicate the solution process.

Three basic regularization methods are provided to illustrate the
solution:
 
* T-SVD, Truncated SVD: [From a project description](http://www.imm.dtu.dk/~pch/Projekter/tsvd.html)
 
* [Tikhonov Regularization](http://en.wikipedia.org/wiki/Tikhonov_regularization)
 
* CGLS, Conjugate Gradient Least Squares - an adoption of the
  iterative [conjugate graident/CG
  method](http://en.wikipedia.org/wiki/Conjugate_gradient_method) for
  least squares methods.
 
<center> 
  <applet archive="/java/BlurDemoApplet.jar" code="BlurDemoApplet" width=730 height=450> </applet> 
</center>
