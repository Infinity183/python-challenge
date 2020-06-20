# Let's first import our dependencies.
import os
import csv

# Now we'll open up the election_data csv file.
election_data = os.path.join("PyPoll", "Resources", "election_data.csv")

# I'm going to define my essential variables/empty lists for later.

# The vote counter will start at 0, but steadily increase once we
# open the csv and loop through it.
number_of_votes = 0

# The candidate list will include the names of each unique candidate
# we discover in the csv.
candidate_list = []

# The candidate counter will contain vote counters with indexes that
# directly correspond to the candidate list.
candidate_counter = []

# The candidate percentages list will make it easier for me to print
# the percentages each candidate received more easily later.
candidate_percentages = []

# Now we will open and read the csv file.
with open(election_data) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # Don't forget the header!
    csv_header = next(csv_reader)

    for row in csv_reader:

        # Each new row delineates a new vote, so we'll add 1 to the
        # total number of votes:
        number_of_votes += 1

        # If we come across a candidate who hasn't yet appeared in the
        # list of candidates, we will need to append the new candidate
        # to our grand list of candidates (row[2] corresponds to the
        # candidate that the current voter cast their ballot for):
        if row[2] not in candidate_list:
            candidate_list.append(row[2])

            # In addition to adding the new candidate to the list of
            # candidate names, we must also add a new index to the
            # list of vote totals. Since the current row is the given
            # candidate's first vote so far, we will start the new
            # counter at 1.
            candidate_counter.append(1)

        # If the current voter chose somebody already accounted for,
        # then we must add 1 to that candidate's vote counter.
        elif row[2] in candidate_list:

            # This nested for loop searches for the chosen candidate
            # in the candidate_list and uses the corresponding index
            # to add one vote to the appropriate counter in the
            # candidate_counter list.
            for i in candidate_list:
                if i == row[2]:

                    # The index is that which corresponds to where the
                    # chosen candidate is found in candidate_list.
                    index = candidate_list.index(i)
                    candidate_counter[index] += 1

# It's time to print our results.

print("FINAL RESULTS")
print("* * * * * * * *")
print("")
print(f'Total Votes: {number_of_votes}')
print("")

# This for loop prints the total number of votes for each candidate.
# It'll go through the candidate_list and use the current index to
# extract the corresponding number of votes in candidate_counter.
for j in candidate_list:
    print(f'Votes for {j}: {candidate_counter[candidate_list.index(j)]}')

    # Since we now have a full list of candidates and their vote grand
    # totals, we may now calculate their vote percentages. I am building
    # the candidate_percentages list in this for loop out of convenience.
    # Each percentage will equal the candidate's number of votes divided
    # by the total number of votes for all candidates.
    candidate_percentages.append((candidate_counter[candidate_list.index(j)] / number_of_votes))
print("")

# With our candidate_percentages list complete, we'll now print a list
# of vote percentages for each candidate.
for k in candidate_percentages:
    print(f'Percent Votes for {candidate_list[candidate_percentages.index(k)]}: {round(k * 100, 3)}%')

# Finally, we need to peruse the vote totals for each candidate to
# determine the winner. To do this properly, we need to find the max
# value in the candidate_counter list before corresponding the value
# to the winning candidate. For this, we can simply create a new
# variable that determines the highest vote total in candidate_counter.
highest_votes = max(candidate_counter)

# With highest_votes defined, we'll now decide the winner from the
# list of candidates.
for l in candidate_counter:
    
    # The winning value has to equal highest_votes.
    if l == highest_votes:

        # From candidate_list, we must use the index for
        # candidate_counter's highest value.
        winner = candidate_list[candidate_counter.index(l)]
print("")

# We will now declare the winner.
print(f'Looks like {winner} is headed for office!')

# Okay! Now for the exported .txt version!
text_path = os.path.join("PyPoll", "analysis", "Poll Results.txt")
analysis = open(text_path, 'w')

analysis.write("FINAL RESULTS\n")
analysis.write("* * * * * * * *\n\n")
analysis.write(f'Total Votes: {number_of_votes}\n\n')

for j in candidate_list:
    analysis.write(f'Votes for {j}: {candidate_counter[candidate_list.index(j)]}\n')
    
    # We've already built the percentage list,
    # so no need to repeat it.

analysis.write("\n")

for k in candidate_percentages:
    analysis.write(f'Percent Votes for {candidate_list[candidate_percentages.index(k)]}: {round(k * 100, 3)}%\n')

# We've already defined highest_votes and winner,
# so no need to repeat them.

analysis.write("\n")

# We will now declare the winner.
analysis.write(f'Looks like {winner} is headed for office!')