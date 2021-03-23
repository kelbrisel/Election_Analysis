# Election_Analysis

## Project Overview
Audit for the Colorado Board of Elections of congressional district to analyze final vote results for each candidate and voter turnout for the district

#### Process of analysis:
1. Calculate total votes cast
2. Complile list of all candidates
3. Calculate total votes per candidate
4. Calculate percentage of votes per candidate
5. Determine winner based on popular vote
 
#### Resources
  -- Software: Python 2.7.16, Visual Studio Code, 1.38.1
  -- Data Source: election_results.csv


## Election-Audit Results
The analysis of the election shows that: 
* There were 369,711 votes cast
 -- Of that we saw 10.5% of the votes coming from Jefferson County (38,855), 82.8% from Denver County (306,055) and lastly 6.7% of the votes came from Arapahoe County (24,801).
 * The county with the highest voter turnout was **Denver County** at 82.8% of all votes cast.

* The candidates included Charles Casper Stockham, Diane DeGette and Raymon Anthony Doane.
* The candidates results were:
  -- *Charles Casper Stockham* received 23% of the votes (85,213)
  -- *Diana DeGette* received 73.8% of the votes (272,892)
  -- *Raymon Anthony Doane* received 3.1% of the votes (11,606)
* The winner of the election was:
 **Diana DeGette** who received 73.8% of the votes and 272,892 number of votes.
  
  <img width="405" alt="Election Results" src="https://user-images.githubusercontent.com/78561980/112073604-76abb900-8b42-11eb-9ca9-fbc36000993c.png">
  
 ## Election-Audit Summary
  In conducting the analysis of the election we were able to quickly reach final voter counts for each candidate, and after receiving the request from the Board, add to our original code to give us the voter turnout for each county in the district. By using Python, versus Excel for example, our code is formatted to include descriptive "pseudocode" for each line so it can be easily interpreted by future coders. Our code includes variables, versus naming the specific candidates or counties in this analysis, which makes the code perfect for analyzing future elections or use by other districts. In addition, larger datasets which include voter demographics or more broad geographical regions will only require small modifications. For additional output summarizing data such as voter age, gender, race/ethnicity, etc. adding indexing with for loop variables is a simple addition to the existing code. Relevant information such as vote turnout by political party would be easily summarized using this code, by adding if-statements, as well. 
