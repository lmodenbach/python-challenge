import os
import csv

#create input variable and store path to source csv
budget_data_csv_path = os.path.join("..", "Resources", "PyBank", "budget_data.csv")

#create output variable and store path to .txt file
writing_path = os.path.join("PyBank_results.txt")

#define function to output data, takes a list of results with desired data in different indices and 
#create/return a formatted string
def budget_analysis(budget_data_list):
    output_string = (
    f"-----------------------------------------------------------------------------\n"
    f"Financial Analysis\n"
    f"-------------------------------\n"
    f"Total Months: {budget_data_list[0]}\n"
    f"Total: ${budget_data_list[1]}\n"
    f"Average Change: ${budget_data_list[2]:.2f}\n"
    f"Greatest Increase in profits: {budget_data_list[3]} (${budget_data_list[4]})\n"
    f"Greatest Decrease in profits: {budget_data_list[5]} (${budget_data_list[6]})\n"
    f"-----------------------------------------------------------------------------\n"
    )
    return output_string
    
#pass in path variable and open up csv file for reading
with open(budget_data_csv_path, 'r') as csvFile:

#specify a csv reader using commas as delimiter
    csvReader = csv.reader(csvFile, delimiter=',')

#declare lists and variables and initialize if needed
    data_results = []
    list_of_changes = []
    total_profits_losses = 0
    rowControl = 0
    prev_row_PorL = 0
    min_change = 0
    max_change = 0
    max_month_year = ""
    min_month_year = ""
    
#for loop to iterate through rows in csv file
    for row in csvReader:

#chop off header
        if  (rowControl == 0):
            rowControl += 1

#pick up first profit/loss and store both as first previous profit/loss and first of the total profits/losses        
        elif (rowControl == 1):
            prev_row_PorL = int(row[1])
            total_profits_losses += int(row[1])
            rowControl += 1

#calculate change and append to list, reset previous profit/loss, accumulate total profits/losses  
        else:     
            current_PorL = int(row[1])
            current_change = current_PorL - prev_row_PorL
            list_of_changes.append(current_change)
            prev_row_PorL = int(row[1]) 
            total_profits_losses += int(row[1])
            
#keep track of max and min change, and the associated month/year - if no change in max/min do nothing
            if (current_change > max_change):
                max_change = current_change
                max_month_year = row[0]
            elif (current_change < min_change):
                min_change = current_change
                min_month_year = row[0]    

#get row count (one more than number of differences) and store it
    total_months = len(list_of_changes) + 1
    data_results.append(total_months)

#store sum of profits/losses
    data_results.append(total_profits_losses)     

#find average of change in profits/losses and store
    profit_loss_avg_change = sum(list_of_changes) / len(list_of_changes)
    data_results.append(profit_loss_avg_change)

#store max_change and associated month/year
    data_results.append(max_month_year)
    data_results.append(max_change)
   
#store min change and associated month/year 
    data_results.append(min_month_year)
    data_results.append(min_change)   
 
#pass results list to string function and print
    print(budget_analysis(data_results))
    
#write string to a new text file
with open(writing_path, "w") as textFile:
        textFile.write(budget_analysis(data_results))

    