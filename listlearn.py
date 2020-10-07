'''stock_prices = [284,500,456,765,999]
print("Stock Prices =",stock_prices)
print(stock_prices[2])
stock_prices.insert(2,696) #arg1-> index arg2-> Value insert within array O(n) complexity
print(stock_prices[2])
print(stock_prices[3])'''

#apply  stock_prices.remaove(1)

'''
 Let us say your expense for every month are listed below,
    January - 2200
    February - 2350
    March - 2600
    April - 2130
    May - 2190

Create a list to store these monthly expenses and using that find out,

1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this
'''

# exp = [2200,2350,2600,2000,2190]
'''Soln a> 
exp = [2200,2350,2600,2130,2190]

def mtm(exp,month1,month2):
    print(exp[month1],exp[month2])
    return (exp[month1] - exp[month2])
# mtm(exp,0,1)    

print("The increase in expense = ",mtm(exp,1,0))    
'''
''' Soln b-->
def quatinc(exp):
    sum = 0
    for i in range(len(exp[0:3])):
        sum += exp[i] 
    return sum

print("The quarterly expense is =",quatinc(exp))        
'''
''' SOln c-->
def is2k(exp):
    for i in range(len(exp)):
        if exp[i] == 2000 :
            print("In the month",i,"exactly 2000 was spent")
        else:
            print("In the month",i,"exactly 2000 was not spent")
             
is2k(exp)
'''

# very easy soln -->
# print("Did i spen 2000$ in any month?",2000 in exp)
''' Soln d -->
exp.append(1980)
print("Monthly expenses in year",exp)
'''


'''Soln d --> 
def retitem(exp,month,amount):
    exp[month] = exp[month] - amount
    return exp

print("After return expenditure=",retitem(exp,3,200))    
'''

# heros=['spider man','thor','hulk','iron man','captain america']

'''
1. Length of the list
2. Add 'black panther' at the end of this list
3. You realize that you need to add 'black panther' after 'hulk',
   so remove it from the list first and then add it after 'hulk'
4. Now you don't like thor and hulk because they get angry easily :)
   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
   Do that with one line of code.
5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)

'''
'''Soln a-->
# print(len(heros)) 
'''
'''
Soln b-->
heros.append("black panther")
print(heros)

Soln c-->
# heros.pop(2) pop works with index passing 
heros.remove('black panther') # remove doesnot work with index passing 
print(heros)
heros.insert(3,'black panther')
print(heros)

Soln d-->
heros[1:3] = ['doctor strange']
print(heros)
'''

'''
print(dir())
dir() tries to return a valid list of attributes of the object it is called upon
For Class Objects, it returns a list of names of all the valid attributes and base attributes as well.
For Modules/Library objects, it tries to return a list of names of all the attributes, contained in that module.
If no parameters are passed it returns a list of names in the current local scope.
'''

'''Soln e-->
heros.sort()
print(heros)
'''
'''
#Question 3 begins:

max_number = int(input("Enter the max number:"))

odds = []

for i in range(max_number):
    if i%2 == 1 :
        odds.append(i)

print("Odd numbers from 1 to",max_number,"are as folows:",odds)        
'''