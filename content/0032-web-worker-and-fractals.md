Title: Creating Fractals with Web Workers
Author: Michael Jacobsen
Date: 2012-02-26
Tags: math, html5, programming

A Web Worker makes it possible to run Javascript code without blocking
the user interface. That is, computations can be made in the background
without locking the user interface.

A Web Worker is created as follows

<pre class="prettyprint">
// Main script
var worker = new WebWorder( url );
</pre>

where url must point to a Javascript file. The script is started immediately. This
article describes the 'standard' Web Worker, not the 'shared' Web Worker.

Web Workers are not threads as known from C#, Java or the like. The
Web Worker does not share memory with the script that initiates it (as
in C# and Java). In stead, communication is done through
messages. Thus, it compares more to processes with some kind of
inter-process communication. In order to receive a message from a Web
Worker you attach to the onmessage event.


<pre class="prettyprint">
// Main script
worker.onmessage = function( eventData ) {
};
</pre>

Similarly a worker can recieve messages with the onmessage event in its global scope

<pre class="prettyprint">
// Worker script
onmessage = function( eventData ) {
};
</pre>

In order to send messages the method postMessage is used. For the Web
Worker the function exist on the global scope, that is,

<pre class="prettyprint">
// Worker script
postMessage( data );
</pre>

The main script uses the postMessage method on the worker object, that is,

<pre class="prettyprint">
// Main script
worker.postMessage( data );
</pre>

The data transfered between worker and main script (in either direction) are only
json like objects.
        
My example uses Web Workers to compute rows of fractals in the complex
plane. A (variable) number of workers are initialized with the
dimensions of the complex plane and the coresponding height and width
of a canvas. The main script then sends messages to each worker asking
it to compute a row. When a row has been computed a message is posted
to the main script, which then updates the image. If more rows remains
the worker is put to work again.

# Mandelbrot and Julia fractals

Both the Mandelbrot and the Julia fractals are defined for the complex
plane. They are computed using the formula $$v_{i+1} = v_i^2 +
p$$. The difference between the Mandelbrot and Julia fractals lie in
the initialization of the formula. The Mandelbrot has \\(v_0 = 0\\)
and \\(p\\) is the point on the complex plane under investigation.
The Julia set uses \\(v\\) as the point in the complex plane under
investigation while \\(p\\) is some point in the complex plane. That
is there is a Julia fractal for each point in the complex plane. More
detailed explanations are available at Wikipedia <a
href="http://en.wikipedia.org/wiki/Mandelbrot_set">Mandelbrot set</a>,
<a href="http://en.wikipedia.org/wiki/Julia_set"> Julia
set</a>. Another option is at Mathworld, <a
href="http://mathworld.wolfram.com/MandelbrotSet.html"> Mandelbrot
set</a> and <a href="http://mathworld.wolfram.com/JuliaSet.html">Julia
set</a>

Enough talk and code - let's see some pictures!

Number of workers to use during computations
<input type="text" value="2" id="workerCount" /><input id="render" type="button" value="Redraw" />

<canvas id="fractal" width="700" height="600">This feature needs canvas support!</canvas>

Duration of last Mandelbrot set computation <span id="duration"></span>ms</p>

Each point of complex plane has a Julia set associated. Click on a
point on the above Mandelbrot set and the corresponding Julia set will
be drawn on the canvas below. The most interesting examples are found
along the edge of the Mandelbrot set.

<canvas id="julia" width="700" height="600">This feature needs canvas support!</canvas>

Duration of last Julia set computation <span id="juliaDuration"></span>ms

<script type="text/javascript" src="/js/fractal/complex.js"></script>

<script type="text/javascript" src="/js/fractal/fractal.js"></script>

<script type="text/javascript">
            $(document).ready(function () {
                var fra = new jacksondk.Fractal(document.getElementById("fractal"), 2);
                fra.ondone = function (duration) {
                    $("#duration").html(duration);
                };
                fra.render();
                var julia = new jacksondk.Fractal(document.getElementById("julia"), 2);
                julia.ondone = function (duration) {
                    $("#juliaDuration").html(duration);
                };
                julia.setType("julia");
                julia.setTopLeft(new Complex(-2, 2));
                julia.setBottomRight(new Complex(2, -2));
                $("#render").click(function () {
var c = document.getElementById("fractal");
var ctx = c.getContext("2d");
ctx.clearRect(0,0,c.width,c.height);
                    fra.workerCount = parseInt($("#workerCount").val());
                    fra.setType("mandelbrot");
                    fra.render();
                });
                $("#fractal").click(function (event) {
                    var x = event.offsetX;
                    var y = event.offsetY;
                    var r = fra.topLeft.real + ((fra.bottomRight.real - fra.topLeft.real) / fra.width) * x;
                    var i = fra.topLeft.imag + ((fra.bottomRight.imag - fra.topLeft.imag) / fra.height) * y;
                    julia.juliaPoint = new Complex(r, i);
                    julia.render();
                });
            });
</script>

# A Couple of Words on Performance

I've tested the code in three browsers

* Chrome 18.0.1025.33 beta-m
* Firefox 10.0.2
* Opera 11.61

with different numbers of Web Workers. I did not have the patience to
do a actual benchmark comparing runtimes. However, Chrome is much
faster than the other two.  Furthermore, it seems that Opera does not
benefit from using more Web Workers.

# Source Code

The source code is available for browsing, and forking at <a
href="https://github.com/jacksondk/fractal">my GitHub 'fractal' repos
page</a>