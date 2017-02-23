import csv

f1=open("data.csv","r")
reader=csv.reader(f1, delimiter=',')

i=1
node_list=list()
graph=[]

for row in reader:
	if i==1:
		i+=1
		node_list=row
		continue
	graph.append([int(j) for j in row])
	
