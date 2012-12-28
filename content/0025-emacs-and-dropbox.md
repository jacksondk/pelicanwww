Title: Emacs and DropBox Integration
Date: 2011-02-24
Author: Michael Jacobsen
Tags: programming, tips

If you use more than one computer chances are that you use <a
href="http://www.dropbox.com">DropBox</a> to keep a number of often
used files syncronized and at hand.

I also like to have at least a somewhat similar configuration of
various programs on systems. With respect
to <a href="http://www.gnu.org/software/emacs/">emacs</a> I have the
following .emacs

<pre>
;; For convenience add the dropbox directory as a variable
;; and set the default directory to that very same one
;; Thus, when storing files you 'start path' will be in
;; the dropbox.
(setq dropbox-directory "c:/Users/mj/Documents/My Dropbox/")
(setq default-directory dropbox-directory)

;; Add the dropbox/emacs dir to the load path
(setq load-path (cons (concat dropbox-directory "emacs/") load-path)

;; Load the settings that I want on all computers
(load "mj-startup")
</pre>

Of course you need to modify the paths to fit with your DropBox setup
and your choice of extra setup.
