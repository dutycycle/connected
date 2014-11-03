import random

def erdos_renyi(nodes, density):
  connections = []
  for i in range(0,nodes):
    for j in range(0,nodes):
      if i != j and (j,i) not in connections:
        if random.uniform(0,1) < density:
          connections.append((i,j))
  return connections

print len(erdos_renyi(50,0))
print len(erdos_renyi(50,.5))
print len(erdos_renyi(50,1))

