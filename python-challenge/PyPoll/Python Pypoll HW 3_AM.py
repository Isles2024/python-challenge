import os
import csv

election_data = os.path.join('election_data.csv')

with open(election_data, 'r') as csvfile:
    csv_reader = csv.reader(csvfile)

    next(csv_reader, None)

    #1 - Total Votes Cast
    total_votes_cast = len(list(csv_reader))

   #2 Candidate list
    csvfile.seek(0)
    next(csv_reader, None)

    candidate_list = []
    candidate_votes = {}

    for row in csv_reader:
        candidate = row[2]
        if candidate not in candidate_list:
            candidate_list.append(candidate)
    
    #3 Candidate Votes
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1
    
    #4 Winner
    Winner = None
    most_votes = 0

print('Election Results')
print('---------------------------')
print(f'Total Votes: {total_votes_cast}')
print('---------------------------')
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes_cast) * 100
    print(f'{candidate}: {percentage:.2f}% ({votes} votes)')

    if votes > most_votes:
        most_votes = votes
        Winner = candidate
print('---------------------------')
print(f'Winner: {Winner}')

output_file = os.path.join('Election_results.txt')
with open(output_file, 'w') as textfile:
    textfile.write('Election Results\n')
    textfile.write('---------------------------\n')
    textfile.write(f'Total Votes: {total_votes_cast}\n')
    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes_cast) * 100
        textfile.write(f'{candidate}: {percentage:.2f}% ({votes} votes)\n')
        if votes > most_votes:
            most_votes = votes
            Winner = candidate
    textfile.write(f'Winner: {Winner}\n')