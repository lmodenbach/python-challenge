"""Objectives:
-read in from python-challenge/Resources/PyBank/budget_data.csv
-total num months: total count rows
-net total profits/losses: sum column B
-changes in profits/losses with avg: diff between column B of current row and that of row before with avg diff
-greatest increase in profits: max of changes in profits/losses
-greatest decrease in losses: min of changes in profits/losses
-output to python-challenge/PyBank/PyBank_results.txt
"""

#create input variable and store path to source csv
budget_data_csv = os.path.join("..", "Resources", "PyBank", "budget_data.csv")

#create output variable and store path to .txt file
output_path = os.path.join("PyBank_results.txt")

#define function to output data, takes a list of results with desired data in different indices
def budget_analysis(budget_data):
    print(f"Financial Analysis\n")
    print(f"-------------------------------\n")
    print(f"Total Months: {budget_data[0]}\n")
    print(f"Total: ${budget_data[1]}\n")
    print(f"Average Change: ${budget_data[2]}\n")
    print(f"Greatest Increase in profits: {budget_data[3]} (${budget_data[4]})\n")
    print(f"Greatest Decrease in profits: {budget_data[5]} (${budget_data[6]})\n")
    print(f"-----------------------------------------------------------------------------\n")

#pass in path variable and open up csv file for reading
with open(budget_dat_csv, 'r') as csvFile:

#specify a reader using commas as delimiter
    csvReader = csv.reader(csvFile, delimiter=',')

#for loop to iterate through rows in csv file
    for row in csvReader: