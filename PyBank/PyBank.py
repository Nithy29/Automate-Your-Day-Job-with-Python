# imports files
import pandas as pd
import os as os
from pathlib import Path

#Directory in the local repository
dir = "C:/GitBash/python-homework/PyBank"

# set the output of the text file
outFile = os.path.join(dir, "Analysis_output.txt")                 #Set output file
print(outFile)
        
readFile = os.path.join(dir, "budget_data.csv")                    #Set input file
df = pd.read_csv(readFile, delimiter=',')                          # read the csv file into data frame variable df using delimiter ',' 

TotalMonth = df['Date'].count()                                    #Calculate Total month by counting column 'Date'
print(f"Total Months: {TotalMonth}")                               #Print value of TotalMonth

total = "${:,.2f}".format(df['Profit/Losses'].sum())               #Calculate Total revenue by adding column 'Profit/Losses'
print(f"Total: {total}")                                           #Print total revenue - variable 'total'

df['RevenueChange'] = df['Profit/Losses'].diff()                   #Calculate Rev difference between month 1 & month 2 in column 'RevenueChange'
TotalChangeRevenue = (df['RevenueChange'].sum())                   #Calculate Total Rev Difference by adding column 'RevenueChange'

Count_ChangeInRevenueMonth = df['RevenueChange'].count()           #Need this value to calculate the AverageChange in revenue
AverageChange = "${:,.2f}". format(TotalChangeRevenue/Count_ChangeInRevenueMonth) #Calculate Average change in revenue
print(f"Average Change: {AverageChange}")                          #Print Average Change value - variable hange'


GreatestIncrease = df['RevenueChange'].max()                                            #Calculate GreatestIncrease on column 'RevenueChange'
GreatestIncreaseDate = df.loc[df['RevenueChange'] == GreatestIncrease, 'Date'].iloc[0]  #Locate Greatest Increase Date in column 'Date'
GreatestIncrease = "${:,.2f}".format(GreatestIncrease)                                  #Format value of 'GreatestIncrease' to 2 decimals
print(f"Greatest Increase in Profits: {GreatestIncreaseDate} ({GreatestIncrease})")     #Print to terminal - GreatestIncreaseDate, GreatestIncrease

GreatestDecrease = df['RevenueChange'].min()                                            #Calculate GreatestDecrease on column 'RevenueChange'
GreatestDecreaseDate = df.loc[df['RevenueChange'] == GreatestDecrease, 'Date'].iloc[0]  #Locate GreatestDecrease Date in column 'Date'
GreatestDecrease = "${:,.2f}". format(GreatestDecrease)                                 #Format value of 'GreatestDecrease' to 2 decimals
print(f"Greatest Decrease in Profits: {GreatestDecreaseDate} ({GreatestDecrease})")     #Print to terminal - GreatestDecreaseDate, GreatestDecrease

#Write the results to file - Analysis_output.txt
with open(outFile, 'w') as outFile:
    outFile.write("                  Financial Analysis\n")
    outFile.write("                   02-Python-PyBank\n")
    outFile.write("                 --------------------\n")
    outFile.write("\n")
    outFile.write("\n")
    outFile.write("Total Months: %d" % TotalMonth + "\n")
    outFile.write("Total Revenue: %s" % total + "\n")
    outFile.write("Average Change: %s" % AverageChange + "\n")
    outFile.write("Greatest Increase in Profits: %s" % (GreatestIncreaseDate) + " %s" %(GreatestIncrease) + "\n")
    outFile.write("Greatest Decrease in Profits: %s" % (GreatestDecreaseDate) + " %s" %(GreatestDecrease) + "\n")
    outFile.write("\n")
    outFile.write("\n")
    outFile.write(" * * * * * * E N D  O F  R E P O R T * * * * * *\n")

# Close the open file
outFile.close()