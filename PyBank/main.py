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
writing_path = os.path.join("PyBank_results.txt")

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

#declare list
    data_results, list_of_diffs = []

#declare variable to help chop off header
header_counter = 1
#for loop to iterate through rows in csv file
    for row in csvReader:
        if  header_counter == 1:
            header = csvReader.next()
            prev_row_PorL = int(row[1])
            data_results[0] += 1
        else 
            list_of_diffs[row - 2] = int(row[1]) - prev_row_PorL 
            data_results[0] += 1
            data_results[1] += int(row[1])
            prev_row_PorL = int(row[1])
    header_counter += 1

# #pass function output to a string
# outputString = budget_analysis(data_results)

# #write string to a new text file
# with open(writing_path, "w") as textFile:
#         textFile.write(outputString)

    