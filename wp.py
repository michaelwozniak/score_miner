import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import csv
import numpy
from tkinter import *
import requests
import random
from bs4 import BeautifulSoup


#connection to google forms/sheets
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json',scope)
client = gspread.authorize(creds)

#reference to google sheets
sheet = client.open('results1').sheet1
sheet2 = client.open('repo_turn').sheet1


val = sheet2.acell('A1').value
need_row_values = sheet.row_values(val)
results_after_run_google_forms = []

#I'm starting to converting values from google forms to our models

def changer_footballers(x):
    y = 3
    if (x == "0"): y = 0
    if (x == "1"): y = 1
    if (x == "2"): y = 2
    if (x == "3"): y = 3
    if (x == "4"): y = 4
    if (x == "5"): y = 5
    return y

temp_table=[1,2,3,4,5]
for x in temp_table:
    results_after_run_google_forms.append(changer_footballers(need_row_values[x]))

def changer_tactic(x):
    y = 5
    if (x == "Basic"): y = 5
    if (x == "Experimental"): y = 0
    return y

results_after_run_google_forms.append(changer_tactic(need_row_values[6]))

def changer_attitude_in_country(x):
    y = 2.5
    if (x == "+"): y = 5
    if (x == "-"): y = 0
    if (x == "="): y = 2.5
    return y

results_after_run_google_forms.append(changer_attitude_in_country(need_row_values[7]))

def changer_rotations(x):
    y = 2.5
    if (x == "0"): y = 0
    if (x == "1"): y = 5
    if (x == "2"): y = 5
    if (x == "3"): y = 0
    if (x == "4"): y = 0
    return y

results_after_run_google_forms.append(changer_rotations(need_row_values[8]))

results_after_run_google_forms.append(changer_attitude_in_country(need_row_values[9]))

results_after_run_google_forms_for_anothers = [3,3,3,3,3,5,2.5,5,2.5]

#odhasować bez tego brak iteracji w programie
#interation in google sheets, kinda stupid but working
# val1 = int(val) + 1
# sheet2.update_acell('A1', val1)

#model preparations
scale_footballers = [5, 4, 3, 2, 1]
footballers_temp = results_after_run_google_forms[0:5]
product = []
product = [a*b for a,b in zip(scale_footballers,footballers_temp)]
final_result_footballers_impact = (sum(product))/3

skills = pd.read_csv('datasets/skills.csv', sep=';')
skills["x"] = (skills["Points"]-(skills["Points"].min()))
skills["y"] = (skills["Points"].max()-(skills["Points"].min()))
skills["Points25"] = skills["x"]/skills["y"]*25

# scraper data from fifa ranking
res= requests.get("http://www.fctables.com/fifa-rankings/")
soup = BeautifulSoup(res.content,"lxml")
table = soup.find_all('table')[0]
df = pd.read_html(str(table))[0]
countries = df["Team"].tolist()
points = df["Points"].tolist()
ranking_after_scrap_and_craft = pd.DataFrame({'Team':countries})
ranking_after_scrap_and_craft['Points'] = pd.DataFrame({'Points':points})
ranking_after_scrap_and_craft["x_ranking"] = (ranking_after_scrap_and_craft["Points"]-(ranking_after_scrap_and_craft["Points"].min()))
ranking_after_scrap_and_craft["y_ranking"] = (ranking_after_scrap_and_craft["Points"].max()-(ranking_after_scrap_and_craft["Points"].min()))
ranking_after_scrap_and_craft["Points25_ranking"] = ranking_after_scrap_and_craft["x_ranking"]/ranking_after_scrap_and_craft["y_ranking"]*25
# fix after data scraper -> string Iceland 0-1 to string Iceland
ranking_after_scrap_and_craft.replace("Iceland 0-1", "Iceland", inplace=True)

#do zmiany!!!
country = "Poland"
country_of_choosen = country

# tu moze byc jakis blad --> crashuje sie wszystko?! sprawdzac
def mode_of_rating_for_one_country_choosen(country):
    after_merge = pd.merge(skills,ranking_after_scrap_and_craft, on="Team", how="inner")
    temp_after_merge = after_merge.query('Team == @country')
    sum_const = temp_after_merge["Points25"]+temp_after_merge["Points25_ranking"]
    if(country_of_choosen == country):
        rating_for_one_country = sum_const + final_result_footballers_impact + \
                                 results_after_run_google_forms[5] + \
                                 results_after_run_google_forms[6] + \
                                 results_after_run_google_forms[7] + \
                                 results_after_run_google_forms[8] + random.randint(0,5)
    else:
        rating_for_one_country = sum_const + final_result_footballers_impact + \
                                 results_after_run_google_forms_for_anothers[5] + \
                                 results_after_run_google_forms_for_anothers[6] + \
                                 results_after_run_google_forms_for_anothers[7] + \
                                 results_after_run_google_forms_for_anothers[8] + random.randint(0, 5)

    return float(rating_for_one_country)

groups = pd.DataFrame()
groups["A"]=["Russia","Saudi Arabia", "Egypt", "Uruguay"]
groups["B"]=["Portugal", "Spain", "Morocco", "Iran"]
groups["C"]=["France", "Australia", "Peru", "Denmark"]
groups["D"]=["Argentina", "Iceland", "Croatia", "Nigeria"]
groups["E"]=["Brazil", "Switzerland", "Costa Rica", "Serbia"]
groups["F"]=["Germany", "Mexico", "Sweden", "South Korea"]
groups["G"]=["Belgium", "Panama", "Tunisia", "England"]
groups["H"]=["Poland", "Senegal", "Colombia", "Japan"]

groupH = pd.DataFrame()
groupA = pd.DataFrame()
groupB = pd.DataFrame()
groupC = pd.DataFrame()
groupD = pd.DataFrame()
groupE = pd.DataFrame()
groupF = pd.DataFrame()
groupG = pd.DataFrame()

groupH["Team"] = groups["H"]
groupH["Points"] = 0
groupA["Team"] = groups["A"]
groupA["Points"] = 0
groupB["Team"] = groups["B"]
groupB["Points"] = 0
groupC["Team"] = groups["C"]
groupC["Points"] = 0
groupD["Team"] = groups["D"]
groupD["Points"] = 0
groupE["Team"] = groups["E"]
groupE["Points"] = 0
groupF["Team"] = groups["F"]
groupF["Points"] = 0
groupG["Team"] = groups["G"]
groupG["Points"] = 0


def compare(groups_df,number_of_group):
    a = 0
    b = 0
    c = 0
    d = 0
    if(mode_of_rating_for_one_country_choosen(groups_df[number_of_group][0])>mode_of_rating_for_one_country_choosen(
            groups_df[number_of_group][1])):
         if (random.random() < 0.25):
             a = 1+a
             b = 1+b
         else:
             a = a + 3
    else:
        if (random.random() < 0.25):
            a = 1 + a
            b = 1 + b
        else:
            b = b + 3
    if (mode_of_rating_for_one_country_choosen(groups_df[number_of_group][2]) > mode_of_rating_for_one_country_choosen(
            groups_df[number_of_group][3])):
        if (random.random() < 0.25):
            c = 1 + c
            d = 1 + d
        else:
            c = c + 3
    else:
        if (random.random() < 0.25):
            c = 1 + c
            d = 1 + d
        else:
            d = d + 3
    if (mode_of_rating_for_one_country_choosen(groups_df[number_of_group][0]) > mode_of_rating_for_one_country_choosen(
            groups_df[number_of_group][2])):
        if (random.random() < 0.25):
            a = 1 + a
            c = 1 + c
        else:
            a = a + 3
    else:
        if (random.random() < 0.25):
            a = 1 + a
            c = 1 + c
        else:
            c = c + 3
    if (mode_of_rating_for_one_country_choosen(groups_df[number_of_group][1]) > mode_of_rating_for_one_country_choosen(
            groups_df[number_of_group][3])):
        if (random.random() < 0.25):
            b = 1 + b
            d = 1 + d
        else:
            b = b + 3
    else:
        if (random.random() < 0.25):
            b = 1 + b
            d = 1 + d
        else:
            d = d + 3
    if (mode_of_rating_for_one_country_choosen(groups_df[number_of_group][0]) > mode_of_rating_for_one_country_choosen(
            groups_df[number_of_group][3])):
        if (random.random() < 0.25):
            a = 1 + a
            d = 1 + d
        else:
            a = a + 3
    else:
        if (random.random() < 0.25):
            a = 1 + a
            d = 1 + d
        else:
            d = d + 3
    if (mode_of_rating_for_one_country_choosen(groups_df[number_of_group][1]) > mode_of_rating_for_one_country_choosen(
            groups_df[number_of_group][2])):
        if (random.random() < 0.25):
            b = 1 + b
            c = 1 + c
        else:
            b = b + 3
    else:
        if (random.random() < 0.25):
            b = 1 + b
            c = 1 + c
        else:
            c = c + 3

    points = [a,b,c,d]

    if(number_of_group == "H"):
        groupH["Points"] = points
        group_temp = groupH

    if (number_of_group == "A"):
        groupA["Points"] = points
        group_temp = groupA

    if (number_of_group == "B"):
        groupB["Points"] = points
        group_temp = groupB

    if (number_of_group == "C"):
        groupC["Points"] = points
        group_temp = groupC

    if (number_of_group == "D"):
        groupD["Points"] = points
        group_temp = groupD

    if (number_of_group == "E"):
        groupE["Points"] = points
        group_temp = groupE

    if (number_of_group == "F"):
        groupF["Points"] = points
        group_temp = groupF

    if (number_of_group == "G"):
        groupG["Points"] = points
        group_temp = groupG


    group_temp = group_temp.sort_values(by = ['Points'], ascending=False)
    temp_update_group = group_temp["Team"].iloc[0]

    temp_temp_group2 = group_temp["Points"].iloc[1]
    temp_temp_group3 = group_temp["Points"].iloc[2]

    if(temp_temp_group2 == temp_temp_group3):
        if(random.random() > 0.5):
            temp_temp_group2 = group_temp["Team"].iloc[1]
        else:
            temp_temp_group2 = group_temp["Team"].iloc[2]

    temp_temp_group2 = group_temp["Team"].iloc[1]
    updated_group_rise_up = [temp_update_group, temp_temp_group2]
    return updated_group_rise_up

#structure of turnament
avance_after_group_stage_group_A = compare(groups,"A")
avance_after_group_stage_group_B = compare(groups,"B")
avance_after_group_stage_group_C = compare(groups,"C")
avance_after_group_stage_group_D = compare(groups,"D")
avance_after_group_stage_group_E = compare(groups,"E")
avance_after_group_stage_group_F = compare(groups,"F")
avance_after_group_stage_group_G = compare(groups,"G")
avance_after_group_stage_group_H = compare(groups,"H")

round_of_16_1_comp = [avance_after_group_stage_group_A[0], avance_after_group_stage_group_B[1]]
round_of_16_2_comp = [avance_after_group_stage_group_C[0], avance_after_group_stage_group_D[1]]
round_of_16_3_comp = [avance_after_group_stage_group_E[0], avance_after_group_stage_group_F[1]]
round_of_16_4_comp = [avance_after_group_stage_group_G[0], avance_after_group_stage_group_H[1]]
round_of_16_5_comp = [avance_after_group_stage_group_A[1], avance_after_group_stage_group_B[0]]
round_of_16_6_comp = [avance_after_group_stage_group_C[1], avance_after_group_stage_group_D[0]]
round_of_16_7_comp = [avance_after_group_stage_group_E[1], avance_after_group_stage_group_F[0]]
round_of_16_8_comp = [avance_after_group_stage_group_G[1], avance_after_group_stage_group_H[0]]

def compare_final_round(round_of_comp):
    a = mode_of_rating_for_one_country_choosen(round_of_comp[0])
    b = mode_of_rating_for_one_country_choosen(round_of_comp[1])
    if (a>b):
        avancer = round_of_comp[0]
        if (random.random()<0.1):
            avancer = round_of_comp[1]
    else:
        avancer = round_of_comp[1]
    return avancer

avancer_after_round_of_16_1 = compare_final_round(round_of_16_1_comp)
avancer_after_round_of_16_2 = compare_final_round(round_of_16_2_comp)
avancer_after_round_of_16_3 = compare_final_round(round_of_16_3_comp)
avancer_after_round_of_16_4 = compare_final_round(round_of_16_4_comp)
avancer_after_round_of_16_5 = compare_final_round(round_of_16_5_comp)
avancer_after_round_of_16_6 = compare_final_round(round_of_16_6_comp)
avancer_after_round_of_16_7 = compare_final_round(round_of_16_7_comp)
avancer_after_round_of_16_8 = compare_final_round(round_of_16_8_comp)

round_of_8_comp_1 = [avancer_after_round_of_16_1, avancer_after_round_of_16_2]
round_of_8_comp_2 = [avancer_after_round_of_16_3, avancer_after_round_of_16_4]
round_of_8_comp_3 = [avancer_after_round_of_16_5, avancer_after_round_of_16_6]
round_of_8_comp_4 = [avancer_after_round_of_16_7, avancer_after_round_of_16_8]

avancer_after_round_of_8_1 = compare_final_round(round_of_8_comp_1)
avancer_after_round_of_8_2 = compare_final_round(round_of_8_comp_2)
avancer_after_round_of_8_3 = compare_final_round(round_of_8_comp_3)
avancer_after_round_of_8_4 = compare_final_round(round_of_8_comp_4)

semifinal_comp_1 = [avancer_after_round_of_8_1, avancer_after_round_of_8_2]
semifinal_comp_2 = [avancer_after_round_of_8_3, avancer_after_round_of_8_4]

def loser (round_of_comp):
    a = mode_of_rating_for_one_country_choosen(round_of_comp[0])
    b = mode_of_rating_for_one_country_choosen(round_of_comp[1])
    if (a>b):
        loser = round_of_comp[1]
        if (random.random()<0.1):
            avancer = round_of_comp[0]
    else:
        loser = round_of_comp[0]
    return loser

avancer_to_final_after_first_semifinal = compare_final_round(semifinal_comp_1)
avancer_to_final_after_second_semifinal = compare_final_round(semifinal_comp_2)
loser_of_first_semifinal = loser(semifinal_comp_1)
loser_of_second_semifinal = loser(semifinal_comp_2)

final = [avancer_to_final_after_first_semifinal, avancer_to_final_after_second_semifinal]
third_place_play_off = [loser_of_first_semifinal, loser_of_second_semifinal]

first_place = compare_final_round(final)
second_place = loser(final)
third_place = compare_final_round(third_place_play_off)

#Bracket as a result of app
top = Tk()
top.title("World Cup 2018 Bracket")
top.resizable(False, False)
C = Canvas(top, bg="white", width=792, height=612)
image = PhotoImage(file = "media/bracket_template.png")
C.create_image(-1, -1, image = image, anchor = NW)
temp_bracket = first_place
s = StringVar(top, temp_bracket)


s = StringVar(top, avance_after_group_stage_group_A[0])
C.create_text(50,155,fill="black",font="Times 12  ", text=s.get())
s = StringVar(top, avance_after_group_stage_group_B[1])
C.create_text(50,235,fill="black",font="Times 12  ", text=s.get())
s = StringVar(top, avance_after_group_stage_group_C[0])
C.create_text(50,265,fill="black",font="Times 12  ", text=s.get())
s = StringVar(top, avance_after_group_stage_group_D[1])
C.create_text(50,350,fill="black",font="Times 12  ", text=s.get())
s = StringVar(top, avance_after_group_stage_group_E[0])
C.create_text(50,380,fill="black",font="Times 12  ", text=s.get())
s = StringVar(top, avance_after_group_stage_group_F[1])
C.create_text(50,465,fill="black",font="Times 12  ", text=s.get())
s = StringVar(top, avance_after_group_stage_group_G[0])
C.create_text(50,495,fill="black",font="Times 12  ", text=s.get())
s = StringVar(top, avance_after_group_stage_group_H[1])
C.create_text(50,575,fill="black",font="Times 12  ", text=s.get())
s = StringVar(top, avance_after_group_stage_group_B[0])
C.create_text(725,155,fill="black",font="Times 12  ", text=s.get())
s = StringVar(top, avance_after_group_stage_group_A[1])
C.create_text(725,235,fill="black",font="Times 12  ", text=s.get())
s = StringVar(top, avance_after_group_stage_group_D[0])
C.create_text(725,265,fill="black",font="Times 12  ", text=s.get())
s = StringVar(top, avance_after_group_stage_group_C[1])
C.create_text(725,350,fill="black",font="Times 12  ", text=s.get())
s = StringVar(top, avance_after_group_stage_group_F[0])
C.create_text(725,380,fill="black",font="Times 12  ", text=s.get())
s = StringVar(top, avance_after_group_stage_group_E[1])
C.create_text(725,465,fill="black",font="Times 12  ", text=s.get())
s = StringVar(top, avance_after_group_stage_group_H[0])
C.create_text(725,495,fill="black",font="Times 12  ", text=s.get())
s = StringVar(top, avance_after_group_stage_group_G[1])
C.create_text(725,575,fill="black",font="Times 12  ", text=s.get())

s = StringVar(top, avancer_after_round_of_16_1)
C.create_text(175,190,fill="black",font="Times 12  ", text=s.get())
s = StringVar(top, avancer_after_round_of_16_2)
C.create_text(175,305,fill="black",font="Times 12  ", text=s.get())
s = StringVar(top, avancer_after_round_of_16_3)
C.create_text(175,420,fill="black",font="Times 12  ", text=s.get())
s = StringVar(top, avancer_after_round_of_16_4)
C.create_text(175,535,fill="black",font="Times 12  ", text=s.get())
s = StringVar(top, avancer_after_round_of_16_5)
C.create_text(610,190,fill="black",font="Times 12  ", text=s.get())
s = StringVar(top, avancer_after_round_of_16_6)
C.create_text(610,305,fill="black",font="Times 12  ", text=s.get())
s = StringVar(top, avancer_after_round_of_16_7)
C.create_text(610,420,fill="black",font="Times 12  ", text=s.get())
s = StringVar(top, avancer_after_round_of_16_8)
C.create_text(610,535,fill="black",font="Times 12  ", text=s.get())

s = StringVar(top, avancer_after_round_of_8_1)
C.create_text(280,250,fill="black",font="Times 12  ", text=s.get())
s = StringVar(top, avancer_after_round_of_8_2)
C.create_text(280,475,fill="black",font="Times 12  ", text=s.get())
s = StringVar(top, avancer_after_round_of_8_3)
C.create_text(500,250,fill="black",font="Times 12  ", text=s.get())
s = StringVar(top, avancer_after_round_of_8_4)
C.create_text(500,475,fill="black",font="Times 12  ", text=s.get())

s = StringVar(top, avancer_to_final_after_first_semifinal)
C.create_text(380,340,fill="black",font="Times 12  ", text=s.get())
s = StringVar(top, avancer_to_final_after_second_semifinal)
C.create_text(380,390,fill="black",font="Times 12  ", text=s.get())
s = StringVar(top, loser_of_first_semifinal)
C.create_text(380,495,fill="black",font="Times 12  ", text=s.get())
s = StringVar(top, loser_of_second_semifinal)
C.create_text(380,560,fill="black",font="Times 12  ", text=s.get())

s = StringVar(top, third_place)
C.create_text(480,550,fill="black",font="Times 12  ", text=s.get())
s = StringVar(top, first_place)
C.create_text(390,280,fill="black",font="Times 12  ", text=s.get())
C.pack()
top.mainloop()