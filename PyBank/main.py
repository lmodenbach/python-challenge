"""Objectives:
-read in from python-challenge/Resources/PyBank/budget_data.csv
-total num months: total count rows
-net total profits/losses: sum column B
-changes in profits/losses with avg: diff between column B of current row and that of row before with avg diff
-greatest increase in profits: max of change in profits/losses
-greatest decrease in losses: min of change in profits/losses
-output to python-challenge/PyBank/PyBank_results.txt
"""
import os
import csv

#create input variable and store path to source csv
budget_data_csv_path = os.path.join("..", "Resources", "PyBank", "budget_data.csv")

#create output variable and store path to .txt file
writing_path = os.path.join("PyBank_results.txt")

#define function to output data, takes a list of results with desired data in different indices
def budget_analysis(budget_data_list):
    print(f"Financial Analysis\n")
    print(f"-------------------------------\n")
    print(f"Total Months: {budget_data_list[0]}\n")
    print(f"Total: ${budget_data_list[1]}\n")
    print(f"Average Change: ${budget_data_list[2]}\n")
    print(f"Greatest Increase in profits: {budget_data_list[3]} (${budget_data_list[4]})\n")
    print(f"Greatest Decrease in profits: {budget_data_list[5]} (${budget_data_list[6]})\n")
    print(f"-----------------------------------------------------------------------------\n")
    
#pass in path variable and open up csv file for reading
with open(budget_data_csv_path, 'r') as csvFile:

#specify a reader using commas as delimiter
    csvReader = csv.reader(csvFile, delimiter=',')

#declare lists and variables and initialize if needed
    data_results = []
    list_of_changes = []
    total_profits_losses = 0

#for loop to iterate through rows in csv file
    for row in csvReader:

#chop off header
        if  (row == 1):
            header = row[0] + row[1]
        else: 

#fill in list of changes from row to row in the second column, starting with list_of_changes[0] receiving the 
#difference between the second and first rows 
#run a sum on the profits/losses column           
            list_of_changes[row - 2] = (row[1]) - ((row-1)[1])
            total_profits_losses += (row[1]) 
#keep track of max and min change, and the associated month/year - if no change in max/min do nothing
            if (row > 2 & list_of_changes[row - 2] > list_of_changes[row - 3]):
                max_change = list_of_changes[row - 2]
                max_month_year = row[0]
            elif (row > 2 & list_of_changes[row - 2] < list_of_changes[row - 3]):
                min_change = list_of_changes[row - 2]
                min_month_year = row[0] 
            else:
                min_month_year = min_month_year   

#store sum of profits/losses
    data_results[0] = total_profits_losses 

#find average of change in profits/losses and store
    profit_loss_avg_change = sum(list_of_changes) / len(list_of_changes)
    data_results[2] = profit_loss_avg_change

#get row count (one more than number of differences) and store it
    total_months = len(list_of_changes) + 1
    data_results[1] = total_months

#store max_change and associated month/year
    data_results[4] = max_change
    data_results[3] = max_month_year

#store min change and associated month/year 
    data_results[6] = min_change
    data_results[5] = min_month_year
 
#for testing only
for change in list_of_changes:
    print(f"{change}\n")

budget_analysis(data_results)
    
# #pass function output to a string
# outputString = budget_analysis(data_results)

# #write string to a new text file
# with open(writing_path, "w") as textFile:
#         textFile.write(outputString)

    