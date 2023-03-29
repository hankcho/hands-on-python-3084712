NAMES = ("Henry", "John", "Brian", "Claire")
AGES = (10, 20, 30, 40)

HENRY = NAMES[0]
JOHN = NAMES[1]

HENRY_JOHN = NAMES[:2]
BRIAN_CLAIRE = NAMES[2:]
# REVERSE = NAMES[star:stop:step-1]
REVERSE = NAMES[::-1]
EVERY_OTHER = NAMES[::2]

print(sum(AGES))
print(min(AGES))
print(max(AGES))

print(HENRY_JOHN)
print(BRIAN_CLAIRE)
print(REVERSE)
print(EVERY_OTHER)
