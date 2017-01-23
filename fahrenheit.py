fahrenheit = float(input("Enter: "))

print("Fahrenheit Celsius")

while fahrenheit <= 250:
    celsius = (fahrenheit - 32) / 1.8
    print("{:5f} {:7.2f}".format(fahrenheit, celsius))
    fahrenheit = fahrenheit + 25
