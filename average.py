N = 10
sum = 0
count = 0

number = float(input("Enter:"));

while count < N:
    sum = sum + number
    count = count + 1

average = sum / N
print("N = {}, Sum = {}".format(N, sum))
print("Average = {:.2f}".format(average))
