# Add our dependencies.
import csv
import os
# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resource", "election_results.csv")
#Assign a variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis","election_analysis.txt")

#1 Initialize a total vote counter.
total_votes= 0

#candidate options
candidate_options = []
#Declare the empty dicionary
candidate_votes={}

# with open(file_to_save, "w") as txt_file:
    #write some data to the file.
    #txt_file.write("Counties in the Election\n")
    #txt_file.write("---------------------\n")
    #txt_file.write("Arapahoe\nDenver\nJefferson")
#Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
    
# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

# Read the file object with the reader function
    #file_reader = csv.reader(election_data)
    #Read the header row
    headers = next(file_reader)
     #Print each row in CSV file.
    for row in file_reader:
        #Add to the total vote count
        total_votes += 1

        #print candidate name from each row
        candidate_name = row[2]

        #If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            #Add the candidate name to list
            candidate_options.append(candidate_name)

            #Begin tracking that candidates votes
            candidate_votes[candidate_name]  = 0

        #Add a vate to that candidates count
        candidate_votes[candidate_name] += 1

print(candidate_votes)
#Determine the percentage of votes for each candidate by looping through
#1. Iterate through the candidate list
for candidate_name in candidate_votes:
    #2. Retrieve vote count of a candidate
    votes =  candidate_votes[candidate_name]
    #3 Calculate percentage of votes
    vote_percentage = float(votes) / float(total_votes) * 100

    #4 Print the candidate name, vote count and percentage
    #votes to the terminal
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    #Determine winning vote count and candidate
    #Determine if the votes is greater than the winning count
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        #If true then set winning_count = votes and winning_percent = vote_percentages
        winning_count = votes
        winning_percentage = vote_percentage
        #And set the winning_candidate equal to the candidate's name
        winning_candidate = candidate_name
winning_candidate_summary = (
    f"---------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"---------------\n")
print(winning_candidate_summary)      
    #print(f"{candidate_name}: received {vote_percentage}% of the vote.")
# Close the file
election_data.close()