# import modules
import os
import csv

#set the path for BudgetData.csv in LearnPython > PyBank
data = os.path.join("BudgetData.csv")

#Create empty lists to append to later on 

monthly_changes_list = []
profit_loss = []
date = []

#set variable values to 0 so that when we loop through data we have a starting point
#hardcode initial month to starting value 867884
#average will be divided by months-1
months = 0
total = 0
total_change = 0
initial = 867884
#given total months = 86, there will only be months-1 monthly changes


#open data csv "with loop"
with open(data, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    #remember row[0] is the month and row[1] is the $$$
    #for loop to count each row.  This will give us the total number of months for average later
    for row in csvreader:
        months = months + 1
        #append values of each row in dates column to date list so we have values for max and min later
        date.append(row[0])
        #create "total" list and sum each value in the list to find our total profit or loss
        profit_loss.append(row[1])
        total = total + int(row[1])

        #create month 2 month variables.  final is the current row and initial is the row before.
        #the monthly change is final - initial
        #make sure we make the initial = to the next final before we go to next row
        #remember initial for month 1 is hardcoded, total change = 0
        final = int(row[1])
        monthly_change_pl = final - initial
        monthly_changes_list.append(monthly_change_pl)
        total_change = total_change + monthly_change_pl
        initial = final

        #avg formula = total_change/ months-1 ---86 months, but 85 monthly changes
        
        #average_change_pl = total_change/month_change_count

        #how do we find greatest increase and greatest decrease?
        #take monthly_changes_list and use max min functions to find largest/ smallest value
        greatest_increase = max(monthly_changes_list)
        greatest_decrease = min(monthly_changes_list)


        #use greatest inc and dec as an index to pull the month and year for print statement
        greatest_increase_month = date[monthly_changes_list.index(greatest_increase)]
        greatest_decrease_month = date[monthly_changes_list.index(greatest_decrease)]
    
    #monthly changes count accounts for the fact that there is one less monthly change than months
    monthly_changes_count = months-1
    average_change_pl = total_change/monthly_changes_count

    #print to terminal
    print("Financial Analysis:")
    print("-----------------------------------------------------------------------------")
    print("Total Months: " +str(months))
    print("Total: $" +str(total))
    print("Average Change: $"+ str(int(average_change_pl)))
    print("Greatest Increase in Profits: " + str(greatest_increase_month) + " $" + str(greatest_increase))
    print("Greatest Decrease in Profits: " + str(greatest_decrease_month) + " $" + str(greatest_decrease))

#print to .txt
with open('fa.txt', 'w') as txt:
    txt.write("Financial Analysis" + "\n")
    txt.write("----------------------------------------------" + "\n")
    txt.write("Total Months: " + str(months) + "\n")
    txt.write("Total: $" + str(total) + "\n")
    txt.write("Average Change: $" + str(int(average_change_pl)) +"\n")
    txt.write("Greatest Increase in Profits: $" + str(greatest_increase_month) + " $" + str(greatest_increase) + "\n")
    txt.write("Greatest Decrease in Profits: $" + str(greatest_decrease_month) + " $" + str(greatest_decrease) +"\n")
    
    


