import random
import pandas as pd
import matplotlib.pyplot as plt

from termcolor import colored

# import matplotlib as mtb
# import numpy as nmp


"""
sort_bad_data():
ideas: 
1. val in ... != type(string)
2. val in ... != type(int)

"""


# Checking correlation between the hours of each activity and the effect on certain attributes.
def check_corr(data_frame):
    correlated_data = data_frame.corr()

   # print(correlated_data[correlated_data['Painting(Hours)'] > 0.9])
    print(f"\nChecking correlation: \n\n{correlated_data.to_string()}")


def plot_puzzle_data(upd_data):
    upd_data.plot(x='Puzzle(Hours)', y='Patience')
    plt.show()


def plot_painting_data(upd_data):
    upd_data.plot(x='Painting(Hours)', y='Creativity')
    plt.show()


def option_explanation():
    pass


def print_data_frame(data_frame):
    print(data_frame.to_string())


# Check menu options.
def menu_options(menu_option, data_frame):
    if menu_option == '1':
        print_data_frame(data_frame)

    elif menu_option == '2':
        print("hold it 1")

    elif menu_option == '3':
        check_corr(data_frame)

    elif menu_option == '4':
        plot_puzzle_data(data_frame)

    elif menu_option == '5':
        plot_painting_data(data_frame)

    else:
        print("EXIT program.")
        exit()


# Print menu message.
def menu_print():
    input_options = ['1', '2', '3', '4', '5', '6']

    print("Please Choose an option from the menu below:")
    print("| 1.Show Collected Data frame.             |\n"
          "| 2 Show correlation between so and so     | \n"
          "| 3.Show correlation between so and so     | \n"
          "| 4.Show plot of Puzzle.                   | \n"
          "| 5.Show plot of Painting.                 |\n"
          "| 6.End program.                           |\n")

    menu_option = input("Your input: ")
    while menu_option not in input_options:
        menu_option = input("You must insert only valid numbers,try again please: ")
    return menu_option


# Print the app starting message.
def opening():
    print("\nDATADATADATADATADATADATADATADATADATADATADATADATADATADATADATA")
    print("|                                                          |")
    print("|               This is our new Project !                  |")
    print("|            In this project we are checking               |")
    print("|             The correlation between doing                |")
    print("|          activities like puzzle and painting             |")
    print("|   and their contribution to patience and creativity.     |")
    print("|                                                          |")
    print("FRAMEFRAMEFRAMEFRAMEFRAMEFRAMEFRAMEFRAMEFRAMEFRAMEFRAMEFRAME \n\n")


# Rating based on the number of hours of activity.
def full_data_frame(data_frame):
    for val in data_frame.index:
        total = (data_frame.loc[val, "Puzzle(Hours)"] + data_frame.loc[val, "Painting(Hours)"])
        data_frame.loc[val, "Total weekly hours"] = total

        if total >= 10:
            data_frame.loc[val, "Total Rating(1-5)"] = 5

        elif 9.5 >= total >= 8:
            data_frame.loc[val, "Total Rating(1-5)"] = 4

        elif total <= 7.5 and total >= 6:
            data_frame.loc[val, "Total Rating(1-5)"] = 3

        elif total <= 5.5 and total >= 4:
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

    corr_data = pd.read_csv('New_Dataframe.csv')

    return corr_data


# Main Function.
def main():
    new_data = create_data_frame()
    upd_data = check_patience(new_data)
    opening()
    option = menu_print()
    menu_options(option, upd_data)


main()
