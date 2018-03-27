from itertools import islice
import os
city1, connection1, cities, connections=[], [], [], []

text_files = [f for f in os.listdir() if f.endswith('.txt')]#gets all txt files in directory
for file_path in text_files:#loop to read each txt file
    with open(file_path, 'r') as f_input:
        cityno = [next(f_input) for x in range(2)] #gets first two values: city, connection values
        city = list(islice(f_input, int(cityno[0]))) #gets all cities
        city1 = [c.lower().rstrip() for c in city] #in city list: remove new line and convert to lower case
        connection = list(islice(f_input, int(cityno[1])))#gets all connections
        connection1 = [c.lower().rstrip() for c in connection]#in connnection list: remove new line and convert to lower case
        cities.append(city1)#append to list of cities
        connections.append(connection1)#append to list of connections


Newlist = sorted(set().union(*cities))#Create a set of unique cities by taking union and sorting alphabetically
print(Newlist)
file=open('new.txt','w')#create a new file named new.txt
for items in Newlist:
    file.write('%s\n' %items)
print(len(Newlist))