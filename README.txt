*********************************************** README ***********************************************



**************************************** What about the Bot ******************************************

This BotNet has been created by Thomas LeBasque.
It goes on Facebook to get public information about a known person (just the name).
After getting it the bot uses a TextToSpeach to read it.
To install the bot, please read the following...
Hope you will enjoy !!



*********************************** How to install the Bot *******************************************

*************

*********************************
Step #1: install python*********************************

Go to this website. Be sure you install the version 2.7
https://www.python.org/downloads/

*************

*********************************
Step #2: install dependencies***************************
Go to the install path (ex: E:\Pograms\Python\Python2.7). 
Open a command prompt here (Shift + right click, Open Powershell). 
Then run :
$ ./pip.exe install selenium
$ ./pip.exe install pillow
$ ./pip.exe install unidecode
***
*************

*********************************
Step #3: install driver*********************************
Look if there is geckodriver.exe in the file path.
If yes, go to Step#4

If not, follow the instructions bellow:
Go to on this website and unzip the .zip file into the current path:
https://github.com/mozilla/geckodriver/releases

*************

*********************************
Step #4: create firefox profile*************************
In the command prompt (not powershell), run :
$ firefox.exe -ProfileManager

Create a profile and save it into BotNet/profile
Open firefox. Go to 'Settings'.
Go to 'Advanced Settings'. Then on the research bar write 'notification'
Then in front of this section click on 'settings'.
At the bottom check the box 'Block all notifications'
Exit firefox.



*************

*********************************
 USE THE BOT *******************************************

Open the python code. If you have Notepad++ it would be better.
At the line 17, you will see "put your email here". So write your Facebook connected email.
Same at the line 22 with the password. Do not forget to put the quotes "".

It will require firstname and lastname of the person you want to get information about.
It will download the profile picture of the first found person and ask if it's the good one.
If not, it will find another one, re-download the profile picture and so on...
If yes it gets the infos and save them to ./output/output.txt.
Then, a TextToSpeach will transform the text into voice and we launch it to hear the voice.
Then save bot.py and exit. The bot is ready.

You can now use the bot by launching the launch_me.bat


****************************************** END README ************************************************
********************************** Made by Thomas ThomasLeBasque *************************************
