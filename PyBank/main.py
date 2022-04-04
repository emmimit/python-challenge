# Python Homework Py Me Up Charlie (PyBank)

# Import OS Module and Dependencies
import os
import csv

#Create file path
csvpath = os.path.join('.', 'budget_data.csv')

# Creating Variables 
total_months = 0
net_amount = 0
monthly_change = []
month_count = []
greatest_increase = 0
greatest_increase_month = 0
greatest_decrease = 0
greatest_decrease_month = 0

# Open and Read CSV File
with open(csvpath) as csvfile:

    # CSV Reader specifies delimeter and variable that holds content
    csvreader = csv.reader(csvfile, delimiter = ',')

    # Read the header row first
    csv_header = next(csvreader)
    row = next(csvreader)
        
    # Calculating the total number of months, the net total of "Profit/Losses" 
    previous_row = int(row[1])
    total_months +=1
    net_amount += int(row[1])
    greatest_increase = int(row[1])
    greatest_decrease_month = row[0]
    greatest_decrease_month = row[0]

     # Read each row of data after the header
    for row in csvreader:

            # Calculate Total Number of months 
            total_months = total_months + 1
            # Calculate net amount from current to previous month
            net_amount += int(row[1])

            # Calculating change from current to previous month
            revenue_change = int(row[1]) - previous_row
            monthly_change.append(revenue_change)
            previous_row = int(row[1])
            month_count.append(row[0])

            # Calculating the greatest increase
            if int(row[1]) > greatest_increase:
                greatest_increase = int(row[1])
                greatest_increase_month = row[0]

            # Calculating the greatest decrease
            if int(row[1]) < greatest_decrease:
                greatest_decrease = int(row[1])
                greatest_decrease_month = row[0]

# Calculate the average and date
average_change = sum(monthly_change)/ len(monthly_change)

highest = max(monthly_change)
lowest = min(monthly_change)

# Print out Analysis
print(f"Financial Analysis")
print(f"---------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_amount}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits:, {greatest_increase_month}, (${highest})")
print(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${lowest}) ")

# Specifying file to write to and creating a text file with the results
output_file = os.path.join('.','financial_analysis.txt')
with open(output_file, 'w',) as datafile:

    write = csv.writer(datafile)
    datafile.write(f"Financial Analysis\n")
    datafile.write(f"---------------------------\n")
    datafile.write(f"Total Months: {total_months}\n")
    datafile.write(f"Total: ${net_amount}\n")
    datafile.write(f"Greatest Increase in Profits:, {greatest_increase_month}, (${highest})\n")
    datafile.write(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${lowest})\n")
