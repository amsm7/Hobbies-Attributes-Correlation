import MyApp
import pandas as pd

# Read csv file from directory.
corr_data = pd.read_csv('Book.csv')
print(corr_data)


# Check Creativity affects of Painting.


def check_creativity(corr_data):

    for val in corr_data.index:

        if corr_data.loc[val, "Painting"] >= 2:
            corr_data.loc[val, "Creativity"] = "This is very good!"

        elif corr_data.loc[val, "Painting"] == 1:
            corr_data.loc[val, "Creativity"] = "Nice, more it's better, try it !"

        else:
            corr_data.loc[val, "Creativity"] = "It's not enough my friend !"


# Check Patience affects of doing Puzzle.
def check_patience(corr_data):

    for val in corr_data.index:

        if corr_data.loc[val, "Puzzle"] >= 2:
            corr_data.loc[val, "Patience"] = "This is very good!"

        elif corr_data.loc[val, "Puzzle"] == 1:
            corr_data.loc[val, "Patience"] = "Nice, more it's better, try it !"

        else:
            corr_data.loc[val, "Patience"] = "It's not enough my friend !"

# Print the updated Data Frame.
def print_data_frame():
    print(corr_data.to_string())


"""
def check_act_cunclusion():
    pass



def check_atr_cunclusion():
    pass

"""


check_creativity(corr_data)
check_patience(corr_data)
print_data_frame()
