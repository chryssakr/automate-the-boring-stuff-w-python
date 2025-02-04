# A short program counting the number of occurences of each letter
import pprint

message = "It was a bright cold day in April, and the clocks were striking thirteen."

count: dict[str, int] = {}
for character in message:
    count.setdefault(character, 0)
    count[character] += 1
pprint.pprint(count)
