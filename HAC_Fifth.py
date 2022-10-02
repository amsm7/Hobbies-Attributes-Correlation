import random
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mtb
import numpy as nmp


def create_data_frame():
    pzl = list()
    pnt = list()
    ptc = [None] * 1000
    crt = [None] * 1000
    twh = [None] * 1000
    tr = [None] * 1000
    i = 0

    for val in range(1, 1001):
        pzl.append(random.randint(0, 9))
        pnt.append(random.randint(0, 9))

    my_dict = {'Puzzle(Hours)': pzl, 'Patience': ptc, 'Painting(Hours)': pnt, 'Creativity': crt,
               'Total weekly hours': twh, 'Total Rating(1-5)': tr}

    df = pd.DataFrame(my_dict)
    df.to_csv('New_Dataframe.csv', index=False)

    corr_data = pd.read_csv('New_Dataframe.csv')

    return corr_data


# Read csv file from directory.


def fill_data_frame():
    pass


# Check Creativity affects of Painting.
def check_creativity(corr_data):
    for val in corr_data.index:

        if corr_data.loc[val, "Painting(Hours)"] >= 10:
            corr_data.loc[val, "Creativity"] = 5

        elif 9.5 >= corr_data.loc[val, "Painting(Hours)"] >= 7.5:
            corr_data.loc[val, "Creativity"] = 4

        elif 7 >= corr_data.loc[val, "Painting(Hours)"] >= 5:
            corr_data.loc[val, "Creativity"] = 3

        else:
            corr_data.loc[val, "Creativity"] = 2

    return corr_data


# Check Patience affects of doing Puzzle.
def check_patience(corr_data):
    for val in corr_data.index:

        if corr_data.loc[val, "Puzzle(Hours)"] >= 10:
            corr_data.loc[val, "Patience"] = 5

        elif 9.5 >= corr_data.loc[val, "Puzzle(Hours)"] >= 7.5:
            corr_data.loc[val, "Patience"] = 4

        elif 7 >= corr_data.loc[val, "Puzzle(Hours)"] >= 5:
            corr_data.loc[val, "Patience"] = 3

        else:
            corr_data.loc[val, "Patience"] = 2

    return corr_data


# Print the updated Data Frame.
def print_data_frame(upd_data):
    print("\nPrinting table contents:\n")
    print(upd_data.to_string())


# Rating based on the number of hours of activity.
def check_total_rating(corr_data):
    for val in corr_data.index:
        total = (corr_data.loc[val, "Puzzle(Hours)"] + corr_data.loc[val, "Painting(Hours)"])
        corr_data.loc[val, "Total weekly hours"] = total

        if total >= 10:
            corr_data.loc[val, "Total Rating(1-5)"] = 5

        elif 9.5 >= total >= 8:
            corr_data.loc[val, "Total Rating(1-5)"] = 4

        elif total <= 7.5 and total >= 6:
            corr_data.loc[val, "Total Rating(1-5)"] = 3

        elif total <= 5.5 and total >= 4:
            corr_data.loc[val, "Total Rating(1-5)"] = 2

        else:
            corr_data.loc[val, "Total Rating(1-5)"] = 1

    return corr_data


"""

sort_bad_data():

ideas: 
1. val in ... != type(string)
2. val in ... != type(int)

...


"""


# Checking correlation between the hours of each activity and the effect on certain attributes.
def check_corr(corr_data):
    print(f"\nChecking correlation: \n\n{corr_data.corr().to_string()}")


def plot_data(upd_data):
    upd_data.plot(x='Painting(Hours)', y='Creativity')
    plt.show()


# sort_bad_data()

# Main Function.
def main(new_data):
    check_creativity(new_data)
    check_patience(new_data)
    upd_data = check_total_rating(new_data)
    print_data_frame(upd_data)
    check_corr(new_data)
    plot_data(upd_data)


new_data = create_data_frame()
main(new_data)
