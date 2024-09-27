import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    flipList = []
    for flip in range(100):
        flip = random.randint(0, 1)
        if flip == 0:
            flip = 'H'
            flipList = flipList + [flip]
        elif flip == 1:
            flip = 'T'
            flipList = flipList + [flip]
# Code that checks if there is a streak of 6 heads or tails in a row.
tailCount = 0
headCount = 0
for i in flipList:
    if i == 'H':
        headCount += 1
        tailCount *= 0
        if headCount == 6:
            numberOfStreaks += 1
            headCount *= 0
        else:
            continue
    elif i =='T':
        tailCount += 1
        headCount *= 0
        if tailCount == 6:
            numberOfStreaks += 1
            tailCount *= 0
        else:
            continue
print('Chance of streak: %s%%' % (numberOfStreaks / 100))
