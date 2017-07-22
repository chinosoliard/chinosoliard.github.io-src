Title: Synchronizing files with UNISON on Fedora
Date: 2013-05-22 14:00
Category: Fedora
Tags: Fedora, GNU/Linux, Local, maintenance, SSH, Sync, Synchronization, UNISON
Lang: en
Slug: synchronizing-files-unison-fedora 
Summary: <img alt="unison-logo" src="/images/article/2013/05/unison-logo.png" class="alignright">I stored most of my files on my desktop computer, other files were saved on my notebook, it had less space, and others automatically synchronized with Dropbox, It ended when I change the notebook, and now, the new notebook has more space than the desktop computer, but storing everything in the notebook is dangerous and unsafe, so I just want to make the data in the 2 computers.</br></br>There are different alternatives for automatic synchronization (most of them are pay), in my case, I decided to use [UNISON](http://www.cis.upenn.edu/~bcpierce/unison/), a multiplatform application that allows the synchronization between two host, or also between two local directories.</br></br>Synchronize means “Make matching in time two or more movements or phenomena.”, therefore, that is exactly what Unison makes, the changes are propagated bidirectionally, it mean, files that are on the host “a” and are not in the host “b”, are copied, and vice versa; Also, it compares file dates to detect, obviously, which is more recent.</br></br>Unison, as mentioned above, allows synchronization between local directories, and between different hosts using [SSH (Secure Shell)](http://en.wikipedia.org/wiki/Secure_Shell), [RSH (Remote Shell)](http://en.wikipedia.org/wiki/Rsh) and [TCP (por Socket)](http://en.wikipedia.org/wiki/Socket_de_Internet). As SSH is the safest method, is the one I chose to operate , and we will use in this simple guide.  

1. **Installing UNISON**  
  Unison is in Fedora repositories, so, installing it is just using the following command:  
  `su -c ‘yum install unison’`  

2. **Creating Sinchronization profiles**  
  Unison works with profiles, which are configured to specify which directories are going to be synchronized.  
    1. We execute Unison, now I can’t remember if the first time it automatically ran the profile wizard to add a profile, if not, click the “Add” button to start the creation wizard.  

    2. On the first screen, which is just an introduction, click on “Forward”.  
    [![unison-1](/images/article/2013/05/unison-1.png)](/images/article/2013/05/unison-1.png)  

    3. Then, it ask us to complete the profile name and description. We complete and give next.  
    [![unison-2](/images/article/2013/05/unison-2.png)](/images/article/2013/05/unison-2.png)  

    4. Then, it asks us to select the connection type, where we can choose Local, SSH, RSH and TCP.  

        * **Local Sinchronization profiles**  
            1. We follow the steps above, now select “Local” from the list of connection types and give “forward”.  
            [![unison-3](/images/article/2013/05/unison-3.png)](/images/article/2013/05/unison-3.png)  

            2. Below, we declare the directories involved in the synchronization, when complete, give “Forward”.  
            [![unison-4](/images/article/2013/05/unison-4.png)](/images/article/2013/05/unison-4.png)  

            3. In my case, I’m going to synchronize directories that are on NTFS partitions, therefore, I check the box to set the profile to work without using the GNU/Linux permissions.  
            [![unison-5](/images/article/2013/05/unison-5.png)](/images/article/2013/05/unison-5.png)  

            4. Finally, Unison report that it finished configuring the profile, and we press “Apply” to create it.  
            [![unison-6](/images/article/2013/05/unison-6.png)](/images/article/2013/05/unison-6.png)  
  

        * **Remote SSH Synchronization Profile**  
            1. We follow the steps above, now select “SSH” from the list of connection types, the contents of the window will be extended and now we be asked to introduce the host, which can be the name or IP address of the computer to which we want to connect, and the username that we will use to log into the host.  
               Also, we can activate a checkbox to let Unison compress the files to be sent, as you can read at the window, is good for slow connections, but make fast connections more slower.  
               After setting this, give next.  
            [![unison-7](/images/article/2013/05/unison-7.png)](/images/article/2013/05/unison-7.png)  

            2. Then, we set the directories that we will synchronize. We can select the Local directory, the remote directory should be written, so it is necessary to know first the name of the directory. You can confirm this by doing a SSH connection with a console.  
             After that, click on “Forward”.  
            [![unison-8](/images/article/2013/05/unison-8.png)](/images/article/2013/05/unison-8.png)  

            3. As in the previous example, where we done a Local Synchronization, we can set the profile to work with NTFS or FAT, or rather, to exclude the treatment of file permissions that GNU / Linux uses. In my case, I use NTFS partitions in sync, so I active the checkbox.  
            [![unison-9](/images/article/2013/05/unison-9.png)](/images/article/2013/05/unison-9.png)  

            4. Then just press “Apply” and it’s ready, we ended setting the profile.  
            [![unison-10](/images/article/2013/05/unison-10.png)](/images/article/2013/05/unison-10.png)  

3. **Performing a Synchronization.**  
    1. Execute a synchronization profile, selecting it from the list and clicking on “Open”.  
    [![unison-11](/images/article/2013/05/unison-11.png)](/images/article/2013/05/unison-11.png)  
      *When opening one of the profiles created to synchronize via SSHwe will be asked for a password to login.*  
      [![unison-12](/images/article/2013/05/unison-12.png)](/images/article/2013/05/unison-12.png)  

    2. When we did the first synchronization, it shows a window like this, which explains that there are no historical records of synchronizations, and that this is because, or synchronizations have not been performed yet, or we’ve updated the version of Unison and this one does not recognize the historical files; Wherefore, Unison assumes that the historical record is completely empty.  
    [![unison-13](/images/article/2013/05/unison-13.png)](/images/article/2013/05/unison-13.png)  
    *The first time you perform synchronizations, this process takes too long.*  

    3. After the comparison, Unison generates a list, which automatically adjusted the changes to make, which we can modify.  
      We review the shifts to be performed, we can skip changes (which ignores the row, it make no changes), and choose the replacement and copying in both directions.  
    [![unison-14](/images/article/2013/05/unison-14.png)](/images/article/2013/05/unison-14.png)  

    4. Once we checked the changes to make, press the “Go” button, and Unison start syncing.  

    5. After finishing copying files, a window will appear reporting that the synchronization finished, and a short summary, which we can extend.  
    [![unison-15](/images/article/2013/05/unison-15.png)](/images/article/2013/05/unison-15.png)  


This is the simply way to use Unison; If a profile have a first run done, the point 3.2 end faster.  
An important point to note is that Unison must be installed on both devices, if synchronization is performed remotely.    
n this guide we work with Unison with graphical environment, but also can be used with a console (I am considering using Unison from the command line  with “cron” for automating synchronizations and backups).  
  

I hope it has served.  
  

regards
