# Python Homework Py Me Up Charlie (PuPoll)

# Import OS Module and Dependencies
import os
import csv

# Creating File Path
csvpath = os.path.join('.', 'election_data.csv')

# A list of all candidates
candidates = []

# A list with the number of votes each candidate receives
number_votes = []

# A list with the total of votes each candidate gets, shown in percentage
percent_votes = []

# Total number of votes
total_votes = 0


# Open and Read CSV File
with open(csvpath) as csvfile:

    # CSV Reader specifies delimeter and variable that holds content
    csvreader = csv.reader(csvfile, delimiter = ',')

    # Read the header row first
    csv_header = next(csvfile)

    # Read each row of data after the header
    for row in csvreader:

        # Calculate total number of votes 
        total_votes = total_votes + 1

        
        # Calculate total number of votes each candidate  won, and add each candidate name in our list
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            number_votes.append(1)
        else:
            index = candidates.index(row[2])
            number_votes[index] += 1
           

    # Calculating percentage of votes each candidate won
    for votes in number_votes:
        percentage = (votes/total_votes) * 100
        percentage = round (percentage)
        percent_votes.append(percentage)

    
    # Calculating winner of the election
    winner = max(number_votes)
    index = number_votes.index(winner)
    winning_candidate = candidates [index]


import sys
with open('c:goat.txt', 'w') as f:
    sys.stdout = f
# Print Analysis
print("Election Results")
print("----------------------------")
print(f"Total Votes: {str(total_votes)}")
print("----------------------------")
for i in range(len(candidates)):
    print(f"{(candidates[i])}: {percent_votes[i]:.1f}% {str(number_votes[i])}")
print ("---------------------------")
print(f"Winner: {winning_candidate}")
print("----------------------------")


# Creating a text file with the results
output_file = os.path.join('.','election_data.txt')
with open(output_file, 'w',) as datafile:

    write = csv.writer(datafile)
    datafile.write (f"Election Results\n")
    datafile.write (f"---------------------\n")
    datafile.write (f"Total Votes: {str(total_votes)}\n")
    datafile.write ("---------------------\n")
    datafile.write 
    for i in range (len(candidates)):
        (f"{candidates[i]}: {percent_votes[i]:.1f}% ({number_votes[i]})\n")
    datafile.write (f"Winner: {winning_candidate}\n")
    datafile.write (f"---------------------\n")