import csv
lst = []
def cheapest(data,c):
    if c == 'cost':
        min_data = min(data,key=lambda x:x[3])
        return min_data
    elif c == 'rating':
        min_data = min(data,key=lambda x:x[4])
        return min_data
def highest(data,c):
    if c == 'cost':
         max_data = max(data,key=lambda x:x[3])
         return max_data
    elif c == 'rating':
         max_data = max(data,key=lambda x:x[4])
         return max_data
def avg_fun(data,c):
    if c == 'cost':
        ave = round(sum([i[3] for i in data])/len(data),1)
        return ave
    if c == 'rating':
        ave = round(sum([i[4] for i in data])/len(data),1)
        return ave

with open('hotels.csv','r') as ifile:
    dataReader = csv.reader(ifile)
    next(dataReader)
    for n in dataReader:
        n[3] = int(n[3])
        n[4] = float(n[4])
        lst.append(n)
        
        
state = input('\nWhat is the state: \n')
cost = input('\nCost or Rating: \n')
option = input('\nOperation: \n')

data_r =[x for x in lst if state in x]
if cost == 'cost':
    if option == 'cheapest':
        cheap = cheapest(data_r,cost)
        print('\nHotel with cheapest price in '+state+' is '+str(cheap[1])+' with price '+str(cheap[3]))
    elif option == 'highest':
        high = highest(data_r,cost)
        print('\nHotel with highest price in '+state+' is '+str(high[1])+' with price '+str(high[3])) 
    elif option == 'average':
        avrg = avg_fun(data_r,cost)
        print('\nAverage price of Hotel in '+state+' is '+str(avrg))
elif cost == 'rating':
    if option == 'cheapest':
        cheap_r = cheapest(data_r,cost)
        print('\nHotel with cheapest rating in '+state+' is '+str(cheap_r[1])+' with rating '+str(cheap_r[4]))
    elif option == 'highest':
        high_r = highest(data_r,cost)
        print('\nHotel with highest rating in '+state+' is '+str(high_r[1])+' with rating '+str(high_r[4]))
    elif option == 'average':
        avrg_r = avg_fun(data_r,cost)
        print('\nAverage rating of Hotel in '+state+' is '+str(avrg_r))
