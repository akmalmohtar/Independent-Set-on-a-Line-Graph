import random
#main function
# n is the number of vertices
# weights is a list of their weights, v_1, ..., v_n
def mwis (n, weights):
 
 #create array opt 
 opt = [0]*(n)
 
 #opt[0] = weights[0] #empty line set
 #opt[1] = max(weights[0], weights[1])
 
 opt[0] = weights[0]
 opt[1] = max(weights[0], weights[1])
 
 #compute maximum total weight
 for i in range(2, n):
  opt[i] = max( weights[i] + opt[i-2], opt[i-1])
 
 sol_tot_weight = opt[n-1]
 
 
 #compute solution indexes
 sol_items = []
 i = n-1
 while(i >= 0):
  if i == 0:
   sol_items.insert(0,i)
   break
  if (weights[i] + opt[i-2] >= opt[i-1]):
   sol_items.insert(0,i)
   i -= 2
  else:
   i -= 1
  
  #sol_items = sorted(sol_items)
  #sol_items.pop()
    
 return (opt, sol_tot_weight, sorted(sol_items))

"""
weights = [49, 100 , 3, 99, 2]
n = len(weights)
"""

#YOU DO NOT NEED TO CHANGE THE CODE BELOW THIS LINE    

#Read input

f = open("input.txt", "r")
weights = [int(x) for x in f.readline().split()] 
n = len (weights)

#call mwis
(opt, sol_tot_weight, sol_items) = mwis(n, weights)

#output solution
print ' '.join(map(str, opt))
print sol_tot_weight
print ' '.join(map(str, sol_items))
