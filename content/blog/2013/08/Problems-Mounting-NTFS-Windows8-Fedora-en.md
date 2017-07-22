Title: Problems mounting NTFS partitions from Windows 8 on Fedora
Date: 2013-08-17 19:00
Category: Fedora
Tags: Fedora, GNU/Linux, issue, NTFS, partition, power, problem, Windows, Windows-8 
Lang: en
Slug: problems-mounting-ntfs-windows8-fedora
Summary: My computers have a configuration to automatically mount some NTFS partitions when Fedora starts, in these partitions I share files between Windows and Fedora.</br></br>I recently upgraded to Windows 8, and after meeting him, I wanted to boot Fedora again, and gave me an error trying to mount the partition.</br></br>Here, I explain what is happening and how to solve it.  

Windows 8 brings enabled by default “Quick Start”, this feature is for Windows to start in a time relatively short (very noticeable compared to other Windows versions), and works by making the system does not shut down completely, if that is not a state “partial” hibernation, I mean, saves the state of the system into a file on disk, and when you start the system again, load the file contents, leaving the system in the same way that when turned off.  

The problem comes when, in my case for this example, I want to start GNU / Linux which has a configuration in / etc / fstab to automatically mount the partition I use to share data between the two operating systems, Fedora tells me that you have problems mount that partition.
The solution is simple, disable this feature in Windows, to do this …  

1. Boot up Windows 8  

2. At the start menu, type “power management”.  

3. On the right side menu, go to “Settings” tab.  

4. There, select from the left menu the option “Change startup / shutdown button actions”.”  
   [![nfts-1](/images/article/2013/08/ntfs-1.png)](/images/article/2013/08/ntfs-1.png) 

5. It opens a “System Configuration” window with some blocked options, we click “Change settings that are currently unavailable”, this will allow us to change the blocked settings.  
  [![nfts-2](/images/article/2013/08/ntfs-2.png)](/images/article/2013/08/ntfs-2.png)  

6. Now, simply uncheck the box “Enable Quick Start (recommended)” and save the changes.  
  [![nfts-3](/images/article/2013/08/ntfs-3.png)](/images/article/2013/08/ntfs-3.png)  

That’s it, now there is no problem to mount NTFS partitions of Windows 8 on GNU / Linux.
