import random
import pandas as pd

# Read csv file from directory.
corr_data = pd.read_csv('Book.csv')


# Check Creativity affects of Painting.
def check_creativity(corr_data):
    high_list = ["This is very good!", "Continue Please, Great Work!"]
    med_list = ["Nice, more it's better, try it !", "Good Job !"]
    low_list = ["It's not enough my friend !", "I believe in you, please believe in yourself !"]

    for val in corr_data.index:

        if corr_data.loc[val, "Painting"] >= 2:
            corr_data.loc[val, "Creativity"] = random.choice(high_list)

        elif corr_data.loc[val, "Painting"] == 1:
            corr_data.loc[val, "Creativity"] = random.choice(med_list)

        else:
            corr_data.loc[val, "Creativity"] = random.choice(low_list)


# Check Patience affects of doing Puzzle.
def check_patience(corr_data):
    high_list = ["This is very good!", "Continue Please, Great Work!", "Patience will pay off and even grow!"]
    med_list = ["Nice, more it's better, try it !", "You are on the right track."]
    low_list = ["It's not enough my friend !", "I believe in you, please believe in yourself !"]
    for val in corr_data.index:

        if corr_data.loc[val, "Puzzle"] >= 2:
            corr_data.loc[val, "Patience"] = random.choice(high_list)

        elif corr_data.loc[val, "Puzzle"] == 1:
            corr_data.loc[val, "Patience"] = random.choice(med_list)

        else:
            corr_data.loc[val, "Patience"] = random.choice(low_list)


# Print the updated Data Frame.
def print_data_frame(upd_data):

    print("\nPrinting table contents:\n")
    print(upd_data.to_string())


def check_total_rating(corr_data):
    for val in corr_data.index:
        total = float((corr_data.loc[val, "Puzzle"] + corr_data.loc[val, "Painting"]))

        if total >= 6:
            corr_data.loc[val, "Total Rating"] = 5

        elif total <=5.5 and total >= 4:
            corr_data.loc[val, "Total Rating"] = 4

        elif total <=3.5 and total >= 2:
            corr_data.loc[val, "Total Rating"] = 3

        elif total == 1.5:
            corr_data.loc[val, "Total Rating"] = 2

        else:
            corr_data.loc[val, "Total Rating"] = 1

    return corr_data


def check_corr(corr_data):
    print(f"\nChecking correlation: \n\n{corr_data.corr()}")


# Main Function.
def main(corr_data):
    check_creativity(corr_data)
    check_patience(corr_data)
    upd_data = check_total_rating(corr_data)
    print_data_frame(upd_data)
    check_corr(corr_data)


main(corr_data)
