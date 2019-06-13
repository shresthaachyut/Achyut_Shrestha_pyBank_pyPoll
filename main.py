import pandas as pd

budgetData = pd.read_csv('budget_data.csv')
pollData = pd.read_csv('election_data.csv')
#--------------------------------------------------------------------------------------------------
months = budgetData['Date'].nunique()
total_PL = budgetData['Profit/Losses'].sum()
budgetData['change'] = budgetData['Profit/Losses'].diff() 
avgchg = round(budgetData['change'].mean(),2)

grtIncProfit = budgetData['change'].max()
grtIncProfitMonth = budgetData[budgetData['change'] == grtIncProfit].Date.max()

grtDecProfit = budgetData['change'].min()
grtDecProfitMonth = budgetData[budgetData['change'] == grtDecProfit].Date.min() 
#---------------------------------------------------------------------------------------------------
totalVotes = pollData['Voter ID'].count()
#totalVotes.summary()
print("Election Results")
print("----------------------")
print("Total Votes: " + str(totalVotes))
print("----------------------")















print("Financial Analysis")
print("-------------------------")
print("Total Months : " + str(months))
print("Total : $" + str(total_PL))
print("Average Change : $" + str(avgchg))
print("Greatest Increase in Profit : $" + str(grtIncProfitMonth) + " ($" + str(int(grtIncProfit)) + ")")
print("Greatest Decrease in Profit : $" + str(grtDecProfitMonth) + " ($" + str(int(grtDecProfit)) + ")")