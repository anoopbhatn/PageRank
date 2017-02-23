# Page rank implementation using Equilibrium values of PageRank

from datagen import node_list,graph

# Calculate number of children for j
def calc_child(row):
	child=0
	for i in range(len(node_list)):
		 if graph[row][i]==1:
		 	child+=1
	return child


def compute():
	l=[0]*len(node_list)

	visit=[0]*len(node_list)

	l[0]=1
	visit[0]=1
	parent=[0]*len(l)
	# Traverse all nodes and update the fraction
	for i in range(len(node_list)):
		if visit[i]==1:
			continue
		for j in range(len(node_list)):
			# Number of children for j
			child=calc_child(j)
			for k in range(len(node_list)):
				# If j reaches k
				if graph[j][k]==1 and k!=0:
					visit[j]=1
					visit[k]=1
					parent[j]=1
					# add the fraction at j to k 
					l[k]+=(l[j]/float(child))
					
					# If the parent had already divided its rank score
					if parent[k]==1:
						# Number of children for j
						child1=calc_child(k)
						# For every child of such parent,redistribute newly added page rank score
						for m in range(len(l)):
							if graph[k][m]==1:
								# Only add newly added score divided by number of its children
								l[m]+=(l[j]/float(child))/child1
	# add up all the fractions and equate to 1
	# x+(fraction(x))+...=1
	s=0
	for i in l:
		s+=i

	# fraction*x=1 ; Hence, x=1/fraction
	x=1/s

	res=[0]*len(l)
	# Find the pagerank values for all, substituting value for x
	for i in range(len(l)):
		res[i]=l[i]*x

	# return the list l with updated fractions to the caller
	return res

result=compute()

print 'The Page Rank values for the nodes : ( Node : Page Rank Value )'

for i in range(len(result)):
	print node_list[i],'\t - \t',result[i]