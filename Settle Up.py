#importing libraries to connect to Gsheet and write data
import gspread
from oauth2client.service_account import ServiceAccountCredentials

#to connect to respected APIs
scope = ["https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive"]

#passing credentials and authorising
credentials = ServiceAccountCredentials.from_json_keyfile_name('smksheet-da6f99763563.json',scope)
gc = gspread.authorize(credentials)

#opening sheet for operations
wks = gc.open("SettleTest").sheet1

#Here it is assumed that only one person is paying per payment made
#Variables to store the incoming expenses
Paid_1 = int((input("Person 1 Paid amount :- ")))
Paid_2 = int((input("Person 2 Paid amount :- ")))
Paid_3 = int((input("Person 3 Paid amount :- ")))
total_amount = int(Paid_1) + int(Paid_2) + int(Paid_3)
#print ('Total Amount :- %s' %total_amount)

#Amoung whom the expense is distributed
Paid_for_1 = input('Press Y/N depending upon was the expense paid for this person :- ').upper()
Paid_for_2 = input('Press Y/N depending upon was the expense paid for this person :- ').upper()
Paid_for_3 = input('Press Y/N depending upon was the expense paid for this person :- ').upper()
lst_paid = [Paid_for_1,Paid_for_2,Paid_for_3]
expnse_spread = lst_paid.count('Y')
#print (expnse_spread)
per_head_expense = (total_amount) / expnse_spread 
#print ('perHeadExpense')
#print (per_head_expense)

#variables to store amount amoung people

part_1 = 0
part_2 = 0
part_3 = 0
if (Paid_for_1 == 'Y'):
    part_1 = per_head_expense
if  (Paid_for_2 == 'Y'):
    part_2 = per_head_expense
if  (Paid_for_3 == 'Y'):
    part_3 = per_head_expense
#print('parts')
#print (part_1)
#print (part_2)
#print (part_3)
#variables to see balance per head for this transaction
bal_1 = 0
bal_2 = 0
bal_3 = 0

if (Paid_1 > 0 ):
    bal_1 = part_2 + part_3
    bal_2 = -(part_2)
    bal_3 = -(part_3)
    
elif (Paid_2 > 0 ):
    bal_2 = part_1 + part_3
    bal_1 = -(part_1)
    bal_3 = -(part_3)
else:
    bal_3 = part_2 + part_1
    bal_1 = -(part_1)
    bal_2 = -(part_2)
#print ('balance')
#print ('Balance for Person 1 : %d'%bal_1)
#print ('Balance for Person 2 : %d'%bal_2)
#print ('Balance for Person 1 : %d'%bal_3)

#inserting values to gsheet in respected order
wks.append_row([Paid_1,Paid_2,Paid_3,Paid_for_1,Paid_for_2,Paid_for_3,part_1,part_2,part_3,bal_1,bal_2,bal_3])