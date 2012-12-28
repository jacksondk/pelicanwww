Title: Provisioning a Windows Mobile PDA for developement
Author: Michael Jacobsen
Date: 2011-01-05
Tags: programming, tips

I had my old Windows Pocket PC 2003 stolen from my office and until
now I have developed on the emulator. However, now the need for a
physical device has come up and I got the HP IPAQ 214.

The old PDA was plug'n'play with respect to developing, that is,
deploying from Visual Studio and so is the emulators. However, the
iPAQ 214 did not allow me to deploy due to some security
permissions. As it was the first time I ran into this problem I
fumbled arround until I discovered that I should copy the Certs.cab
file from the Windows Mobile 6 SDK to the device (via Active Sync) and
run it (using File Explorer on the device).

Now I have access.

# Other notes

Sometimes ActiveSync fails to connect to the emulator. My solution is
to go to File->Connection Settings and remove the check for "Allow
connections to one of the following:" where the drop down box below
has "DMA" selected. Click OK, go back in the settings and recheck the
box. Now ActiveSync and the emulator connects...