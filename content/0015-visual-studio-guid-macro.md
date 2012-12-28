Title: Visual Studio 2008 GUID Macro
Author: Michael Jacobsen
Date: 2009-07-22
Tags: programming

I have never completely understood why Visual Studio had to start
another (graphical) utility in order to create GUIDs. I'm all for the
UNIX kind of small (text based) utilities than can be
combined. Furthermore, this utility creates GUID in formats that are
useful to C++ programmers. Why have they not used the built in Macro
system?

On the other hand it makes it possible for me to try out Visual Studio
macro programming. Unfortunately the macro language is Visual Basic
and it hurts my eyes, but for this small job I should be able to
survive.

So here it is 

    Public Module Module1

      Sub InsertGuid()        
        Dim doc As EnvDTE.Document
        Dim sel As EnvDTE.TextSelection

        doc = DTE.ActiveDocument
        sel = doc.Selection        
        sel.Insert(System.Guid.NewGuid().ToString())
      End Sub

    End Module

That is, take the active document. Find the current point and insert a
newly created GUID (as text). And viola, we have a Guid which we can
attach a keyboard shortcut to. No need to start another GUI
application.

And finally my wish to future versions of Visual Studio:

Please allow other languages than VB.NET (C#, F# and IronPython comes
to mind (or how about elisp))
