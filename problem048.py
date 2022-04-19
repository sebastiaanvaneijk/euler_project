# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
#
# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

tot = 0
for i in range(1, 1001):
    tot += i**i

last_digits = str(tot)[-10:]
print(last_digits)
