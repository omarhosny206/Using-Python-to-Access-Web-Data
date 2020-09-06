import re

data_file = open(
    r'E:\omarHosnyKeshk\Python for Everybody Specialization\_3 Using Python to Access Web Data\Week 2\Programming Assignments\regex_sum_913788.txt'
)
sum = 0
count = 0

for line in data_file:
    line = line.rstrip()
    numbers = re.findall('[0-9]+', line)
    for number in numbers:
        sum += int(number)
        count += 1

print('There are ', count, ' values with a sum=', sum)
