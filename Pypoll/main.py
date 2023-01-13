import os
import csv

# file path for csv
election_csv = os.path.join('Resources', 'election_data.csv')

# create global variables
vote_count = 0
candidates = []
candidate_votes = []
total_candidates = 0
winner = ""
winner_votes = 0

# open and read csv file, skip first line since it is the header
with open (election_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

# go through each row in csv file
    for row in csvreader:
        # overall vote counter
        vote_count += 1
        # extract the name of the person who received the vote
        person = row[2]
        # if the candidate is not in our list, add their name and add 1 vote to their vote total
        if person not in candidates:
            candidates.append(person)
            candidate_votes.append(1)
            total_candidates += 1
        # if the candidate is already in our list, identify their position in our list and add 1 vote
        else:
            x = 0
            while x < total_candidates:
                if person == candidates[x]:
                    candidate_votes[x] += 1
                x += 1

# print total votes output
print("Election Results")
print("----------------------------")
print(f'Total Votes: {vote_count}')
print("----------------------------")

# loop to output each candidate and the number of votes they received, as well as the percentage
# loop also identifies which candidate received the most votes
z = 0
while z < total_candidates:
    percentage = candidate_votes[z]/vote_count
    percentage = round(percentage * 100, 3)
    print(f'{candidates[z]}: {percentage}% ({candidate_votes[z]})')

    if candidate_votes[z] > winner_votes:
        winner_votes = candidate_votes[z]
        winner = candidates[z]
    z += 1
# print remaining outputs
print("----------------------------")
print(f'Winner: {winner}')
print("----------------------------")

# create a new text file that we can write to
with open('analysis/pypoll_output_file.txt', "w") as datafile:
    # output the results, same as what was printed above
    # resource for write to new line : https://www.pythontutorial.net/python-basics/python-write-text-file/
    datafile.write("Election Results")
    datafile.write('\n')
    datafile.write("----------------------------")
    datafile.write('\n')
    datafile.write(f'Total Votes: {vote_count}')
    datafile.write('\n')
    datafile.write("----------------------------")
    datafile.write('\n')
    
    z = 0
    while z < total_candidates:
        percentage = candidate_votes[z]/vote_count
        percentage = round(percentage * 100, 3)
        datafile.write(f'{candidates[z]}: {percentage}% ({candidate_votes[z]})')
        datafile.write('\n')

        if candidate_votes[z] > winner_votes:
            winner_votes = candidate_votes[z]
            winner = candidates[z]
        z += 1
    
    datafile.write("----------------------------")
    datafile.write('\n')
    datafile.write(f'Winner: {winner}')
    datafile.write('\n')
    datafile.write("----------------------------")