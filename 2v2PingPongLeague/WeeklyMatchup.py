import pandas as pd
import random
from matching.games import StableRoommates

# read Excel file with League Standings
df = pd.read_excel("2v2PingPongLeague-FinalExcel.xlsx", sheet_name= 'League Table')

# number of players must be a multiple of 4 to make sure everybody plays a game every match-week
players = df["Players"].tolist()
my_dict = dict()

# definition of quartiles
quartileOne = players[0:int((len(players)/4))]
quartileTwo = players[int((len(players)/4)):int((len(players)/2))]
quartileThree = players[int((len(players)/2)):int(3 * (len(players)/4))]
quartileFour = players[int(3 * (len(players)/4)):int(len(players))]

# read Excel file with Players' previous teammates
dfPlayedWith = pd.read_excel("2v2PingPongLeague-FinalExcel.xlsx", sheet_name= 'Players Teamates')

"""Populates dictionary with players as the keys and their pref lists as the values
   preference lists are completely randomized
   players in the same quartile and previous teammates are invalid matchings, so they are placed at the end of the
   player's preference list. This is to make sure the dictionary is suitable for the stable roomates algorithm."""
for name in players:
    # randomizes players list to give each player equal probability of being chosen as a teammate for a suitable player
    # Ensures matches are random.
    playersRandomized = df["Players"].tolist()
    random.shuffle(playersRandomized)
    # removes current player from their own preference list
    playersRandomized.remove(name)
    # if and elif statements determine a players' quartile and appends players in the same quartile to the end of their
    # preference list
    if name in quartileOne:
        for i in quartileOne:
            try:
                playersRandomized.remove(i)
                playersRandomized.append(i)
            except ValueError:
                pass
    elif name in quartileTwo:
        for i in quartileTwo:
            try:
                playersRandomized.remove(i)
                playersRandomized.append(i)
            except ValueError:
                pass
    elif name in quartileThree:
        for i in quartileThree:
            try:
                playersRandomized.remove(i)
                playersRandomized.append(i)
            except ValueError:
                pass
    elif name in quartileFour:
        for i in quartileFour:
            try:
                playersRandomized.remove(i)
                playersRandomized.append(i)
            except ValueError:
                pass

    # find row number of player in the "Players Teammates" Tab to find previous teammates
    row_num_list = dfPlayedWith[dfPlayedWith["Players"] == name].index.tolist()
    row_index = row_num_list[0]
    removed_players = []

    # check's the players previous teammates for all weeks available and adds them to the end of the pref list
    for column in dfPlayedWith.columns:
        if column == "Players":
            continue
        removed_players.append(dfPlayedWith.at[row_index, column])

    for teammate in removed_players:
        playersRandomized.remove(teammate)
        playersRandomized.append(teammate)

    # stores the key value pair
    my_dict[name] = playersRandomized

#create game from diitonary
game = StableRoommates.create_from_dictionary(my_dict)

#create matchings
game.solve()


