import sys
from cycfind import cyclic_search
OFFSET = 9
fName = "data.txt"
data_base = []
try:
    with open("data.txt", 'r') as f:
        for line in f:
            tup = tuple(line.strip().split(' '))
            data_base.append(tup)
except IOError:
    print("Could not read file:", fName)
    sys.exit()
else:
    f.close()

data_base.sort(key=lambda x: x[0])
test_base =data_base[:OFFSET] + data_base[OFFSET:]
names = [name[0] for name in data_base]


for query in names:
    print("Query: {0:7s} Answer: {1:10s}".format(query, cyclic_search(test_base, query)))

