import os
import csv

#create input variable and store path to source csv
election_data_csv = os.path.join("..", "Resources", "PyPoll", "election_data.csv")

 #create output variable and store path to .txt file
writing_path = os.path.join("..", "Analysis", "PyPoll_analysis.txt")

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

#increment vote_count with each row, initialized to -1 so header doesn't add a vote
        vote_count += 1

#if on first row of data, grab first candidate and record the vote
        if (vote_count == 1):
           candidate_results.append(row[2])
           totals_candidate_0 += 1

#otherwise... 
        elif (vote_count > 1 ):

#check if candidate is in candidate list and append if not        
            if (row[2] not in candidate_results):
                candidate_results.append(row[2])

#augment the vote for the appropriate candidate            
            if (row[2] == candidate_results[0]):
                totals_candidate_0 += 1
            elif (row[2] == candidate_results[1]):
                totals_candidate_1 += 1 
            elif (row[2] == candidate_results[2]):
                totals_candidate_2 += 1
            elif (row[2] == candidate_results[3]):
                totals_candidate_3 += 1

#add vote_count and candidate totals to results
    totals_results.append(vote_count)
    totals_results.append(totals_candidate_0)
    totals_results.append(totals_candidate_1)
    totals_results.append(totals_candidate_2)
    totals_results.append(totals_candidate_3)

#calculate and record percents, round decimal before converting to int to do math so we don't lose data
    percent_candidate_0 = int(round((totals_candidate_0/vote_count)*100))
    percent_results.append(percent_candidate_0)
    percent_candidate_1 = int(round((totals_candidate_1/vote_count)*100))
    percent_results.append(percent_candidate_1)
    percent_candidate_2 = int(round((totals_candidate_2/vote_count)*100))
    percent_results.append(percent_candidate_2) 
    percent_candidate_3 = int(round((totals_candidate_3/vote_count)*100))
    percent_results.append(percent_candidate_3)

#figure out who the winner is through comparisons then record
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
