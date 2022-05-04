#
# dump 10 random number [1,10]
#
import pickle
import random
dump = []

for i in range(0,9):
    dump.append(random.randint(1,10))

with open('list.bin','wb') as fh:
    pickle.dump(dump,fh)

print('done...')
