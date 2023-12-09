"""
In this little assignment you are given a
string of space separated numbers, and have to return the highest and lowest number.
"""

def high_and_low(numbers):
    max_num = max(list(map(int, numbers.split())))
    min_num = min(list(map(int, numbers.split())))

    return f"{max_num} {min_num}"

print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))
