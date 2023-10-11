![chess_club](Images/chess_club.png)

# Project 4 Chess-Tournament Python (Trissi Mohammad Saleh) 

---------

***OpenClassrooms Develops a software program in Python Project 4 deliverable: 
chess tournament management application with database.***

_Tested on Windows 10 - Python version 3.11.3_

---------

## Table of Contents
1. [Project initialization](#id-section1)
    1. [Windows](#id-section1-1)
    2. [MacOS and Linux](#id-section1-2)
    3. [Generate a flake8 report](#id-section1-3)
2. [Menu Options](#id-section2)
    1. [Main Menu](#id-section2-1)
    2. [Reports](#id-section2-2)
3. [Display Examples](#id-section3)

<div id='id-section1'></div>

## 1. Project Initiation

<div id='id-section1-1'></div>

---------

#### i. Windows :

In Windows Powershell, navigate to the desired folder.

###### Project Recovery

        $ git clone https://github.com/SalehTrissi/P4-Chess-Tournament-Trissi-MohammadSaleh.git

##### Enable Virtual Environment
    $ cd P4-Chess-Tournament-Trissi-MohammadSaleh
    $ python -m venv env 
    $ env\scripts\activate
    # In cmd.exe
    venv\Scripts\activate.bat
    # In PowerShell
    venv\Scripts\Activate.ps1
   
###### Install the required packages
    $ pip install -r requirements.txt

###### Launch the program
    $ python main.py

<div id='id-section1-2'></div>

---------
#### ii. MacOS and Linux :
In the terminal, navigate to the desired folder.

###### Project Recovery
    $ git clone https://github.com/SalehTrissi/P4-Chess-Tournament-Trissi-MohammadSaleh.git

###### Enable Virtual Environment
    $ cd P4-Chess-Tournament-Trissi-MohammadSaleh
    $ python3 -m venv env 
    $ source env/bin/activate

###### Install the required packages
    $ pip install -r requirements.txt

###### Launch the program
    $ python3 main.py


<div id='id-section1-3'></div>

----------

#### iii. Generate a flake8 report

    $ flake8 --format=html --htmldir=flake8_report

**You will find the report in the _'flake8-report' folder.**

_Last exported report:_

![latest_report](Images/latest_report.png)

<div id='id-section2'></div>

----------

## 2. Menu options

----------

<div id='id-section2-1'></div>

#### i. Menu Principal
![main_menu](Images/main_menu.png)

<div id='id-section2-2'></div>

----------

#### ii. Reports Menu
![main_menu](Images/reports_menu.png)

<div id='id-section3'></div>

----------

## 3. display examples
#### Round Games:
![round](Images/round_example.png)

----------

#### Report players :
![player_report](Images/players_report.png)

----------

#### Round Report :
![round_report](Images/rounds_report.png)