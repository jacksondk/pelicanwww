Title: How far can you see?
Author: Michael Jacobsen
Tags: math
Date: 2011-02-27

How far can you see when you are, say, 2 meters high? Lets find out
assuming that we stand on a perfect circle with perfect visibility
([and that we do not have
refraction]("http://mintaka.sdsu.edu/GF/explain/atmos_refr/horizon.html").

# The Math

In Figure 1 I have sketched the situation. The distance \(c\) is the
radius of the sphere (could be the radius of the earth). The distance
\(a\) is the hight of the observer above the circle. The key point is
that the triangle (A,B,C) must be a right triangle where the angle at
B where the line of sight meets the horizont must the right angle. The
distance of the line of sight we call \(b\).

<object data="/ArticleImages/HowFarToSee/how-far-can-you-see.svg" width="400px" height="400px" type="image/svg+xml"></object>

Depending on the initial attack angle you end up with an extremely simple solution
or a more complicated solution. I, of course, started out doing the complicated 
solution (option 1 in the following). The simple solution is described under option 2.

## Option 1

We assume that we know the radius of the circle (that is, \(c\)) and the
hight of the observer (that is, \(a\)). By using Pythagoras we get

$$ (c+a)^2 = b^2 + c^2 \Leftrightarrow b^2 = a^2 + 2ac $$.

We can safely assume a positive \(b\),

$$ b = \sqrt{ a^2 + 2ac } $$

which gives the distance measured by line of sight. However, if we
walked the distance we would follow the circle which is larger than
\(b\).  

The formula for sine in a right triangle states

$$ \sin ( \theta ) =  \left( \frac{b}{c+a} \right) $$

which gives us

$$ \theta = \arcsin \left( \frac{b}{c+a} \right) $$

Now we only need to scale with the radius \(c\) to get the distance
following the circle

$$ d = c \arcsin \left( \frac{\sqrt{a^2 + 2ac}}{c+a} \right) $$

## Option 2

When I came to computing the \( \theta \) angle I wondered - why not go directly to 
this angle via the cosine function?

Hereby we get

$$ \cos ( \theta ) = \frac{c}{c+a} .$$

So much simpler.....

# Applications

## How far can I see?

Lets assume the earth to be a perfect sphere with a radius of
\(6357.5\cdot10^3\) meters
(<a href="http://www.wolframalpha.com/input/?i=radius+of+earth">source</a>)
and that I'm $1.8$ meters high. Simply putting the data into the
formalat yields

$$ 6357.5 \cdot 10^3 \arccos 
\left( \frac{6357.5 \cdot 10^3}{6357.5 \cdot 10^3 + 1.8} \right)
\approx 4784, $$

that is, almost 5 km.

## How high to see from LA to Tokoy?

According to Wolfram Alpha the distance
is <a href="http://www.wolframalpha.com/input/?i=distance+from+LA+to+tokyo">8818
km</a> or about 1/5 of the earth circumference. Had it been more than
1/4 it would not have been possible to look that far.

In this case \(\theta = 8818/40075 \approx 0.22\) and \(c\) is
known and we need to solve for \(a\).

$$\cos ( 0.22 ) = \frac{ 6357.5 \cdot 10^3 }{6357.5 \cdot 10^3 + a} \Leftrightarrow a \approx 157.0 \cdot 10^3 $$.

The Internation Space Station is in orbit about 386 kilometers above
the earth. That is, if they pass over LA or Tokyo they are more than
capable of seeing the other city!



