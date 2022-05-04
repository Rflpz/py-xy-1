#
# 2do
#
import pickle

dictionary = {'one':'aaa aaa', 'two':'bbb bbb', 'three':'ccc ccc'}

with open('dictionary.bin', 'wb') as fh:
    pickle.dump(dictionary, fh)

print('done...')
