import time

numbers = [3, 1, 4, 1, 5, False, "This is PI"]
print(str(numbers[0]))
print(str(numbers[1]))
print(str(numbers[2]))
print(str(numbers[3]))
print(str(numbers[4]))

time.sleep(1)
print(numbers[6] + "?")
print(numbers[5])


numbers.append(6);
print(len(numbers))
print("\nCounting ones: " + str(numbers.count(1)))

coordinates = (1,2)
print("\nPrinting touples now: " + str(coordinates[0]) + "," + str(coordinates[1]))
