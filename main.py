from LongComparison import LongComparison
from LongNumber import LongNumber

a = LongNumber('1287')
b = LongNumber('447')
m = LongNumber('516')
print(LongComparison(a,b,m).solve()[0])
print(LongNumber.GCD(a,b))