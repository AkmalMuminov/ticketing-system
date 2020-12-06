import datetime
x = [(1, 'test2', '2', datetime.date(2020, 12, 2), 'closed'), (2, 'test1', '1', datetime.date(2020, 11, 2), 'closed')]

newList = []
n=3#index of datetime
for i in x:
        a = list(i) #convert to list
        b = a.pop(n) #remove datetime element
        a.insert(n,b.strftime('%m/%d/%Y')) #put str date
        newList.append(a)
print(newList)

newList=tuple(newList)
print (newList)

    
