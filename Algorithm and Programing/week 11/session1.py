import csv 
import statistics as st
import pygal
import matplotlib.pyplot as plt

'''reader = csv.reader("activity.csv")

print(next(reader)) '''

filename = "activity.csv"

with open(filename) as f:
    reader = csv.reader(f)
    headerRow = next(reader)


# getting the number of steps per day , 0 1 2 for steps, date, interval

    dictDate = {}
    dictInterval = {}

#variable to store number of steps/day 
    for row in reader:
        steps = row [0]
        if steps != 'NA': 
            date = row[1]
            interval = int(row[2])

            dictDate.setdefault(str(date),[]) # update a value in a kaey, if the key does not exsist --> create a key 
            dictDate[str(date)].append(int(steps))

            dictInterval.setdefault(interval,[])
            dictInterval[interval].append(int(steps))

#number of steps per day

listDate = []
listTotal = []

for i in dictDate.keys():
    listDate.append(i)
    listTotal.append(sum(dictDate.get(i)))

print(" ")
print(f'{listDate}:{listTotal}')

dictTotalSteps = {}
for i in dictDate.keys():
    dictTotalSteps.setdefault(str(date),0)
    dictTotalSteps[str(date)] = sum(dictDate.get(i))

print(" ")
print(dictTotalSteps)

#calculate the mean and median of steps 

#mean 
print(f"Mean : {st.mean(listTotal)}")

#median

q = sorted(listTotal)
print(f"Median : {st.median(q)}")

hist = pygal.Bar()
hist.title = "total steps per day"
hist.x_title = "steps per day"
hist.y_title = "frequency"
hist.x_labels = listDate
hist.add("Total number of steps", listTotal)
hist.render_to_file("StepsPerDay.svg")

'''
make a time series plot of the 5 minute interval (x-axis) and the average number of steps taken, 
averaged across all days (y-axis)
'''

listAvePerInterval = []
for i in dictInterval.keys():
    listAvePerInterval.append(st.mean(dictInterval.get(i)))

plt.plot(list(dictInterval.keys()),listAvePerInterval)
plt.title("average daily activity")
plt.xlabel("time interval")
plt.ylabel("average number of steps taken")
plt.show()


'''
which 5 minute interval, on average across all the days in the dataset, contains the maximum number of steps?
'''

n = 0
maxValue = max(listAvePerInterval)
indexMax = listAvePerInterval.index(maxValue)

for i in dictInterval.keys():
    if n == indexMax:
        max = i 
        break
    n+=1

print(" ")
print(f"maximum number of steps in interval {max}")