
import pandas as pd

## All rights reserved - Amir Sillam - September 2022 ##

print("\nWe want to test the correlation between solving puzzles and drawing pictures\n"
      "And how these actions contribute"
      " to attributes such as patience and creativity.")

data = {
    "Puzzle": [2, 1, 1, 3, 1, 0 , 2],
    "Painting": [3, 1, 0, 1, 1, 2 , 1],
    "Creativity": ["High", "Ok", "Low", "High", "Ok", "Low" ,"High"],
    "Patient": ["High", "Ok", "Low", "Ok", "Ok", "High" , "High"]
}

dataFr = pd.DataFrame(data,
                  index=["Day1","Day2","Day3","Day4", "Day5","Day6",
                         "Day7"])

print()
print(dataFr)
