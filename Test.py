'''
Program for testing and debugging
functions from Image_Processing.py
'''


from Image_Processing import establishThreshold
from Image_Processing import checkVariance

print('checkVariance() check #1: ', checkVariance((50, 60, 70), (55, 66, 77)))
print('checkVariance() check #2: ', checkVariance((50, 60, 70), (45, 54, 63)))
print('checkVariance() check #3: ', checkVariance((50, 60, 70), (51, 60, 70)))

li1 = [(46, 54, 63), (50, 60, 70), (50, 60, 70), (50, 60, 70)]
print('establishThreshold() check #1: ', establishThreshold(li1, (45, 54, 63)))

li2 = [(50, 60, 70), (50, 60, 70), (50, 60, 70), (50, 60, 70)]
print('establishThreshold() check #2: ', establishThreshold(li2, (45, 54, 63)))

li3 = [(69, 21, 52), (19, 20, 13), (99, 60, 70), (78, 60, 22)]
print('establishThreshold() check #3: ', establishThreshold(li2, (1, 1, 1)))