# First we'll import the os module
import os

# Module for reading CSV files
import csv

# Module for statistics
import statistics


#Specify file path to read
budget_data_csv = os.path.join('.', "Resources", "budget_data.csv")


#Define lists for collecting data
p_n_l_change = []
month_change = []

#Define variables for previous month profit/loss and months
total_months = 0
total_profit = 0
previous_mprofit = 0
current_mprofit = 0
revenue_change = 0



#Open csv file in reader status
with open (budget_data_csv, 'r') as csv_file:

    #Read csv file and set delimiter value to ","
    csv_reader = csv.reader(csv_file, delimiter = ",")

    #Read the row with header first
    csv_header = next(csv_reader)

    #Iterate through data and read each row of data after the header
    for row in csv_reader:

        #Count the number of months
        total_months += 1

        #Calculate revenue for entire report
        current_mprofit = int(row[1])
        total_profit += current_mprofit

        #Set condition to initiate loop
        if (total_months == 1):
            #Validate starting in beginning of data
            previous_mprofit = current_mprofit
            continue

        else:
            #Calculate the change revenue
            revenue_change = current_mprofit - previous_mprofit

            #Add the month value to the month_change list
            month_change.append(row[0])

            #Add the revenue change for each month to the p_n_l_change list
            p_n_l_change.append(revenue_change)

            #Set condition to finish loop and start again until all data have been iterated
            previous_mprofit = current_mprofit



    #All profit changes added togather from each month
    profit_summary = sum(p_n_l_change)
    
    #Average of total of all changes from each month
    profit_average = round(profit_summary/(total_months - 1), 2)

    #Set variable and its value for month with greatest increase
    max_change = max(p_n_l_change)

    #set value and its value for month with greatest decrease
    min_change = min(p_n_l_change)

    #Determine index for greatest change in revenue for entire report
    max_month_index = p_n_l_change.index(max_change)


    #Determine index for greatest loss in revenue for entire report
    min_month_index = p_n_l_change.index(min_change)

    #Set variable and value for month with greatest increase 
    increase_month = month_change[max_month_index]

    #set variable ad value for month with greatest decrease
    decrease_month = month_change[min_month_index]


    #Define variable for header line in title print
    header_line = str("----------------------------")

    #Print line to space from previous text
    print(' ')
    
    #Print title
    print("Financial Analysis")
    
    #Print header lines 
    print(header_line)
    
    
    #Print Analysis report
    print("Total Months: " + str(total_months))
    print("Total: $" + str(total_profit))
    print("Average Change: $" + str(profit_average))
    print("Greatest Increase in Profits: " + str(increase_month) + " ($" + str(max_change) + ")")
    print("Greatest Decrease in Profits: " + str(decrease_month) + " ($" + str(min_change) + ")")



#set variable for pathway to write new file for results in Analasis folder
results = os.path.join(".", "analysis" , "pybank_results.txt")

#Open file to write to file
with open(results, "w") as py_file:
    
    #Write statesment to pybank_results.txt file 
    py_file.write("Financial Analysis" + "\n") 
    py_file.write(str(header_line) + "\n")
    py_file.write("Total Months: " + str(total_months) + "\n")
    py_file.write("Total: $" + str(total_profit) + "\n")
    py_file.write("Average Change: $" + str(profit_average) + "\n")
    py_file.write("Greatest Increase in Profits: " + str(increase_month) + " ($" + str(max_change) + ")" + "\n")
    py_file.write("Greatest Decrease in Profits: " + str(decrease_month) + " ($" + str(min_change) +  ")" + "\n")
    py_file.close() 



    


         






