# set dependencies
import csv
import os

# file paths needed
data_in = os.path.join("..", "Resources", "budget_data.csv")
data_out = os.path.join("..", "Resources", "budget_analysis.txt")

# define variables and set to 0 
months = 0
profloss = 0
prev_profloss = 0
profloss_change = 0
profloss_change_list = []
month_change = []
big_inc = ["", 0]
big_dec = ["", 99999999999]

# read the budget_data.csv file
with open(data_in) as profloss_data:
   read = csv.DictReader(profloss_data)

# loop through data
   for row in read:

       # count months and calculate net Profit/Losses
           months = months + 1
           profloss = profloss + int(row["Profit/Losses"])

# calculate changes in profit/losses
           profloss_change = int(row["Profit/Losses"]) - prev_profloss
           prev_profloss = int(row["Profit/Losses"])
           month_change = month_change + [row["Date"]]

           #Greatest Increase value
           if (profloss_change > big_inc[1]):
               big_inc[1] = profloss_change
               big_inc[0] = row["Date"]

           if (profloss_change < big_dec[1]):
               big_dec[0] = row["Date"]
               big_dec[1] = profloss_change
        
# calculate the average profit/losses for all datA
mean_profloss = sum(profloss_change_list) / months


#print the outcomes
analysis = (
    f"Total Months: {months}\n"
    f"Total: {profloss}\n"
    f"Average Change: ${mean_profloss}\n"
    f"Greatest increase in Profits: {big_inc[0]} ${big_inc[1]}\n"
    f"Greatest decrease in Profits: {big_dec[0]} ${big_dec[1]}\n"
)

print(analysis)

#Write to the text path
with open(data_out, "w") as txt_file:
    txt_file.write(analysis)