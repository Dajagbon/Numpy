import pandas as pd
import numpy as np

# Load the data
data = pd.read_csv("C:/Users/danie/Downloads/Pythonclasstwo/players_stats_by_season_full_details.csv")

# Calculate Field Goal Accuracy, Three Point Accuracy, and Free Throw Accuracy
data['FG%'] = np.divide(data['FGM'], data['FGA']) * 100
data['3P%'] = np.divide(data['3PM'], data['3PA']) * 100
data['FT%'] = np.divide(data['FTM'], data['FTA']) * 100

# Calculate Average Points Scored per Minute
data['PPM'] = np.divide(data['PTS'], data['MIN'])

# Calculate Overall Shooting Accuracy
data['OS%'] = np.divide(data['PTS'], (data['FGA'] + data['FTA']))

# Calculate Average Number of Blocks per Game and Average Number of Steals per Game
data['BPG'] = np.divide(data['BLK'], data['GP'])
data['SPG'] = np.divide(data['STL'], data['GP'])

# Create a list of the top 100 players and corresponding seasons for each metric
metrics = ['FG%', '3P%', 'FT%', 'PPM', 'OS%', 'BPG', 'SPG']
top_100_players = {}

for metric in metrics:
    top_100_players[metric] = data[['Player', 'Season', metric]].sort_values(by=metric, ascending=False).head(100)

# Display the results
for metric in metrics:
    print(f"Top 100 players for {metric}:")
    print(top_100_players[metric].to_string(index=False))
    print("\n")
