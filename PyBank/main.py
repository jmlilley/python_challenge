import os
import csv

# file path for csv file
bank_csv = os.path.join('Resources', 'budget_data.csv')

# open csv file and read, skip first line since it is the header
with open (bank_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    # declare variables
    month_count = 0
    net_total = 0
    overall_change = 0
    previous_row = 0
    greatest_increase = 0
    greatest_decrease = 0
    greatest_increase_month = ""
    greatest_decrease_month = ""
    
    # loop through each row in csv file
    for row in csvreader:
        # add 1 to the total number of months counter
        month_count += 1
        # add value of current row to net total
        net_total = net_total + int(row[1])

        # cannot calculate the change from the previous for the first row so need to skip it
        if month_count > 1:
            # calculate the change of the current month compared to the previous month
            change = int(row[1]) - previous_row
            # add the current change to the overall change so average can be calculated at the end
            overall_change += change
            # check to see if the current change is the largest increase we have come across so far
            # if so, replace the new value and update the date 
            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_month = row[0]
            # check to see if the current change is the largest decrease we have come across so far
            # if so, replace the new value and update the date
            if change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_month = row[0]
        # store value of current row so that it can be used to determine the change with the next row
        previous_row = int(row[1])
# calculate the average change, subtract 1 from the month counter since the first month is not included
# round output to two decimal places
avg_change = round(overall_change/(month_count - 1), 2)

# print out results
print("Financial Analysis")
print("----------------------------")
print(f'Total Months: {month_count}')
print(f'Total: ${net_total}')
print(f'Average Change: ${avg_change}')
print(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})')
print(f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})')

# create a new text file that we can write to
with open('analysis/pybank_output_file.txt', "w") as datafile:
    # output the results, same as what was printed above
    # resource for write to new line : https://www.pythontutorial.net/python-basics/python-write-text-file/
    datafile.write('\n')
    datafile.write("Financial Analysis")
    datafile.write('\n')
    datafile.write("----------------------------")
    datafile.write('\n')
    datafile.write(f'Total Months: {month_count}')
    datafile.write('\n')
    datafile.write(f'Total: ${net_total}')
    datafile.write('\n')
    datafile.write(f'Average Change: ${avg_change}')
    datafile.write('\n')
    datafile.write(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})')
    datafile.write('\n')
    datafile.write(f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})')