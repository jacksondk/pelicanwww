Title: Kensington Mouse Drivers Kills Click-Once
Author: Michael Jacobsen
Date: 2009-04-10
Tags: debug, programming

For a long time I had a strange problem on my workstation. Some
programs crashed before showing a window. For example, I was unable to
run programs in the standard Visual Studio projects folder under my
documents and settings. But they ran fine when moved somewhere else. I
suspected some permission problem but I could not find and thus fix
it.

Another program that I have helped develop, <a
href="www.farmguard.com">FarmGuard</a>, had an even more bizarre
behaviour. It would run until I switched out of the program and back!
That is,

<ul>
<li>Start the program</li>
<li>Do none or some work in the program - it works perfectly</li>
<li>Switch to another window - no matter which</li>
<li>Switch back to the FarmGuard window</li>
<li>Crash! The window simply disappears - no asking about debugger - just nothing</li>
</ul>

Attaching the Windows debugger showed me that it was a stack overflow
but my skills with the debugger is not good enough to find out more
than that. And this only happened when I used the version installed
via Click Once and not when I ran the exact same program from the
build directory. The FarmGuard program is written en C# with the WPF
framework which should eliminate stack overflow problems on our
part. I tried upgrading my GFX drivers but no luck.

Then by change I stumpled on <a
href="http://blogs.msdn.com/winformsue/archive/2006/05/22/604103.aspx">an
article from Microsoft</a>. And yes removing the drivers for my
trackball solved all my issues. Note the date on the article - it is
from 2006 and Kensington has not fixed their drivers yet!

The driver uses a 128 byte buffer to do something about the path of
the program. When you use Click-Once (FarmGuard) or are in a subdirectory of

<pre class="prettyprint">
c:\Documents and Settings\user\Document\Visual Studio 2008\My Projects\.
</pre> 

A large number of bytes are used before you get to the actual
executeable and you overflow the buffer, destroys the stack
effectively crashing the program.

Who would expect a mouse driver to cause such strange behaviour.