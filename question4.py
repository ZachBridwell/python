import pandas as pd

# There are now 100 aliens, and their physical characteristics have been recorded in the file aliens.csv
# Write a function called "analyze" which opens aliens.csv and returns:
#    A) The mean number of arms the aliens have
#    B) The most common eye color of the aliens i.e., the mode
#    C) The data frame

def analyze():
    data = pd.read_csv('aliens.csv')
    meanArms = data['Number of Arms'].mean()
    mode = data['Eye Color'].mode()
    return meanArms, mode, data
# Define a function 'group' which reads aliens.csv into a dataframe and performs the following actions:
#    A) Groups the data by Eye color
#    B) Displays the group means
#    C) Displays the number of occurrences of each group
#    D) Returns the results of B) and C)

def group():
    data = pd.read_csv('aliens.csv')
    for key, item in data.groupby("Eye Color"):
        print(key + '\n', item.mean(), "\n\n")
    print(data.groupby("Eye Color").size())
    return data.groupby("Eye Color").mean(), data.groupby("Eye Color").size()
group()

#    The aliens appear to be mutating such that the amount of arms they have is halved.
#    Write a function called 'new_arms' which reads aliens.csv into a dataframe and performs the following actions:
#    A) Use a lambda function to generate the new number of arms the aliens will have, 
#    B) uses the lambda function to map the values of Number of Arms
#    C) returns in the result in B

def new_arms():
    data = pd.read_csv('aliens.csv')
    return data['Number of Arms'].map(lambda x: (x/2))