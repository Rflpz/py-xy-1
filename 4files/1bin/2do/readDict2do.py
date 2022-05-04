#
# 2do
#

import pickle

with open('dictionary.bin','rb') as fh:
    dictionary = pickle.load(fh)
    print(dictionary)