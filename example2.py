i = int(raw_input('净利润:'))
arr = [10000000, 6000000, 4000000, 2000000, 1000000, 0]
rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
r = 0

for idx in range(0, 6):
    if i > arr[idx]:
        r = r + (i - arr[idx]) * rat[idx]
        print (i - arr[idx]) * rat[idx]
        i = arr[idx]
print r