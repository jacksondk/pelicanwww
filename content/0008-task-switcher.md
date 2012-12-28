Title: A Native Win32 TaskSwitcher
Date: 2008-09-03
Author: Michael Jacobsen
Tags: programming, tips

My previous task switcher application had a serious performance
problem as it was programmed in .NET. In order to start the small
utility you had to load up the CLR and a bunch of assemblies
(dlls). If you are a .NET developer it might not be that big a problem
as most of the code was already loaded up. However, for general use it
was not the best option.

Hence, I ported the utitly to C++ with the MFC framework to help
me. The result can be downloaded here:
[TaskSwitcher32.exe](/static/downloads/TaskSwitcher32.exe). The executable is
staticly linked with the MFC library and has no dependencies besides a
standard Windows system. It has been tested on XP 32 bit and Vista 64
bit. I see no reason for the utility not to work on other similar
platforms.

# Usage

Place the program somewhere in your file system. If you start the
program without options you get a list of windows. You can select a
window using the arrow keys and make the window the foreground window
using the enter key. You can type text in order to limit the number of
windows shown. The search searches the window title and the
corresponding executable name (both in LOWER case).

<img src="/images/TaskSwitcher/taskswitcherscreenshot.png">

The program can be used with a couple of command line arguments:


  * /title "search" initializes the program with a search
  criteria. If only one window matches, we skip the dialog and makes
  it the foreground window immediately. If multiple windows matches we
  show the dialog with the search criteria included. If no window
  matches - the following arguments are used:
  
  * /exe "executable with arguments" starts a program if no windows
  matches the search criteria. 
  
  * /wdir "workingdir" specifies the working directory used when
  starting the above process.

  
  * /help Show a small help  message.

Observe, that this little utility goes very well with AutoHotKey [see
previous article on AutoHotKey](//autohotkey1.html)

# Other notes, license, .... 

The program is provided as is. You may use it privately and
commercially. If you really like the program you can make me happy by
sending an email of appreciation. You may also send feature requests
and bug reports. The email is mic.jacobsen@gmail.com.
