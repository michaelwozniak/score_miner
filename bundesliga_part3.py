# ACTUAL BUNDESLIGA TABLE

import pandas as pd
import requests
from bs4 import BeautifulSoup
import matplotlib.pylab as plt
import numpy as np
import six

def bundes3():
    # scraping actual Bundesliga Table
    res = requests.get("https://www.bundesliga.com/en/stats/table/")
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
    all2017["Goals For"] = 0
    all2017["Goals Against"] = 0
    for i in range(18):
        text = all2017.loc[i, "Team"]
        text = text[:-4]
        all2017.loc[i, "Team"] = text
    for i in range(18):
        text = all2017.loc[i, "Goals"]
        words = text.split(":")
        all2017.loc[i, "Goals For"] = words[0]
        all2017.loc[i, "Goals Against"] = words[1]
    all2017.__delitem__("Goals")

    # changing Team names
    all2017.replace("FC Bayern München", "Bayern", inplace=True)
    all2017.replace("FC Schalke 04", "Schalke", inplace=True)
    all2017.replace("Borussia Dortmund", "Dortmund", inplace=True)
    all2017.replace("Bayer 04 Leverkusen", "Leverkusen", inplace=True)
    all2017.replace("Borussia Mönchengladbach", "BMG", inplace=True)
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

    # final order
    all2017["Position"] = np.arange(1,19)

    # choosing order of headers
    all2017 = all2017[["Position", "Team", "Matches", "Points", "Goals For", "Goals Against"]]

    # dataframe to png (sample from stackoverflow)
    def bundesliga_table_3(data, col_width=3.0, row_height=0.625, font_size=10,
                         header_color='green', row_colors=['#f1f1f2', 'w'], edge_color='w',
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

    bundesliga_table_3(all2017, header_columns=0, col_width=1.4)

    plt.savefig('media/bundes3.png')

