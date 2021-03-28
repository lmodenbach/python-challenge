"""Objectives:
-read in from python-challenge/Resources/PyPoll/election_data.csv
-total num votes cast: count of rows
-list of candidates: list of unique string values in column C
-total num of votes per candidate: count of instances per each unique value in C
-percentage of vote won by candidate: (each count of instances over row count)*100
-winner of election based on pop vote: max of units of a data structure holding count of instances
    of unique values in C
-output results to python-challenge/PyPoll/PyPoll_results.txt
 """

#create input variable and store path to source csv
election_data_csv = os.path.join("..", "Resources", "PyPoll", "election_data.csv")

 #create output variable and store path to .txt file
output_path = os.path.join("PyPoll_results.txt")

#define function to output data, takes 3 lists of results with desired data in corresponding indices
def election_analysis(candidate_data, percent_data, totals_data):
    print(f"Election Results\n")
    print(f"-------------------------------\n")
    print(f"Total Votes: {election_data[0]}\n")
    print(f"{candidate_data[1]}: {percent_data[1]} ({totals_data[3]}\n")
    print(f"{candidate_data[2]}: {percent_data[2]} ({totals_data[6]}\n")
    print(f"{candidate_data[3]}: {percent_data[3]} ({totals_data[9]}\n")
    print(f"-----------------------------------------------------------------------------\n")


#pass in path variable and open up csv file for reading
with open(election_data_csv, 'r') as csvFile:

#specify a reader using commas as delimiter
    csvReader = csv.reader(csvFile, delimiter=',')

#for loop to iterate through rows in csv file
    for row in csvReader: