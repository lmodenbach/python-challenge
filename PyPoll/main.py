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

import os
import csv

#create input variable and store path to source csv
election_data_csv = os.path.join("..", "Resources", "PyPoll", "election_data.csv")

 #create output variable and store path to .txt file
writing_path = os.path.join("PyPoll_results.txt")

#define function to output data, takes 3 lists of results with desired data in corresponding indices
def election_analysis(candidate_data, percent_data, totals_data):
    outputString = (
    f"-----------------------------------------------------------------------------\n"
    f"Election Results\n"
    f"-------------------------------\n"
    f"Total Votes: {totals_data[0]}\n"
    f"-------------------------------\n"
    f"{candidate_data[0]}: {percent_data[0]:.3f}% ({totals_data[1]})\n"
    f"{candidate_data[1]}: {percent_data[1]:.3f}% ({totals_data[2]})\n"
    f"{candidate_data[2]}: {percent_data[2]:.3f}% ({totals_data[3]})\n"
    f"{candidate_data[3]}: {percent_data[3]:.3f}% ({totals_data[4]})\n"
    f"-------------------------------\n"
    f"Winner: {candidate_data[4]}\n"
    f"-----------------------------------------------------------------------------\n"
    )
    return outputString


#pass in path variable and open up csv file for reading
with open(election_data_csv, 'r') as csvFile:

#specify a csv reader using commas as delimiter
    csvReader = csv.reader(csvFile, delimiter=',')

#declare lists and variables, initialize if needed
    candidate_results = []
    percent_results = [] 
    totals_results = []
    vote_count = -1
    totals_candidate_0 = 0
    totals_candidate_1 = 0
    totals_candidate_2 = 0
    totals_candidate_3 = 0

#for loop to iterate through rows in csv file
    for row in csvReader:
        vote_count += 1
        if (vote_count == 1):
           candidate_results.append(row[2])
           totals_candidate_0 += 1
        elif (vote_count > 1 ):
        
            if (row[2] not in candidate_results):
                candidate_results.append(row[2])
            
            if (row[2] == candidate_results[0]):
                totals_candidate_0 += 1
            elif (row[2] == candidate_results[1]):
                totals_candidate_1 += 1 
            elif (row[2] == candidate_results[2]):
                totals_candidate_2 += 1
            elif (row[2] == candidate_results[3]):
                totals_candidate_3 += 1
    totals_results.append(vote_count)
    totals_results.append(totals_candidate_0)
    totals_results.append(totals_candidate_1)
    totals_results.append(totals_candidate_2)
    totals_results.append(totals_candidate_3)
    percent_candidate_0 = int(round((totals_candidate_0/vote_count)*100))
    percent_results.append(percent_candidate_0)
    percent_candidate_1 = int(round((totals_candidate_1/vote_count)*100))
    percent_results.append(percent_candidate_1)
    percent_candidate_2 = int(round((totals_candidate_2/vote_count)*100))
    percent_results.append(percent_candidate_2) 
    percent_candidate_3 = int(round((totals_candidate_3/vote_count)*100))
    percent_results.append(percent_candidate_3)
    if (percent_candidate_0 > percent_candidate_1 & percent_candidate_0 > percent_candidate_2 & percent_candidate_0 > percent_candidate_3):
        candidate_results.append(candidate_results[0])
    elif (percent_candidate_1 > percent_candidate_0 & percent_candidate_1 > percent_candidate_2 & percent_candidate_1 > percent_candidate_3): 
        candidate_results.append(candidate_results[1])
    elif (percent_candidate_2 > percent_candidate_0 & percent_candidate_2 > percent_candidate_1 & percent_candidate_2 > percent_candidate_3):
        candidate_results.append(candidate_results[2])
    elif (percent_candidate_3 > percent_candidate_0 & percent_candidate_3 > percent_candidate_1 & percent_candidate_3 > percent_candidate_2):
        candidate_results.append(candidate_results[3])
    else:               
        candidate_results.append("No clear winner")


#print formatted output
print(election_analysis(candidate_results, percent_results, totals_results))

#write output to a new text file
with open(writing_path, "w") as textFile:
        textFile.write(election_analysis(candidate_results, percent_results, totals_results))
