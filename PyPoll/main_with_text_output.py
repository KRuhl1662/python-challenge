#ON THE WAY TO THE STORE TODAY IT DAWNED ON ME THAT I FORGOT TO DO THE TEXT OUTPUT, I REALIZE I MAY NOT GET CREDIT, BUT I DIDN'T WANT TO LEAVE IT INCOMPLETE

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

       


#A complete list of candidates who received votes (didn't end up using this ,but wanted to keep it)   
    # for i in Candidate:
    #     if i not in Candidate_Clean:
    #         Candidate_Clean.append(i)

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
    

#The total number of votes cast
TotalVotes = len(VoterID)


print("Election Results")
print("------------------------------")
print("Total Votes: ",TotalVotes)
print("------------------------------")

#Use Candidate Votes dictionary in loop to print for each value and its key, also calculate average
for k,v in Candidate_Votes.items():
    percentage = (v/TotalVotes)*100
    print(f"{k} : {percentage:.3f}% ({v})")

print("------------------------------")

#get max value from Candidate Votes Dictionary
winner = max(Candidate_Votes, key=Candidate_Votes.get)

print("Winner: ",winner)
print("------------------------------")

#print to text file

with open("Analysis/Analysis.txt", "w") as text_file:
    print(f"Election Results", file=text_file)
    print(f"------------------------------", file=text_file)
    print(f"Total Votes: {TotalVotes}", file=text_file)
    print(f"------------------------------", file=text_file)

    #Use Candidate Votes dictionary in loop to print for each value and its key, also calculate average
    for k,v in Candidate_Votes.items():
        percentage = (v/TotalVotes)*100
        print(f"{k} : {percentage:.3f}% ({v})", file=text_file)

    print(f"------------------------------", file=text_file)

    #get max value from Candidate Votes Dictionary
    winner = max(Candidate_Votes, key=Candidate_Votes.get)

    print(f"Winner: {winner}", file=text_file)
    print(f"------------------------------", file=text_file)



