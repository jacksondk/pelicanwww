Title: Deleting hidden Subversion files before zipping
Author: Michael Jacobsen
Date: 2011-12-19
Tags: programming, tips

Subversion holds various information in .svn directories placed in all
directories and sub-directories under version control. Sometimes it is
desireable to clean out these files, for example, prior to emailing a
zip of the files. I use the awesome tool Total Commander for the job.

The procedure is as follows

1. Start Total Commander and make a directory in a scratch area such as c:\temp.

2. Copy the directories to this tempoary directory

3. In the tempoary directory press Alt-F7 to enter search

4. Search for ".svn" files

5. Click the "Feed to list box" button

6. Select all files 

7. Delete

All the .svn directories are now deleted and the tempoary directory
can be zipped and mailed.

