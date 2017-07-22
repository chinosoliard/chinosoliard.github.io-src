Title: Samsung printers on Fedora
Date: 2012-10-21 19:00
Category: Fedora
Tags: CLP-315, CUPS, Fedora, GNU/Linux, printer, ML-1640, samsung, Samsung Unified Linux Driver, SPLIX
Lang: en
Slug: samsung-printer-on-fedora
Summary: I have 2 Samsung laser printers since 2 years ago, a [ML-1640](http://www.samsung.com/es/consumer/pc-peripherals-printer/printers/laser-monocrome-printers/ML-1640/SEE) and a [CLP-315](http://www.samsung.com/es/business/printer/productos-y-soluciones/impresoras-y-faxes/impresoras-l%C3%A1ser-color/clp-310-/impresora-l%C3%A1ser-color-clp-315/feature.prt?printerCode=CLP-315/SEE). Honestly, I never spent too much time to make them work in GNU/Linux, when I try to do it, only with [CUPS](http://www.cups.org/), I couldn’t do it. Now, that I’m using [Fedora](http://www.fedoraproject.org/es/) 99,9% of the time that I’m sitting at a computer, I had to find the way to make them work. After ask a question in [ask.fedoraproject.org](http://ask.fedoraproject.org), I recieved 2 answers, one of which worked.

The first (and no functional) option was install the [Samsung Unified Linux Drivers](http://downloadcenter.samsung.com/content/DR/200911/20091118145015140/UnifiedLinuxDriver_1.01.tar.gz), I executed the installer with “$ sudo” and start the installation. During the installation, it’s possible installing printers, I plug the ML-1640, and everything looks to be right. When I finished the installation, I go to CUPS page ([http://localhost:631](http://localhost:631/)) and the printer were on the list. Among many details that I can’t remember, all I know is that the printer never worked, I searched the Internet and found that the package was very problematic, then I want to uninstall the package, for this, in a console run $ sudo / opt / Samsung / mfp / uninstall / guiuninstall, this will start the uninstallation. After a few steps, the program did not leave traces (or it seems).

The second (and functional), and simpler, is installing Splix, a set of CUPS drivers that handle SPL (Samsung Printer Language). Following, I explain how I did.

1. Now is packaged for Fedora, so, all you have to do to install the package is run in a console 
  `$ sudo yum install splix`

2. 2. After installing Splix, just connect the printer (windows appear to install drivers, but cancel) and go to CUPS (http://localhost:631), once in CUPS, we go to Administration, and then to “Add printer “.

3. The printer appears connected in the list of local printers, select it and press “next”. 
[![samsung-printer-on-fedora-1](/images/article/2012/10/samsung-printer-on-fedora-1.png)](/images/article/2012/10/samsung-printer-on-fedora-1.png)

4. After, configurations for printer name, description, location, and the option of sharing appears; We click on “next” (after set the fields to taste).
[![samsung-printer-on-fedora-2](/images/article/2012/10/samsung-printer-on-fedora-2.png)](/images/article/2012/10/samsung-printer-on-fedora-2.png)

5. We got to the step where we define the controller, in the list “Model” select the model you are installing, then “Add Printer”.
[![samsung-printer-on-fedora-3](/images/article/2012/10/samsung-printer-on-fedora-3.png)](/images/article/2012/10/samsung-printer-on-fedora-3.png)

6. Finally, we are asked to establish the default options for the printer
[![samsung-printer-on-fedora-4](/images/article/2012/10/samsung-printer-on-fedora-4.png)](/images/article/2012/10/samsung-printer-on-fedora-4.png)

7. Once we are in the printer’s page in CUPS, we can test the printer selecting “Print Test Page” in the “Maintenance” menu.
[![samsung-printer-on-fedora-5](/images/article/2012/10/samsung-printer-on-fedora-5.png)](/images/article/2012/10/samsung-printer-on-fedora-5.png)



The printer is working, but, to me personally, four printers appear installed on the CUPS printer list, so I removed the ones I didn’t install (detected by the name).
[![samsung-printer-on-fedora-6](/images/article/2012/10/samsung-printer-on-fedora-6.png)](/images/article/2012/10/samsung-printer-on-fedora-6.png)

Well, that’s the simply way to install the printers, I hope you have been useful.
