def to_rna(dna):
    d = {
        'G': 'C',
        'C': 'G',
        'T': 'A',
        'A': 'U',
    }

    res = []
    for i in dna:
        res.append(d.get(i))
    return ''.join(res)


def build_query_string(query_string):
    res = []
    for param, val in sorted(query_string.items()):
        res.append(f'{param}={val}')
    return '&'.join(res)

print(build_query_string({'per': 10, 'page': 1}))