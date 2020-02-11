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
            temp.append(char)
            temp.append(char)
        output.append(''.join(temp))
        output.append(''.join(temp))
    return output


def find_longest_length(string):
    pass
