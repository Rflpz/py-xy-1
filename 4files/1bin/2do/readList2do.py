#
# load bin file
# calculate
#   sum
#   avg
#   mode
import pickle

with open('list.bin','rb') as fh:
    dumpList = pickle.load(fh)
    print("List " + str(dumpList))
    sum = 0
    mode = 0
    for item in dumpList:
        sum += item
    print("Sum: " + str(sum))
    print("Avg: " + str(sum / len(dumpList)))
    print("Mode: " + str(max(set(dumpList), key = dumpList.count)))