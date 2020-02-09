def fizz_buzz(begin: int, end: int):
    result = []
    while begin < end:
        if begin % 3 == 0 and begin % 5 == 0:
            result.append('FizzBuzz')
        elif begin % 3 == 0:
            result.append('Fizz')
        elif begin % 5 == 0:
            result.append('Buzz')
        else:
            result.append(str(begin))
        begin += 1
    return ' '.join(result)

print(fizz_buzz(11, 20))