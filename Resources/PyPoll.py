# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

# Assign a variable for the file to load and the path


# Open the election results and read the file.

# To do: perform analysis.

# Close the file.  
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

total_votes = 0
candidate_options = []

candidate_votes = {}
#candidate_votes = {"Charles Casper Stockham": votes, "Diana Degette": votes, "Raymon Anthony Doane": votes}

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

    headers = next(file_reader)
    print(headers)


    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
           # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

            # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
# Print the candidate list.
print(candidate_options)


print(candidate_votes)

print(total_votes)


winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = round(float(votes) / float(total_votes) * 100,1)
    # 4. Print the candidate name and percentage of votes.
    print(f"{candidate_name}: received {vote_percentage}% of the vote.")

    if (votes>winning_count) and (vote_percentage> winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate= candidate_name

    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
print(winning_candidate_summary)



#directory = "analysis"
#if not os.path.exists(directory):
#    os.makedirs(directory)


#outfile = open(file_to_save, "w")

#os.path.exists(file_to_save)

#outfile.write("Hello World again")

#outfile.close()

#with open(file_to_save, "w") as txt_file:
#    txt_file.write("Counties in the Election\n-------------\nArapahoe\nDenver\nJefferson")




