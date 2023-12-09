"""Return the number (count) of vowels in the given string."""

def get_count(sentence):
    num = 0
    for char in sentence:
        if char in "aeiou":
            num += 1

    return num

print(get_count("hello"))

res = get_count("hello")
assert res, 2
