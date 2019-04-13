import os
import random
import re
import numpy as np
import re
import shutil

your_path_here = "path to dataset directory here"

topPath = your_path_here + "TSRD-Test"

newPath = your_path_here + "TSRD-TEST-SELECTED"

os.chdir(newPath)

## Find the 10 classes with most data in our training set to train them 
## separately
img_names = os.listdir()
classSet = set([28, 54, 3, 5, 55, 35, 7, 30, 16, 11])

freq = [0] * 100

for img in img_names:
    m = re.findall(r'[0-9]+', img)
    classNum = int(m[0])
    # print(img)
	## Code to move just the Classes we want out of the Testing Set of Data
    # if classNum in classSet:
    #     shutil.move(topPath + "/" + img, newPath + "/" + img)
    freq[classNum] = freq[classNum] + 1

# classSum = 0
# for i in classSet:
#     classSum = freq[i] + classSum
#     print("Class {} with Frequency {}".format(i, freq[i]))

# print("Total Files: ", classSum)

### Outputs:
# Class 3 with Frequency 84
# Class 35 with Frequency 46
# Class 5 with Frequency 50
# Class 7 with Frequency 50
# Class 11 with Frequency 130
# Class 16 with Frequency 76
# Class 54 with Frequency 176
# Class 55 with Frequency 58
# Class 28 with Frequency 68
# Class 30 with Frequency 34
# Total Files:  772

# Code to get the 10 most frequent classes. This was used in
# TSRD-Train to get the classes in the training set with the most
# dataset.

sortedFreq = [0] * 100
for i in range(len(freq)):
    sortedFreq[i] = (i, freq[i])

sortedFreq = sorted(sortedFreq, key = lambda x : x[1], reverse = True)

for i in range(10):
    print("Class {} with Frequency {}".format(sortedFreq[i][0], sortedFreq[i][1]))
# print(sortedFreq[:10])

# mostFreq = []
# for dataClass in sortedFreq[:10]:
#     mostFreq.append(dataClass[0])

# print(mostFreq)

### Outputs:
# Class 54 with Frequency 176
# Class 11 with Frequency 130
# Class 3 with Frequency 84
# Class 16 with Frequency 76
# Class 28 with Frequency 68
# Class 55 with Frequency 58
# Class 5 with Frequency 50
# Class 7 with Frequency 50
# Class 35 with Frequency 46
# Class 30 with Frequency 34