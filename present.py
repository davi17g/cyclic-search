"""
This an example module that demonstrates the use of the cyclic search on data that is included with
with the project.
"""

import sys
from cycfind import cyclic_search
OFFSET = 9
fName = "data.txt"
data_base = []

# Data is loaded from the text file.
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


# Data is sorted and special list with an arbitrary offset is created.
data_base.sort(key=lambda x: x[0])
test_base = data_base[:OFFSET] + data_base[OFFSET:]
# This list is used for querying an existing data.
names = [name[0] for name in data_base]
names.append('Something')  # Example for query that is not in data set.


for query in names:
    try:
        result = cyclic_search(test_base, query)
        print("Query: {0:10s} Answer: {1:10s}".format(query, result))
    except NameError as e:
        print(e.args)

