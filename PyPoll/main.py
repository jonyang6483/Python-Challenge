
# First we'll import the os module
import os

# Module for reading CSV files
import csv

# Module for statistics
import statistics


#Specify file path to read
election_data_csv = os.path.join(".", "Resources", "election_data.csv")

#Set dictionary for candidates
Candidates = {}

#Open csv file in reader status
with open(election_data_csv, 'r') as csv_file:

    #Read csv file and set delimiter value to ","
    csv_reader = csv.reader(csv_file, delimiter= ",")

    #Read the header row first
    csv_header = next(csv_reader)

    #Set initial value for total votes to zero
    vote_total = 0

    #Iterate through data
    for row in csv_reader:

        #Count all votes
        vote_total += 1

        #Set start location for candidate_name is column 3
        candidate_name = row[2]

        #Set conditions to initiate loop
        if candidate_name in Candidates:

            #Increase by one to move to next row of data
            Candidates[candidate_name] += 1

        #Set condition to stop iteration
        else:
            Candidates[candidate_name] = 1



#Calculate percentage of votes per candidate based on keys for candidates dictionary
Candidates["stockham"] = round((Candidates["Charles Casper Stockham"]/vote_total) * 100, 3)
Candidates["deGette"] = round((Candidates["Diana DeGette"]/vote_total) * 100, 3)
Candidates["doane"] = round((Candidates["Raymon Anthony Doane"]/vote_total) * 100, 3)

#Set variable and value for election winner
election_winner = max(Candidates, key=Candidates.get)

#Create varable for header line output
header_line = ("-------------------------")

#Print to add space to previous text
print(" ")

#Output header
print("Election Results")

#Output header line
print(header_line)

#Output total votes amount
print("Total Votes: " + str(vote_total))

#Output header line
print(header_line)

#Output election results
print("Charles Casper Stockham: " + str(Candidates["stockham"]) + "% " + "(" + str(Candidates["Charles Casper Stockham"]) + ")" )
print("Diana DeGette: " + str(Candidates["deGette"]) + "% " + "(" + str(Candidates["Diana DeGette"]) + ")")
print("Raymon Anthony Doane: " + str(Candidates["doane"]) + "% " + "(" + str(Candidates["Raymon Anthony Doane"]) + ")" )

#Output header line
print(header_line)

#Output election winner
print("Winner: " + str(election_winner))

#Output header line
print(header_line)



#Set variable for file pathway
results = os.path.join(".", "analysis" , "election_results.txt")

#Open file to write to file
with open(results, "w") as py_file:

    #Write statesment to election_results.txt file 
    py_file.write("Election Results" + "\n")
    py_file.write(str(header_line) + "\n")
    py_file.write("Total Votes: " + str(vote_total) + "\n")
    py_file.write(str(header_line) + "\n")
    py_file.write("Charles Casper Stockham: " + str(Candidates["stockham"]) + "% " + "(" + str(Candidates["Charles Casper Stockham"]) + ")" + "\n")
    py_file.write("Diana DeGette: " + str(Candidates["deGette"]) + "% " + "(" + str(Candidates["Diana DeGette"]) + ")" + "\n")
    py_file.write("Raymon Anthony Doane: " + str(Candidates["doane"]) + "% " + "(" + str(Candidates["Raymon Anthony Doane"]) + ")" + "\n")
    py_file.write(str(header_line) + "\n")
    py_file.write("Winner: " + str(election_winner)+ "\n")
    py_file.write(str(header_line) + "\n")
    py_file.close() 







