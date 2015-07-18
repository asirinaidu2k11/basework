# this code will return the series of fabonacci nubers to the called function

def series_fibonacci(number):
    a, b = 0, 1
    series = []
    series.append(a)
    series.append(b)
    for num in range(number):
        a, b = b, a + b
        series.append(a)
    return series

if __name__ == "__main__":
    number = input('Please enter numer for you want fibonacci')
    result = series_fibonacci(number)
    for value in result:
        print value
