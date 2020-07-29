# Import csv
import os
import csv

#Read csv
csv_path = os.path.join("Resources", "budget_data.csv")

#create empty list to store columns and calculuations
Date = []
Profit_Losses = []
Difference = []


# open/read csv
with open(csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    #skip header row
    csv_header = next(csv_reader)

    #add csv columns to lists
    for row in csv_reader:
        Date.append(row[0])
        Profit_Losses.append(int(row[1]))
    #print (Date)

# -To get the total number of months included in the dataset, put column A in a list and count using length
month_count = len(Date)


#get total amount of profit/losses
def Sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

 
# calculate the profit/losses each month
#Difference.append(none)
for i in range (1 , month_count):
    x = Profit_Losses[i] - Profit_Losses[i-1]
    Difference.append(x)

def Average(numbers):
    total = 0.00
    length = len(numbers)   
    for number in numbers:
        total += number
    return total / length

Max_Profit = max(Difference) 
Min_Profit = min(Difference)

x = Difference.index(Max_Profit)

Max_Date=Date[x+1]

y = Difference.index(Min_Profit)

Min_Date=Date[y+1]



#Print Findings
print("Financial Analysis")
print("------------------------")
print("Total Months: ",month_count)
print("Total: $",Sum(Profit_Losses))    
print("Average Change: $", round(Average(Difference), 2))
print(f"Greatest Increase in Profits: {Max_Date} (${Max_Profit})")
print(f"Greatest Decrease in Profits: {Min_Date} (${Min_Profit})")






