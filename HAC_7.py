## All rights reserved - Amir Sillam - October 2022 ##

import random
import pandas as pd
import matplotlib.pyplot as plt
import termcolor
from termcolor import colored

# import matplotlib as mtb
# import numpy as np


"""
sort_bad_data():
ideas: 
1. val in ... != type(string)
2. val in ... != type(int)


def ratio_print(): 
    pass

def ratio_test(houston, new_list):
    new_list.append(houston)
"""


# Checking correlation between all indexes.
def check_corr(data_frame):
    correlated_data = data_frame.corr()
    print("---------------------------------------------------")
    print("Showing correlation between the entire data frame.")
    print("---------------------------------------------------\n")
    return colored(f"{correlated_data.to_string()}", 'blue', attrs=["bold"])


# Checking correlation between puzzle and patience.
def puzzle_patience_corr(data_frame):
    new_corr = data_frame['Puzzle(Hours)'].corr(data_frame['Patience'])
    print("-------------------------------------------------------------- ")
    print("Correlation between doing Puzzle and contribution to Patience.")
    print("-------------------------------------------------------------- \n")
    print(colored(data_frame[['Puzzle(Hours)', 'Patience']].corr(), 'blue'))
    print(colored(f"\n** full length: {new_corr}", 'blue'))
    return ""


# Checking correlation between painting and creativity.
def painting_creativity_corr(data_frame):
    new_corr = data_frame['Painting(Hours)'].corr(data_frame['Creativity'])

    print("------------------------------------------------------------ ")
    print("Correlation between Painting and contribution to Creativity.")
    print("------------------------------------------------------------ \n")
    print(colored(data_frame[['Painting(Hours)', 'Creativity']].corr(),
          'blue'))
    print(colored(f"\n** full length: {new_corr}", 'blue'))
    return ""


def plot_puzzle_data(upd_data):
    upd_data.plot(x='Puzzle(Hours)', y='Patience')
    print("-------------------------------------- ")
    print("The plot of doing Puzzle and Patience.")
    print("-------------------------------------- \n")
    plt.show()


def plot_painting_data(upd_data):
    upd_data.plot(x='Painting(Hours)', y='Creativity')

    print("------------------------------------ ")
    print("The plot of Painting and Creativity.")
    print("------------------------------------ \n")
    plt.show()

def print_data_frame(data_frame):
    print(data_frame.to_string())


# Check menu options.
def menu_options(menu_option, data_frame):
    if menu_option == '1':
        print_data_frame(data_frame)

    elif menu_option == '2':
        print(check_corr(data_frame))

    elif menu_option == '3':
        puzzle_patience_corr(data_frame)

    elif menu_option == '4':
        painting_creativity_corr(data_frame)

    elif menu_option == '5':
        plot_puzzle_data(data_frame)

    elif menu_option == '6':
        plot_painting_data(data_frame)

    else:
        exit("EXIT program.")


# Print menu message.
def menu_print():
    input_options = ['1', '2', '3', '4', '5', '6', '7']

    print("Please Choose an option from the menu below:")
    print(colored("------------------------------------------------------- \n"
                  "| 1.Show Collected Data frame.                        |\n"
                  "| 2.Show all Data frame correlation.                  | \n"
                  "| 3.Show correlation between Puzzle and Patience      | \n"
                  "| 4.Show correlation between Painting and Creativity. | \n"
                  "| 5.Show plot of Puzzle.                              | \n"
                  "| 6.Show plot of Painting.                            |\n"
                  "| 7.End program.                                      |\n"
                  "-------------------------------------------------------", 'green'))

    menu_option = input(colored("\nYour input: ",
                                'green'))
    count = 1
    while menu_option not in input_options:
        if count > 5:
            print(f"You have tried {count - 1} times, that's the limit.")
            exit("Try again next time, Thank you.")
        count += 1
        menu_option = input(colored("You must insert only valid numbers,try again please:", 'green'))
    return menu_option


# Print the app starting message.
def opening_message():
    print("\nDATADATADATADATADATADATADATADATADATADATADATADATADATADATADATA")
    print(colored("|                                                          |", 'green'))
    print(colored("|                This is my new Project !                  |", 'green'))
    print(colored("|               In this project im checking                |", 'green'))
    print(colored("|              the correlation between doing               |", 'green'))
    print(colored("|           activities like puzzle and painting            |", 'green'))
    print(colored("|    and their contribution to patience and creativity.    |", 'green'))
    print(colored("|                                                          |", 'green'))
    print("FRAMEFRAMEFRAMEFRAMEFRAMEFRAMEFRAMEFRAMEFRAMEFRAMEFRAMEFRAME \n\n")


# Rating based on the number of hours of activity.
def full_data_frame(data_frame):
    new_list = list()
    for val in data_frame.index:
        total = (data_frame.loc[val, "Puzzle(Hours)"] + data_frame.loc[val, "Painting(Hours)"])

        #       if total >= 10 and (data_frame.loc[val, "Puzzle(Hours)"] or data_frame.loc[val, "Painting(Hours)"]) <= 2:
        #       houston = f"Houston, we have a problem in line number {val}"
        #    ratio_test(houston, new_list)

        data_frame.loc[val, "Total weekly hours"] = total

        if total >= 10:
            data_frame.loc[val, "Total Rating(1-5)"] = 5

        elif 9.5 >= total >= 8:
            data_frame.loc[val, "Total Rating(1-5)"] = 4

        elif 7.5 <= total >= 6:
            data_frame.loc[val, "Total Rating(1-5)"] = 3

        elif 5.5 <= total >= 4:
            data_frame.loc[val, "Total Rating(1-5)"] = 2

        else:
            data_frame.loc[val, "Total Rating(1-5)"] = 1

    return data_frame

    # Check Patience affects of doing Puzzle and rate it.

    # Check Creativity affects of Painting and rate it.


def check_creativity(data_frame):
    for val in data_frame.index:

        if data_frame.loc[val, "Painting(Hours)"] >= 10:
            data_frame.loc[val, "Creativity"] = 5

        elif 9.5 >= data_frame.loc[val, "Painting(Hours)"] >= 7.5:
            data_frame.loc[val, "Creativity"] = 4

        elif 7 >= data_frame.loc[val, "Painting(Hours)"] >= 5:
            data_frame.loc[val, "Creativity"] = 3

        else:
            data_frame.loc[val, "Creativity"] = 2

    full_data_frame(data_frame)
    return data_frame


def check_patience(data_frame):
    for val in data_frame.index:

        if data_frame.loc[val, "Puzzle(Hours)"] >= 10:
            data_frame.loc[val, "Patience"] = 5

        elif 9.5 >= data_frame.loc[val, "Puzzle(Hours)"] >= 7.5:
            data_frame.loc[val, "Patience"] = 4

        elif 7 >= data_frame.loc[val, "Puzzle(Hours)"] >= 5:
            data_frame.loc[val, "Patience"] = 3

        else:
            data_frame.loc[val, "Patience"] = 2

    check_creativity(data_frame)
    return data_frame


# Create new Data Frame and save to CSV file.
def create_data_frame():
    pzl = list()
    pnt = list()
    ptc = [None] * 1000
    crt = [None] * 1000
    twh = [None] * 1000
    tr = [None] * 1000

    for val in range(1, 1001):
        pzl.append(random.randint(0, 11))
        pnt.append(random.randint(0, 11))

    my_dict = {'Puzzle(Hours)': pzl, 'Patience': ptc, 'Painting(Hours)': pnt, 'Creativity': crt,
               'Total weekly hours': twh, 'Total Rating(1-5)': tr}

    df = pd.DataFrame(my_dict)
    df.to_csv('New_Dataframe.csv', index=False)

    data_frame = pd.read_csv('New_Dataframe.csv')

    return data_frame


# Main Function.
def main():
    new_data = create_data_frame()
    upd_data = check_patience(new_data)
    opening_message()
    option = menu_print()
    menu_options(option, upd_data)


main()
