# TABLE WITH RESULTS FROM AUTUMN ROUND WITH PREDICTED RESULTS FROM SPRING ROUND GAMEWEEK BY GAMEWEEK

import pandas as pd
import requests
from bs4 import BeautifulSoup
import math
import datetime
import matplotlib.pylab as plt
import numpy as np
import six

def bundes2():
    # scraping Bundesliga Home Matches Table after 17 Gameweek
    res = requests.get("https://www.bundesliga.com/en/stats/table/?d=17&t=HEIM")
    soup = BeautifulSoup(res.content, "lxml")
    table = soup.find_all('table')[0]
    df = pd.read_html(str(table))[0]
    team = df["Unnamed: 4"].tolist()
    matches = df["Matches MD"].tolist()
    points = df["Points Pts"].tolist()
    goals = df["Goals"].tolist()
    home2017 = pd.DataFrame({'Team': team})
    home2017['Matches'] = pd.DataFrame({'matches': matches})
    home2017['Points'] = pd.DataFrame({'points': points})
    home2017['Goals'] = pd.DataFrame({'goals': goals})
    home2017["Goals for"] = 0
    home2017["Goals against"] = 0
    for i in range(18):
        text = home2017.loc[i, "Team"]
        text = text[:-4]
        home2017.loc[i, "Team"] = text
    for i in range(18):
        text = home2017.loc[i, "Goals"]
        words = text.split(":")
        home2017["Goals for"][i] = words[0]
        home2017["Goals against"][i] = words[1]
    home2017.__delitem__("Goals")

    # scraping Bundesliga Away Matches Table after 17 Gameweek
    res = requests.get("https://www.bundesliga.com/en/stats/table/?d=17&t=AUSWAERTS")
    soup = BeautifulSoup(res.content, "lxml")
    table = soup.find_all('table')[0]
    df = pd.read_html(str(table))[0]
    team = df["Unnamed: 4"].tolist()
    matches = df["Matches MD"].tolist()
    points = df["Points Pts"].tolist()
    goals = df["Goals"].tolist()
    away2017 = pd.DataFrame({'Team': team})
    away2017['Matches'] = pd.DataFrame({'matches': matches})
    away2017['Points'] = pd.DataFrame({'points': points})
    away2017['Goals'] = pd.DataFrame({'goals': goals})
    away2017["Goals for"] = 0
    away2017["Goals against"] = 0
    for i in range(18):
        text = away2017.loc[i, "Team"]
        text = text[:-4]
        away2017.loc[i, "Team"] = text
    for i in range(18):
        text = away2017.loc[i, "Goals"]
        words = text.split(":")
        away2017["Goals for"][i] = words[0]
        away2017["Goals against"][i] = words[1]
    away2017.__delitem__("Goals")

    # scraping Bundesliga Table after 17 Gameweek
    res = requests.get("https://www.bundesliga.com/en/stats/table/?d=17&t=BLITZTABELLE")
    soup = BeautifulSoup(res.content, "lxml")
    table = soup.find_all('table')[0]
    df = pd.read_html(str(table))[0]
    team = df["Unnamed: 4"].tolist()
    matches = df["Matches MD"].tolist()
    points = df["Points Pts"].tolist()
    goals = df["Goals"].tolist()
    all2017 = pd.DataFrame({'Team': team})
    all2017['Matches'] = pd.DataFrame({'matches': matches})
    all2017['Points'] = pd.DataFrame({'points': points})
    all2017['Goals'] = pd.DataFrame({'goals': goals})
    all2017["Goals for"] = 0
    all2017["Goals against"] = 0
    for i in range(18):
        text = all2017.loc[i, "Team"]
        text = text[:-4]
        all2017.loc[i, "Team"] = text
    for i in range(18):
        text = all2017.loc[i, "Goals"]
        words = text.split(":")
        all2017["Goals for"][i] = words[0]
        all2017["Goals against"][i] = words[1]
    all2017.__delitem__("Goals")

    # changing Team names
    all2017.replace("FC Bayern München", "Bayern", inplace=True)
    all2017.replace("FC Schalke 04", "Schalke", inplace=True)
    all2017.replace("Borussia Dortmund", "Dortmund", inplace=True)
    all2017.replace("Bayer 04 Leverkusen", "Leverkusen", inplace=True)
    all2017.replace("Borussia Mönchengladbach", "B. Monchengladbach", inplace=True)
    all2017.replace("TSG 1899 Hoffenheim", "Hoffenheim", inplace=True)
    all2017.replace("Eintracht Frankfurt", "Eintracht", inplace=True)
    all2017.replace("FC Augsburg", "Augsburg", inplace=True)
    all2017.replace("Hertha BSC", "Hertha", inplace=True)
    all2017.replace("Hannover 96", "Hannover", inplace=True)
    all2017.replace("VfL Wolfsburg", "Wolfsburg", inplace=True)
    all2017.replace("Sport-Club Freiburg", "Freiburg", inplace=True)
    all2017.replace("VfB Stuttgart", "Stuttgart", inplace=True)
    all2017.replace("1. FSV Mainz 05", "Mainz", inplace=True)
    all2017.replace("SV Werder Bremen", "Werder", inplace=True)
    all2017.replace("Hamburger SV", "Hamburger", inplace=True)
    all2017.replace("1. FC Köln", "FC Koln", inplace=True)

    home2017.replace("FC Bayern München", "Bayern", inplace=True)
    home2017.replace("FC Schalke 04", "Schalke", inplace=True)
    home2017.replace("Borussia Dortmund", "Dortmund", inplace=True)
    home2017.replace("Bayer 04 Leverkusen", "Leverkusen", inplace=True)
    home2017.replace("Borussia Mönchengladbach", "B. Monchengladbach", inplace=True)
    home2017.replace("TSG 1899 Hoffenheim", "Hoffenheim", inplace=True)
    home2017.replace("Eintracht Frankfurt", "Eintracht", inplace=True)
    home2017.replace("FC Augsburg", "Augsburg", inplace=True)
    home2017.replace("Hertha BSC", "Hertha", inplace=True)
    home2017.replace("Hannover 96", "Hannover", inplace=True)
    home2017.replace("VfL Wolfsburg", "Wolfsburg", inplace=True)
    home2017.replace("Sport-Club Freiburg", "Freiburg", inplace=True)
    home2017.replace("VfB Stuttgart", "Stuttgart", inplace=True)
    home2017.replace("1. FSV Mainz 05", "Mainz", inplace=True)
    home2017.replace("SV Werder Bremen", "Werder", inplace=True)
    home2017.replace("Hamburger SV", "Hamburger", inplace=True)
    home2017.replace("1. FC Köln", "FC Koln", inplace=True)

    away2017.replace("FC Bayern München", "Bayern", inplace=True)
    away2017.replace("FC Schalke 04", "Schalke", inplace=True)
    away2017.replace("Borussia Dortmund", "Dortmund", inplace=True)
    away2017.replace("Bayer 04 Leverkusen", "Leverkusen", inplace=True)
    away2017.replace("Borussia Mönchengladbach", "B. Monchengladbach", inplace=True)
    away2017.replace("TSG 1899 Hoffenheim", "Hoffenheim", inplace=True)
    away2017.replace("Eintracht Frankfurt", "Eintracht", inplace=True)
    away2017.replace("FC Augsburg", "Augsburg", inplace=True)
    away2017.replace("Hertha BSC", "Hertha", inplace=True)
    away2017.replace("Hannover 96", "Hannover", inplace=True)
    away2017.replace("VfL Wolfsburg", "Wolfsburg", inplace=True)
    away2017.replace("Sport-Club Freiburg", "Freiburg", inplace=True)
    away2017.replace("VfB Stuttgart", "Stuttgart", inplace=True)
    away2017.replace("1. FSV Mainz 05", "Mainz", inplace=True)
    away2017.replace("SV Werder Bremen", "Werder", inplace=True)
    away2017.replace("Hamburger SV", "Hamburger", inplace=True)
    away2017.replace("1. FC Köln", "FC Koln", inplace=True)

    # read all matches in 2018 from season 17/18 with dates
    matches_with_dates = pd.read_csv('datasets/matches_with_dates.csv', sep=';')

    # datetime format for dates
    matches_with_dates['Date'] = pd.to_datetime(matches_with_dates['Date'], infer_datetime_format=True)
    matches_with_dates['Current_date'] = datetime.date.today()
    matches_with_dates['Date'] = matches_with_dates['Date'].astype('datetime64[ns]')
    matches_with_dates['Current_date'] = matches_with_dates['Current_date'].astype('datetime64[ns]')

    # choosing actual dates for Gameweeks
    actual_matches = matches_with_dates.loc[(matches_with_dates["Date"]) <= (matches_with_dates["Current_date"])]


    # changing columns names
    home2017.columns.values[1] = "Home Games Played"
    home2017.columns.values[3] = "Home Goals For"
    home2017.columns.values[4] = "Home Goals Against"
    away2017.columns.values[1] = "Away Games Played"
    away2017.columns.values[3] = "Away Goals For"
    away2017.columns.values[4] = "Away Goals Against"

    # merging home2017 and away2017
    merge_home_away = pd.merge(home2017, away2017, on="Team", how="inner")

    bundes = merge_home_away[["Team", "Home Games Played", "Home Goals For", "Home Goals Against", "Away Games Played", "Away Goals For", "Away Goals Against"]]

    bundes["Home Average Goals For"] = bundes["Home Goals For"] / bundes["Home Games Played"]
    bundes["Home Average Goals Against"] = bundes["Home Goals Against"] / bundes["Home Games Played"]
    bundes["Away Average Goals For"] = bundes["Away Goals For"] / bundes["Away Games Played"]
    bundes["Away Average Goals Against"] = bundes["Away Goals Against"] / bundes["Away Games Played"]

    bundes["Home Total Average Goals For"] = bundes["Home Goals For"].sum() / bundes["Home Games Played"].sum()
    bundes["Home Total Average Goals Against"] = bundes["Home Goals Against"].sum() / bundes["Home Games Played"].sum()
    bundes["Away Total Average Goals For"] = bundes["Away Goals For"].sum() / bundes["Away Games Played"].sum()
    bundes["Away Total Average Goals Against"] = bundes["Away Goals Against"].sum() / bundes["Away Games Played"].sum()

    bundes["Home Attacking Strength"] = bundes["Home Average Goals For"] / bundes["Home Total Average Goals For"]
    bundes["Home Defensive Strength"] = bundes["Home Average Goals Against"] / bundes["Home Total Average Goals Against"]
    bundes["Away Attacking Strength"] = bundes["Away Average Goals For"] / bundes["Away Total Average Goals For"]
    bundes["Away Defensive Strength"] = bundes["Away Average Goals Against"] / bundes["Away Total Average Goals Against"]

    home_score = bundes[["Team", "Home Attacking Strength", "Home Defensive Strength"]]
    away_score = bundes[["Team", "Away Attacking Strength", "Away Defensive Strength"]]

    # merging tables
    home_score.columns.values[0] = "HomeTeam"
    after_merge_home_score = pd.merge(home_score, actual_matches, on="HomeTeam", how="inner")
    away_score.columns.values[0] = "AwayTeam"
    after_merge_home_score_and_away_score = pd.merge(after_merge_home_score, away_score, on="AwayTeam", how="inner")

    total_goals = bundes[["Team", "Home Total Average Goals For", "Away Total Average Goals For"]]
    total_goals.columns.values[0] = "HomeTeam"
    whole_table = pd.merge(after_merge_home_score_and_away_score, total_goals, on="HomeTeam", how="inner")
    whole_table["Home Team Goal Expectancy"] = whole_table["Home Attacking Strength"] * whole_table[
        "Away Defensive Strength"] * whole_table["Home Total Average Goals For"]
    whole_table["Away Team Goal Expectancy"] = whole_table["Away Attacking Strength"] * whole_table[
        "Home Defensive Strength"] * whole_table["Away Total Average Goals For"]


    # factorial (silnia)
    def factorial(n):
        if (n > 1):
            return n * factorial(n - 1)
        else:
            return 1


    from math import e


    # Poisson Distribution
    def p_d(x, y, e=e):
        p = ((y ** x) * ((math.e) ** (-y))) / (factorial(x))
        return p

    # table with probabilities of results (from 0-0 to 3-3) for two particular teams which returns the most probable result
    def table_probabilities(a, b):
        L = [[p_d(0, a) * p_d(0, b), p_d(1, a) * p_d(0, b), p_d(2, a) * p_d(0, b), p_d(3, a) * p_d(0, b)],
             [p_d(0, a) * p_d(1, b), p_d(1, a) * p_d(1, b), p_d(2, a) * p_d(1, b), p_d(3, a) * p_d(1, b)],
             [p_d(0, a) * p_d(2, b), p_d(1, a) * p_d(2, b), p_d(2, a) * p_d(2, b), p_d(3, a) * p_d(2, b)],
             [p_d(0, a) * p_d(3, b), p_d(1, a) * p_d(3, b), p_d(2, a) * p_d(3, b), p_d(3, a) * p_d(3, b)]]
        LL = np.asmatrix(L)
        i, j = np.where(LL == np.amax(LL))
        k = i[0]
        l = j[0]
        indexes = [l, k]
        return indexes


    # new table with goal expectancy
    new_table = whole_table[["HomeTeam", "AwayTeam", "Home Team Goal Expectancy", "Away Team Goal Expectancy"]]
    new_table["goalA"] = 0
    new_table["goalB"] = 0

    # choosing only matches after particular Gameweeks
    for z in range(actual_matches["HomeTeam"].count()):
        score = table_probabilities(new_table.loc[z, 'Home Team Goal Expectancy'],
                                    new_table.loc[z, 'Away Team Goal Expectancy'])
        new_table.loc[z, "goalA"] = score[0]
        new_table.loc[z, "goalB"] = score[1]

    new_table["pointsA"] = 0
    new_table["pointsB"] = 0

    # awarding points to teams after Poisson Distribution
    for z in range(actual_matches["HomeTeam"].count()):
        a = new_table.loc[z, "goalA"]
        b = new_table.loc[z, "goalB"]
        if (a > b):
            new_table.loc[z, "pointsA"] = 3
        elif (a < b):
            new_table.loc[z, "pointsB"] = 3
        else:
            new_table.loc[z, "pointsA"] = 1
            new_table.loc[z, "pointsB"] = 1

    # new table
    spring_table = bundes[["Team"]]
    spring_table["points"] = 0
    spring_table["goals_for"] = 0
    spring_table["goals_against"] = 0

    # summing points and goals in table
    for z in range(18):
        team = spring_table.loc[z, "Team"]
        for x in range(actual_matches["HomeTeam"].count()):
            if (new_table.loc[x, "HomeTeam"] == team):
                spring_table.loc[z, "points"] = float(new_table.loc[x, "pointsA"]) + float(spring_table.loc[z, "points"])
                spring_table.loc[z, "goals_for"] = float(new_table.loc[x, "goalA"]) + float(
                    spring_table.loc[z, "goals_for"])
                spring_table.loc[z, "goals_against"] = float(new_table.loc[x, "goalB"]) + float(
                    spring_table.loc[z, "goals_against"])
            if (new_table.loc[x, "AwayTeam"] == team):
                spring_table.loc[z, "points"] = float(new_table.loc[x, "pointsB"]) + float(spring_table.loc[z, "points"])
                spring_table.loc[z, "goals_for"] = float(new_table.loc[x, "goalB"]) + float(
                    spring_table.loc[z, "goals_for"])
                spring_table.loc[z, "goals_against"] = float(new_table.loc[x, "goalA"]) + float(
                    spring_table.loc[z, "goals_against"])

    # sorting by points
    spring_table = spring_table.sort_values(by=['points'], ascending=False)


    autumn_table = all2017[["Team", "Points", "Goals for", "Goals against"]]

    # sorting by Teams
    spring_table = spring_table.sort_values(by=['Team'], ascending=False)
    autumn_table = autumn_table.sort_values(by=['Team'], ascending=False)

    # changing headers
    spring_table.columns.values[1] = "Points"
    spring_table.columns.values[2] = "Goals for"
    spring_table.columns.values[3] = "Goals against"

    autumn_table.columns.values[1] = "Points"
    autumn_table.columns.values[2] = "Goals for"
    autumn_table.columns.values[3] = "Goals against"

    # merging autumn_table with predicted spring_table
    predicted_table_season_17_18 = pd.merge(spring_table, autumn_table, on="Team", how="inner")

    # summing points and goals
    predicted_table_season_17_18["Points"] = predicted_table_season_17_18["Points_x"] + predicted_table_season_17_18["Points_y"]
    predicted_table_season_17_18["Goals For"] = predicted_table_season_17_18["Goals for_x"] + predicted_table_season_17_18["Goals for_y"]
    predicted_table_season_17_18["Goals Against"] = predicted_table_season_17_18["Goals against_x"] + predicted_table_season_17_18["Goals against_y"]

    # final table with interesting values
    final_predicted_table = predicted_table_season_17_18[["Team", "Points", "Goals For", "Goals Against"]]

    # sorting by points
    final_predicted_table = final_predicted_table.sort_values(by=['Points'], ascending=False)

    final_predicted_table.replace("B. Monchengladbach", "BMG", inplace=True)

    # quantity of matches
    final_predicted_table["Matches"] = actual_matches["HomeTeam"].count()/9 + 17

    # final order
    final_predicted_table["Position"] = np.arange(1,19)

    # order of headers
    final_predicted_table = final_predicted_table[["Position", "Team", "Matches", "Points", "Goals For", "Goals Against"]]
    final_predicted_table["Matches"] = pd.to_numeric(final_predicted_table["Matches"], downcast='signed')
    final_predicted_table["Points"] = pd.to_numeric(final_predicted_table["Points"], downcast='signed')
    final_predicted_table["Goals For"] = pd.to_numeric(final_predicted_table["Goals For"], downcast='signed')
    final_predicted_table["Goals Against"] = pd.to_numeric(final_predicted_table["Goals Against"], downcast='signed')


    # dataframe to png (sample from stackoverflow)
    def bundesliga_table_2(data, col_width=3.0, row_height=0.625, font_size=10,
                         header_color='#40466e', row_colors=['#f1f1f2', 'w'], edge_color='w',
                         bbox=[0, 0, 1, 1], header_columns=0,
                         ax=None, **kwargs):
        if ax is None:
            size = (np.array(data.shape[::-2]) + np.array([0, 0])) * np.array([col_width, row_height])
            fig, ax = plt.subplots(figsize=size)
            ax.axis('off')

        mpl_table = ax.table(cellText=data.values, bbox=bbox, colLabels=data.columns, **kwargs)

        mpl_table.auto_set_font_size(False)
        mpl_table.set_fontsize(font_size)

        for k, cell in  six.iteritems(mpl_table._cells):
            cell.set_edgecolor(edge_color)
            if k[0] == 0 or k[1] < header_columns:
                cell.set_text_props(weight='bold', color='w')
                cell.set_facecolor(header_color)
            else:
                cell.set_facecolor(row_colors[k[0]%len(row_colors) ])
        return ax

    bundesliga_table_2(final_predicted_table, header_columns=0, col_width=1.4)

    plt.savefig('media/bundes2.png')


