import time

numbers = [3, 1, 4, 1, 5, False, "This is PI"]
print(numbers)

time.sleep(1)
print(numbers[1])
print(numbers[6] + "?")
print(numbers[5])


numbers.append(6);
print(len(numbers))
print("\nCounting ones: " +str(numbers.count(1)))

coordinates = (1,2)
print("\nPrinting touples now: " + str(coordinates[0]) + "," + str(coordinates[1]))
