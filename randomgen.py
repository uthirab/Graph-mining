from random import sample
from itertools import islice

no_cities=int(input("Enter the number of cities "))
airlines= input("Enter the airlies you wanted to take(Delta,American, Frontier, Alligent, Southwest, Spirit)")
airlineslist=airlines.split(',')

city_list=open(airlineslist[0]+'.txt','r')
cityno = [next(city_list) for x in range(2)]
city = list(islice(city_list, int(cityno[0])))
random_city=sample(city,k=no_cities)
random_city1, connection1=[], []
for x in random_city:
    random_city1.append(x.strip('\n'))
random_city1.sort()
print(random_city1)
for file_path in airlineslist:            # loop to read each txt file
    with open(file_path + '.txt', 'r') as airline_file:
        tempcityno = [next(airline_file) for x in range(2)]
        tempcity = list(islice(airline_file, int(tempcityno[0])))
        connection = list(islice(airline_file, int(tempcityno[1])))
        for x in range(len(connection)):
            connection1.append(connection[x].lower())
        print(connection1)
        connection_list, index_connection = [], []
        for x in connection1:
            e = x.rstrip()
            r = e.split(' - ')
            if r[0] in random_city1 and r[1] in random_city1:
                connection_list.append(x)
                indes_r0 = random_city1.index(r[0])
                indes_r1 = random_city1.index(r[1])
                w = (str(indes_r0) + "," + str(indes_r1) + ',1.0')
                index_connection.append(w)
        file = open(file_path+'index'+'.txt', 'w')
        file.write(file_path+'\n')
        file.write((str(len(random_city1)))+'\n')
        file.write((str(len(connection_list)))+'\n')
        for x in range(len(random_city1)):
            print(x)
            file.write("%d\n" %x)
        for x in index_connection:
            print(x)
            file.write("%s\n" %x)
        #print(connection_list)
        #print(index_connection)



#
 #   with open(file_path+'.txt', 'r') as airline_file:
