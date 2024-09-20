# Basketball Player Statistics Analysis
____________
Purpose:
____________
This project is designed to analyze basketball player statistics from a CSV file and calculate various performance metrics. It identifies the top 100 players for each metric and displays the results. The goal is to provide insights into player performance based on different statistical measures.
___________________________________
Class Design and Implementation:
___________________________________
The project uses the pandas and numpy libraries for data manipulation and numerical operations. The main operations are performed on a pandas DataFrame loaded from a CSV file containing player statistics.
____________________
Class Attributes
____________________
data: A pandas DataFrame containing the player statistics loaded from the CSV file.

metrics: A list of performance metrics to be calculated and analyzed.

top_100_players: A dictionary to store the top 100 players for each metric.
___________
**Methods**
___________
load_data(file_path): Loads the player statistics data from the specified CSV file into the data attribute.

calculate_metrics(): Calculates various performance metrics and adds them as new columns to the data DataFrame.

Field Goal Accuracy (FG%): Percentage of successful field goals out of total field goal attempts.

Three Point Accuracy (3P%): Percentage of successful three-point shots out of total three-point attempts.

Free Throw Accuracy (FT%): Percentage of successful free throws out of total free throw attempts.

Average Points Scored per Minute (PPM): Average points scored per minute played.

Overall Shooting Accuracy (OS%): Overall shooting accuracy based on points scored and total shooting attempts (field goals and free throws).

Average Number of Blocks per Game (BPG): Average number of blocks per game.

Average Number of Steals per Game (SPG): Average number of steals per game.

identify_top_100_players(): This function identifies the top 100 players for each metric and stores the results in the top_100_players dictionary.

display_results(): Displays the top 100 players for each metric.
_______________
**Limitations**
_______________
Data Quality: The accuracy of the results depends on the quality and completeness of the input data.

Performance: For very large datasets, the sorting and selection operations may be time-consuming.

Assumptions: The code assumes that the input CSV file has the necessary columns (FGM, FGA, 3PM, 3PA, FTM, FTA, PTS, MIN, FGA, FTA, BLK, GP, STL).
__________
**Usage**
__________
Load the Data: Use the load_data(file_path) method to load the player statistics data from a CSV file.

Calculate Metrics: Use the calculate_metrics() method to calculate various performance metrics.

Identify Top 100 Players: Use the identify_top_100_players() method to identify the top 100 players for each metric.

Display Results: Use the display_results() method to display the top 100 players for each metric.
