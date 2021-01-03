# Client-TransactionManagment

# Demo : https://ctmanagement.herokuapp.com/

# Requirements
Python 3.8.0

# Setup Project 
At first download or clone this git repository using git clone https://github.com/GreenFoxCoders/client-transaction-management command.

Then,
run: python -m venv env 
if you don't have venv installed, use ;python -m pip install venv' to install pip(windows, in other os, you don't need 'python -m')

Then 
run: env/Scripts/Activate.ps1 
if you're using powershell, Activate.bat if you're using command prompt,
or activate in othercases. 
Help in Getting Venv running: 
windows: (smaller, shortcut) https://youtu.be/XmM0UpNkvnE
windows: https://www.youtube.com/watch?v=APOPm01BVrk 
mac/linux: https://www.youtube.com/watch?v=Kg1Yvry_Ydk

Then, 
run: pip install -r requirements.txt
Then, nevigate to the ctmanagement folder where manage.py file exists.

Then,
run: python manage.py runserver 

Finally, you'll see something similar to this:

"Performing system checks...

System check identified no issues (0 silenced).
January 03, 2021 - 18:57:19
Django version 3.1.4, using settings 'ctmanagement.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK."

Open http://127.0.0.1:8000 in your browser.

To stop the server, just press CTRL+C in your command shell.



