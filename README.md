# webd

A django project for web development society.

# Project Allotment Portal

A web portal for smooth allotment of project.

## Getting Started

Clone this repo and unzip it.

Install Python 3.6 or above in your system

Create the environment directory and go in it then enter command :- 
	python -m venv name

go to environment directory then to activate virtual environment run command :-
		name\Scripts\activate

Then run following commands :- 

pip install Django~=2.1.7 <br>
pip install Pillow <br>
pip install sendgrid <br>

Then while the virtual environment is still activated go to the repos directory directly to the place with manage.py file and run following commands:-

python manage.py makemigrations <br>
python manage.py migrate  <br>
python manage.py createsuperuser   fill details of super user <br>

Everything is set up now. You must clear the stray data from database first before using.

## Libraries required

Pillow

Send Grid


## super user Features:

You can go to 127.0.0.1:8000/admin and login using super user details and access and edit the entire database.

## owner Features

Also you can go to the directory which directly contains manage.py and run the following scripts by typing python script_name.py for there respective functions

verifyall.py    verify all users then group divide them also create teams based on leaders only leaders are added in each team not every member

groups.py divide into groups and create team leaders based teams only leaders are added in each team by it.

test.py create 40 users then does above tasks

proff.py create 10 professors with verified data

proff_allotment allots professors based on priority set by team leaders



			
## User’s Features:
    -Signup.
    -Login.
    -Different authority level admin can set authority levels of different users.
    -Users can fill in profile.
    -Admin and professor can verify and update verification status.
    -Then based on CPI students are divided and a team leaders are chosen. when respective script is run by owner
    -Team Leaders can send requests to different users of different groups.
    -Other members can send request for team leaders.
    -Then team is created on acceptance of requests.
    -After your team is created you can set professor priority list.
    -On running of script by owner professors are alloted to the teams.
    -Then Everything is complete team is set with mentor now you can discuss on project.
    
## Features Working on
    -Notification
    -Better styling
    -Lots of polishing
    -Chat box
    -Chat Bot
    -Other python Scripts for more automation of testing tasks
    -Scripts for better and smooth testing.

# General Number meanings


## authority

1-3 team member

4 team leader

5 prof

## data verified

0 default

1 under verification

2 details verified now set up team

3 >= team complete

4 >    Professor selected wait for verification

5 >=    Complete


## Priority

Lower the priority means more I want it.








