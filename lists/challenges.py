def hamming_weight(number: int) -> int:
    return bin(number).count('1')


def hamming_weight_gen(number: int) -> int:
    return sum(int(i) for i in bin(number)[2:])


def compare_version(v1, v2):
    l1 = [int(i) for i in v1.split('.')]
    l2 = [int(i) for i in v2.split('.')]
    if l1 > l2:
        return 1
    elif l1 < l2:
        return -1
    return 0


def is_continuous_sequence(sequence):
    if len(sequence) < 2:
        return False
    for index, element in enumerate(sequence, start=sequence[0]):
        if index != element:
            return False
    return True


def length_of_last_word(sentence):
    words = sentence.split()
    if not words:
        return 0
    return len(words[-1])


def same_parity_filter(sequence):
    if not sequence:
        return []

    rest = sequence[0] % 2
    return [element for element in sequence if element % 2 == rest]


def chunked(step, sequence):
    output = []
    for i in range(0, len(sequence), step):
        output.append(sequence[i:i+step])
    return output


def show(image):
    for line in image:
        print(line)


def enlarge(items):
    output = []
    for string in items:
        temp = []
        for char in string:
            temp.extend([char, char])
        string = ''.join(temp)
        output.extend([string, string])
    return output


def find_longest_length(string):
    output = []
    for index, _ in enumerate(string):
        substring = ''
        for char in string[index:]:
            if char in substring:
                output.append(len(substring))
                substring = char
                continue
            substring += char
        output.append(len(substring))
    return max(output)


def transposed(matrix):
    if not len(matrix):
        return []
    count_columns = len(matrix)
    count_rows = len(matrix[0])
    res = [[0] * count_columns for _ in range(count_rows)]

    for index_row, row in enumerate(matrix):
        for index_col, col in enumerate(row):
            res[index_col][index_row] = col
    return res


def triangle(count_rows):
    prev = [1]
    if count_rows == 0:
        return prev

    while count_rows != 0:
        res = [1]
        for index, element in enumerate(prev[:-1], start=1):
            res.append(element + prev[index])
        res.append(1)
        prev = res
        count_rows -= 1
    return prev


def summary_ranges(l):
    if len(l) < 2:
        return []

    start = l[0]
    stop = l[len(l)-1]
    flag = False
    res = []
    for i, element in enumerate(l[:-1], start=1):
        if l[i] - element != 1:
            if element == stop:
                start = l[i]
                continue
            res.append(f'{start}->{element}')
            start = stop = l[i]
            flag = True
    else:
        if not flag:
            res.append(f'{start}->{stop}')
    return res

print(summary_ranges([110, 111, 112, 111, -5, -4, -2, -3, -4, -5]))