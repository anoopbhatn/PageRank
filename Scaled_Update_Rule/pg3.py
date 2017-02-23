# Page rank implementation without Equilibrium and Scaling

from datagen import node_list,graph

# Initialize the nodes to 1/n
def init_nodes():
	l=[(1/float(len(node_list))) for i in range(len(node_list))]
	return l  


# Calculate number of children for j
def calc_child(row):
	child=0
	for i in range(len(node_list)):
		 if graph[row][i]==1:
		 	child+=1
	return child


# Compute fractions for kth step
def compute(prev):
	l=[0]*len(node_list)

	visit=[0]*len(node_list)

	# Traverse all nodes and update the fraction
	for i in range(len(node_list)):
		if visit[i]==1:
			continue
		for j in range(len(node_list)):
			# Number of children for j
			child=calc_child(j)
			for k in range(len(node_list)):
				# If j reaches k
				if graph[j][k]==1:
					visit[j]=1
					visit[k]=1
					# add the fraction at j to k 
					l[k]+=(prev[j]/float(child))

	# return the list l with updated fractions to the caller
	return l

# Compute fractions for k-steps
def compute_k(prev):
	while True:
		res=compute(prev)
		for i in range(len(res)):
			res[i]=round(res[i],3)
		if res==prev:
			return res
		prev=res

prev=init_nodes()
# Find basic pagerank
result=compute_k(prev)

# Scaling factor
scale=0.8
for i in range(len(result)):
	# Distribute page rank uniformly using scaling factor 
	result[i]=round((result[i]*scale)+((1-scale)/len(result)),3)

print 'The Page Rank values for the nodes : ( Node : Page Rank Value )'

for i in range(len(result)):
	print node_list[i],'\t - \t',result[i]