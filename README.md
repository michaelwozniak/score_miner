# score_miner
Project WNE UW

Score Miner is an app dedicated for football fans. 

There are two possible predictions: World Cup 2018 and Bundesliga season 2017/2018.

User has significant influence on World Cup results, Bundesliga prediction is based only on autumn round without user's impact.

Score Miner's algorithm assumes that user can suppose: 
  •	form of five top player;
  •	coach tendency to risk with tactic;
  •	number of rotations match by match;
  •	fan's attitude to future results;
  •	relationships between team members.
  
This assumptions are user variables in Score Miner's model (45%).

Part of model without user influence are:
  •	actual points from Ranking FIFA (25%);
  •	skills of players measured with FIFA 18 top 5 players each team (25%);
  •	random points (5%).
  
These variables and constants give 100 points. In the result of this, each team rating is in range (0 - 100) points.

In group stage algorithm assumes that with probability of 25% it is draw between particular two teams, 75% means that 3 points go to team with higher Score Miner's rating.
In knock-out stage assumptions are changes. With probability of 10%, random team wins, with 90% team which has higher rating.
In the second part of app (Bundesliga) user has two possibilities.

He can display:
  •	final table (after 34 gameweek);
  •	two tables: actual table without Score Miner's predictions and actual table with predictions after 17 gameweek.
  
There are calculated Home Team Goal Expectancies and Away Team Goal Expectancies (on the grounds of results from previous round. 
It is necessary to create matrix with Poisson Distribution for all possible results (from 0-0 to 3-3) for each match in spring round. 
The result with the highest probability go to final table.

The second element of Bundesliga part points out differences between real and predicted table.


We are using libraries like: 
tkinter
tkinter -> tk.messagebox
csv
pathlib
sys
os
pandas
webbrowser
gspread
oauth2client.service_account
request
random
bs4
matplotlib.pyplot
numpy
six
math

As you notice, we are using os library (os.system command) which requires well working python on your win (I mean you are able use this command in your cmd: python).

Description of all files:
main_menu.py -> please, start app using this file! Here you will find some info and hence you're going step by step

PLEASE! DO NOT START APP USING ANOTHER FILES! -> ONLY main_menu.py!

hub.py -> here, you are able to make a choice between WC predictions and BL predictions
wp.py -> here, we expect you are gonna fill in google forms file and name of your country
wp_core.py -> heart of WC predictor (algorith and visualisation)
bl.py -> menu of bundesliga predictor
bundesliga_part1.py -> it creates first table for BL predictor
bundesliga_part2.py -> it creates second table for BL predictor
bundesliga_part3.py -> it creates third table for BL predictor
media -> folder for images
datasets -> folder with databases saved in csv

