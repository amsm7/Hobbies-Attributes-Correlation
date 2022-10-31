# All rights reserved - Amir Sillam - October 2022

import numpy as np
import pandas as pd
from termcolor import colored
import matplotlib.pyplot as plt


def plot_painting_data(upd_data):
    """ Create diagram of painting and creativity and visualize it. """

    upd_data.plot(x='Painting(Hours)', y='Creativity')
    print("------------------------------------------------------------- ")
    print(plot_painting_data.__doc__)
    print("------------------------------------------------------------- \n")
    print("** Note: Close the plot window if you wish"
          " to run the program again.")

    plt.show()


def plot_puzzle_data(upd_data):
    """ Create diagram of doing puzzle and patience and visualize it. """

    upd_data.plot(x='Puzzle(Hours)', y='Patience')
    print("------------------------------------------------------------ ")
    print(plot_puzzle_data.__doc__)
    print("------------------------------------------------------------ \n")
    print("** Note: Close the plot window if you wish"
          " to run the program again.")

    plt.show()


def painting_creativity_corr(data_frame):
    """ Correlation between Painting and contribution to Creativity. """

    new_corr = data_frame['Painting(Hours)'].corr(data_frame['Creativity'])
    print("------------------------------------------------------------ ")
    print(painting_creativity_corr.__doc__)
    print("------------------------------------------------------------ \n")
    print(colored(data_frame[['Painting(Hours)', 'Creativity']].corr(),
                  'blue'))
    print(colored(f"\n** full length: {new_corr}", 'blue'))

    if new_corr > 0.75:
        print(colored(f"\n** We got {round(new_corr, 2)} correlation between "
                      f"painting and creativity attribute."
                      f"\nTherefore the correlation is Strong.", 'blue'))


def puzzle_patience_corr(data_frame):
    """ Correlation between doing Puzzle and contribution to Patience."""

    new_corr = data_frame['Puzzle(Hours)'].corr(data_frame['Patience'])
    print("--------------------------------------------------------------- ")
    print(puzzle_patience_corr.__doc__)
    print("--------------------------------------------------------------- \n")
    print(colored(data_frame[['Puzzle(Hours)', 'Patience']].corr(), 'blue'))
    print(colored(f"\n** full length: {new_corr}", 'blue'))

    if new_corr > 0.75:
        print(colored(f"\n** We got {round(new_corr, 2)} correlation between "
                      f"doing puzzle and patience attribute."
                      f"\nTherefore the correlation is Strong.", 'blue'))


def check_corr(data_frame):
    """ Getting data frame and printing all of its correlation ."""

    correlated_data = data_frame.corr()
    print("------------------------------------------------------")
    print(check_corr.__doc__)
    print("------------------------------------------------------\n")

    return colored(f"{correlated_data.to_string()}", 'blue')


def print_data_frame(data_frame):
    """ Print the whole data frame. """

    print("------------------------ ")
    print(print_data_frame.__doc__)
    print("------------------------ ")
    print(data_frame.to_string())


def user_input(menu_option, data_frame):
    """ Check user input and call to certain functions according to it. """

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
        print("You choose to exit the program, see you soon !")
        exit("\n             _ _ _ EXIT _ _ _")


def menu_input(data_frame):
    """ User menu input."""

    input_options = ['1', '2', '3', '4', '5', '6', '7']

    menu_option = input(colored("\nYour input: ",
                                'green'))
    count = 1
    while menu_option not in input_options:
        if count > 5:
            print(f"You have tried {count - 1} times, that's the limit.")
            exit("Try again next time, Thank you.")
        count += 1
        menu_option = input(colored("You must insert only valid numbers,try again please:", 'green'))
    user_input(menu_option, data_frame)
    print()
    menu_print(data_frame)


def menu_print(upd_data):
    """ Print menu message."""

    print("-------------------------------------------- ")
    print("Please Choose an option from the menu below:")
    print("-------------------------------------------- ")
    print(colored("------------------------------------------------------- \n"
                  "| 1.Show Collected Data frame.                        |\n"
                  "| 2.Show all Data frame correlation.                  | \n"
                  "| 3.Show correlation between Puzzle and Patience      | \n"
                  "| 4.Show correlation between Painting and Creativity. | \n"
                  "| 5.Show plot of Puzzle.                              | \n"
                  "| 6.Show plot of Painting.                            |\n"
                  "| 7.End program.                                      |\n"
                  "-------------------------------------------------------", 'green'))
    menu_input(upd_data)


def opening_message():
    """ Print the app starting message. """
    print("<<<   All rights reserved - Amir Sillam - October 2022   >>> ")
    print("\nDATADATADATADATADATADATADATADATADATADATADATADATADATADATADATA")
    print(colored("|                                                          |", 'green'))
    print(colored("|                This is my new Project !                  |", 'green'))
    print(colored("|               In this project im checking                |", 'green'))
    print(colored("|              the correlation between doing               |", 'green'))
    print(colored("|           activities like puzzle and painting            |", 'green'))
    print(colored("|    and their contribution to patience and creativity.    |", 'green'))
    print(colored("|                                                          |", 'green'))
    print("FRAMEFRAMEFRAMEFRAMEFRAMEFRAMEFRAMEFRAMEFRAMEFRAMEFRAMEFRAME \n\n")


def full_data_frame(data_frame):
    """ Rating based on the number of hours of activity. """

    for val in data_frame.index:
        total = (data_frame.loc[val, "Puzzle(Hours)"] + data_frame.loc[val, "Painting(Hours)"])

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


def check_creativity(data_frame):
    """ Check Creativity effects of Painting, and rate it. """
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
    """ Check Patience effects of doing Puzzle, and rate it."""

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


def create_data_frame():
    """ Create new Data Frame and save it to CSV file."""

    pzl = np.random.randint(1, 11, 1000)
    pnt = np.random.randint(1, 11, 1000)
    ptc = np.full(shape=1000, fill_value=0)
    crt = np.full(shape=1000, fill_value=0)
    twh = np.full(shape=1000, fill_value=0)
    tr = np.full(shape=1000, fill_value=0)

    my_dict = {'Puzzle(Hours)': pzl, 'Patience': ptc, 'Painting(Hours)': pnt,
               'Creativity': crt, 'Total weekly hours': twh, 'Total Rating(1-5)': tr}

    df = pd.DataFrame(my_dict)
    df.to_csv('New_Dataframe.csv', index=False)

    data_frame = pd.read_csv('New_Dataframe.csv')

    return data_frame


def main():
    """ Main function - starts the program and invoke functions."""
    new_data = create_data_frame()
    upd_data = check_patience(new_data)
    opening_message()
    menu_print(upd_data)


main()
