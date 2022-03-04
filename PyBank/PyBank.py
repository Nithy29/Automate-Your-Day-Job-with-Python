# imports files
import pandas as pd

# set the output of the text file
text_path = "C:/GitBash/python-homework/PyBank/Analysis_output.txt"

# read the csv file into variable df
df = pd.read_csv("C:/GitBash/python-homework/PyBank/budget_data.csv", delimiter=',')

TotalMonth = df['Profit/Losses'].count()                           #Calculate Total month 
print(f"Total Months: {TotalMonth}")

total = "${:,.2f}". format(df['Profit/Losses'].sum())              #Calculate Total revenue
print(f"Total: {total}")

df['RevenueChange'] = df['Profit/Losses'].diff()                   #Calculate Rev difference column
TotalChangeRevenue = (df['RevenueChange'].sum())                   #Calculate Total Rev Difference
AverageChange = "${:,.2f}". format(totalChangeRevenue/TotalMonth)  #Calculate Total Rev Chg Avag
print(f"Average Change: {AverageChange}")

GreatestIncrease = df['RevenueChange'].max()                                            #Calculate GreatestIncrease
GreatestIncreaseDate = df.loc[df['RevenueChange'] == GreatestIncrease, 'Date'].iloc[0]  #Greatest Increase Date
GreatestIncrease = "${:,.2f}". format(GreatestIncrease)                                 #Format to currency
print(f"Greatest Increase in Profits: {GreatestIncreaseDate} ({GreatestIncrease})")

GreatestDecrease = df['RevenueChange'].min()                                            #Calculate Greatest Decrease
GreatestDecreaseDate = df.loc[df['RevenueChange'] == GreatestDecrease, 'Date'].iloc[0]  #Greatest Decrease Date
GreatestDecrease = "${:,.2f}". format(GreatestDecrease)                                 #Format to currency
print(f"Greatest Decrease in Profits: {GreatestDecreaseDate} ({GreatestDecrease})")

#Write the results to file - Analysis_output.txt
with open(text_path, 'w') as outFile:
    outFile.write("                  Financial Analysis\n")
    outFile.write("                   02-Python-PyBank\n")
    outFile.write("                  ---------------------\n")
    outFile.write("\n")
    outFile.write("\n")
    outFile.write("Total Months: %d" % TotalMonth + "\n")
    outFile.write("Total Revenue: %s" % total + "\n")
    outFile.write("Average Change: %s" % AverageChange + "\n")
    outFile.write("Greatest Increase in Profits: %s%s" % (GreatestIncreaseDate, GreatestIncrease) + "\n")
    outFile.write("Greatest Decrease in Profits: %s%s" % (GreatestDecreaseDate, GreatestDecrease) + "\n")
    outFile.write("\n")
    outFile.write("\n")
    outFile.write(" * * * * * * E N D  O F  R E P O R T * * * * * *\n")

# Close the open file
outFile.close()
