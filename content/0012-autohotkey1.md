Title: Two Monitors and AutoHotKey
Author: Michael Jacobsen
Date: 2008-09-03
Updated: 2010-06-04
Tags: programming, tips

I prefer to use the keyboard whenever possible. I have a two monitor
setup and found myself moving windows from one monitor to the other
using the mouse. However, using AutoHotKey I was able to do this by
keyboard. Also I wanted to swithc easily to a particular window using
the keaboard.

Update: The functionality has now been integrated into Windows 7. 

[AutoHotKey](http://www.autohotkey.com) is an utility for creating hot
keys. Each hot key can runs a command or a small script. My setup is
currently as follows:

<pre class="prettyprint">
#Up::
	WinMaximize,A
return

#Down::
	WinRestore,A
return

+#Down::
	WinMinimize,A
return

#Left::
	WinRestore,A
	WinGetPos,X,Y,,,A
	if X >= 1919
	{	
		WinMove,A,,X-1920,Y
	}
return

#Right::
	WinRestore,A
	WinGetPos,X,Y,,,A
	if X < 1920
	{
		WinMove,A,,X+1920,Y
	}
return

#1::
	WinRestore,A
	WinMove,A,,0,0,960,1140
return

#2::
	WinRestore,A
	WinMove,A,,960,0,960,1140
return

#3::
	WinRestore,A
	WinMove,A,,1920,0,960,1200
return

#4::
	WinRestore,A
	WinMove,A,,2880,0,960,1200
return

#Space::
	Run,c:\bin\TaskSwitcher32.exe
return

#F2::
	Run,c:\bin\TaskSwitcher32.exe /title outlook
return

#F3::
	Run,c:\bin\TaskSwitcher32.exe /title firefox
return

#F4::
	Run,c:\bin\TaskSwitcher32.exe /title "visual studio"
return

#F5::
	Run,c:\bin\TaskSwitcher32.exe /title "total commander" /exe "c:\programmer\totalcmd\totalcmd.exe"
return

#F6::
	Run,c:\bin\TaskSwitcher32.exe /title "putty" /exe "C:\Programmer\PuTTY\putty.exe"
return

#F7::
	Run,"C:\Programmer\PuTTY\putty.exe"
return

#F8::
	Run,c:\bin\taskswitcher32.exe /title opera
return

#F9::
	Run,c:\bin\taskswitcher32.exe /title "emacs" /exe "f:\emacs-22.1\bin\runemacs.exe"
return
</pre>

A line such as #Left:: means "When Windows - Left arrow" is pressed do
the following. In this case I check the position of the window. If it
is on my right monitor, I move it to the left monitor. #Right does the
opposite, #Up maximizes the window, #Down restores the window (not
very useful., but stays for the moment). If your setup uses monitors
with a width different from 1280 you should change the constants.

The small utilty "TaskSwitcher32.exe" used in the AutoHotkey script
above is a small utility created by me. It's Freeware, see
[TaskSwitcher32](/a-native-win32-taskswitcher.html).
