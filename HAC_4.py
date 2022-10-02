import random
import pandas as pd

# Read csv file from directory.
corr_data = pd.read_csv('Book.csv')


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
        corr_data.loc[val, "Total Weekly hours"] = total

        if total >= 10:
            corr_data.loc[val, "Total Rating"] = 5

        elif 9.5 >= total >= 8:
            corr_data.loc[val, "Total Rating"] = 4

        elif total <= 7.5 and total >= 6:
            corr_data.loc[val, "Total Rating"] = 3

        elif total <= 5.5 and total >= 4:
            corr_data.loc[val, "Total Rating"] = 2

        else:
            corr_data.loc[val, "Total Rating"] = 1

    return corr_data


# Checking correlation between the hours of each activity and the effect on certain attributes.
def check_corr(corr_data):
    print(f"\nChecking correlation: \n\n{corr_data.corr().to_string()}")


# Main Function.
def main(corr_data):
    check_creativity(corr_data)
    check_patience(corr_data)
    upd_data = check_total_rating(corr_data)
    print_data_frame(upd_data)
    check_corr(corr_data)


main(corr_data)
