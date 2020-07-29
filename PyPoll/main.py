# Import csv
import os
import csv

#Read csv
election_csv = os.path.join("Resources", "election_data.csv")

#set blank lists
VoterID = []
County = []
Candidate = []  
Candidate_Clean = []
Candidate_Occur=[]

#open csv
with open(election_csv,'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    #skip header row
    csv_header = next(csv_reader)

    #append columns from CSV to lists
    for row in csv_reader:
        VoterID.append(row[0])
        County.append(row[1])
        Candidate.append(row[2])

       


#A complete list of candidates who received votes    
    for i in Candidate:
        if i not in Candidate_Clean:
            Candidate_Clean.append(i)

            #print(i)

    #print(Candidate_Clean)

#count number of votes per candidate
Candidate_Votes={}

for item in Candidate:
    if item not in Candidate_Occur:
        Candidate_Occur.append(item)
        Candidate_Votes[item] = 1
    else:
        Candidate_Votes[item] += 1
    
        
#print(Candidate_Votes)

#The total number of votes cast
TotalVotes = len(VoterID)


print("Election Results")
print("------------------------------")
print("Total Votes: ",TotalVotes)
print("------------------------------")

for k,v in Candidate_Votes.items():
    percentage = (v/TotalVotes)*100
    print(f"{k} : {percentage:.3f}% ({v})")

print("------------------------------")

#get max value from Candidate Votes Dictionary
winner = max(Candidate_Votes, key=Candidate_Votes.get)

print("Winner: ",winner)
print("------------------------------")





#The percentage of votes each candidate won


#The total number of votes each candidate won


#The winner of the election based on popular vote.

