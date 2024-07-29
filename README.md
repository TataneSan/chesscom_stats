# chesscom_stats
Chess.com statistics about Titled Players

Description
This project provides a visual analysis of chess players' ratings across different formats: Bullet, Blitz, and Rapid. Using Plotly, we create interactive plots that show the relationship between players' FIDE ratings and their performance in these three categories. The script also calculates and displays the trend lines to understand the general behavior of the data.

Getting Started
Dependencies
Ensure you have the following Python packages installed:

Plotly
Pandas
NumPy
You can install these packages using pip:


```pip install plotly pandas numpy``` 
Installing
Clone the repository:

```git clone https://github.com/TataneSan/chesscom_stats/.git```
Navigate to the cloned directory:

```cd chesscom_stats```

## Data Format
Your data should be in a text file named merged_output.txt and formatted as follows:


PlayerName1:info|Y1_value:"value":Y2_value:"value":Y3_value:"value"|X_value
PlayerName2:info|Y1_value:"value":Y2_value:"value":Y3_value:"value"|X_value

You can use the mmerged_output.txt file which is present on the repository.
...
Each line represents a player with their ratings and a FIDE rating. Ensure the values are correctly formatted and separated by | and : as shown.

Usage
To run the analysis, follow these steps:

Ensure your data file merged_output.txt is in the root of the project directory and correctly formatted.
Run the script:

python plot.py
This script will:

- Read the data from merged_output.txt.
- Filter and clean the data.
- Plot the ratings against the FIDE rating.
- Calculate and display the slope of the trend lines for Bullet, Blitz, and Rapid ratings.
