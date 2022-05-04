#
# 2do
#
import pickle

with open('tuple.bin','rb') as fh:
    t = pickle.load(fh)
    print(t)