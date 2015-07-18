# this snippet is to display simple series of fabonacci numbers

a, b = 0, 1
print a
print b
num = 10
for i in range(num):
    a, b = b, a + b
    print a
