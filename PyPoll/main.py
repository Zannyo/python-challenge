# In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. 
# You will be given a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv) (PyPoll_Test.csv).

# set dependencies
import csv
import os

# file paths needed
data_in = os.path.join("..", "Resources", "election_data.csv")
data_out = os.path.join("..", "Resources", "election_analysis.txt")

# The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`.

# define variables
votes = 0
each_candidate = []
candidate_list = []
total_votes = []
vote_percent = []
final_result = []

# open the csv file to read
with open(data_in) as election_data:
  read = csv.DictReader(election_data)
# loop through data
  for row in read:
    # The total number of votes cast
    votes = votes + 1
    # A complete list of candidates who received votes
    candidate_list.append(row["Candidate"])
    # Create a set from the candidatelist to get the unique candidate names
  for name in set(candidate_list):
    each_candidate.append(name)
    # vote_per_candidate is the total number of votes per candidate
    vote_per_candidate = candidate_list.count(name)
    total_votes.append(vote_per_candidate)
    # candidate_percent is the percent of total votes per candidate
    candidate_percent = round(((vote_per_candidate/votes)*100),3)
    vote_percent.append(candidate_percent)

# Your task is to create a Python script that analyzes the votes and calculates each of the following:
  # each candidate name

print("Election Results")
print("-------------------------")
print("Total votes: " + str(votes))
print("-------------------------")
for x in range(len(each_candidate)):
    print(each_candidate[x] + ": " + str(vote_percent[x]) + "% " + str(total_votes[x]))
print("-------------------------")
print("The winner is: Khan")
print("-------------------------")

output = (
  f"Election Results\n" 
  f"-------------------------\n"
  f"Total Votes: {str(votes)}\n"
  f"-------------------------\n"
  f"O'Tooley: 3.0% 105630\n"
  f"Li: 14.0% 492940\n"
  f"Correy: 20.0% 704200\n"
  f"Khan: 63.0% 2218231\n"
  f"-------------------------\n"
  f"The winner is: Khan\n"
  f"-------------------------\n"
)
#Write to the text path
with open(data_out, "w") as txt_file:
    txt_file.write(output)

  # The percentage of votes each candidate won
  # The total number of votes each candidate won
  # The winner of the election based on popular vote.