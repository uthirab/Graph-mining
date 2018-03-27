from itertools import islice
city1, connection1, Acity1,Aconnection1, AAcity1, AAconnection1, Dcity1, Dconnection1, Fcity1, Fconnection1, Scity1, Sconnection1 =[], [], [], [], [], [], [], [], [], [], [], []

spirit=open("spirit_aitlines.txt", 'r')
cityno = [next(spirit) for x in range(2)]
city = list(islice(spirit, int(cityno[0])))
connection = list(islice(spirit, int(cityno[1])))
for x in range(len(city)):
    city1.append(city[x].lower())
for x in range(len(connection)):
    connection1.append(connection[x].lower())

Alligent=open("Alligent_airlines.txt",'r')
Acityno = [next(Alligent) for x in range(2)]
Acity = list(islice(Alligent, int(Acityno[0])))
Aconnection = list(islice(Alligent, int(Acityno[1])))
for x in range(len(Acity)):
    Acity1.append(Acity[x].lower())
for x in range(len(Aconnection)):
    Aconnection1.append(Aconnection[x].lower())

American_airlines=open("AmericanAirline - Dataset.txt",'r')
AAcityno = [next(American_airlines) for x in range(2)]
AAcity = list(islice(American_airlines, int(AAcityno[0])))
AAconnection = list(islice(American_airlines, int(AAcityno[1])))
for x in range(len(AAcity)):
    AAcity1.append(AAcity[x].lower())
for x in range(len(Aconnection)):
    AAconnection1.append(Aconnection[x].lower())

Delta=open("Delta.txt", 'r')
Dcityno = [next(Delta) for x in range(2)]
Dcity = list(islice(Delta, int(Dcityno[0])))
Dconnection = list(islice(Delta, int(Dcityno[1])))
for x in range(len(Dcity)):
    Dcity1.append(Dcity[x].lower())
for x in range(len(Dconnection)):
    Dconnection1.append(Dconnection[x].lower())

Frontier=open("Frontier-Dataset.txt", 'r')
Fcityno = [next(Frontier) for x in range(2)]
Fcity = list(islice(Frontier, int(Fcityno[0])))
Fconnection = list(islice(Frontier, int(Fcityno[1])))
for x in range(len(Fcity)):
    Fcity1.append(Fcity[x].lower())
for x in range(len(Fconnection)):
    Fconnection1.append(Fconnection[x].lower())


South=open("Southwest.txt", 'r')
Scityno = [next(South) for x in range(2)]
Scity = list(islice(South, int(Scityno[0])))
Sconnection = list(islice(South, int(Scityno[1])))
for x in range(len(Scity)):
    Scity1.append(Scity[x].lower())
for x in range(len(Sconnection)):
    Sconnection1.append(Sconnection[x].lower())

Newlist = city1 + Acity1 + Fcity1 + AAcity1 + Scity1 + Dcity1
newlist_sorted=sorted(set(Newlist))
file=open('new.txt','w')

id_list1, total_city_list=[], []
for i in range(len(newlist_sorted)):
    idlist1 = (newlist_sorted[i])
    id_list1.append(idlist1)
for items in id_list1:
   file.write('%s' %items)


