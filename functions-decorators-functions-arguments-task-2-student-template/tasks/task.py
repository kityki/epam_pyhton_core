def union(*args) -> set:
    res = [list(i) for i in args]
    jojo = []
    for l in res:
        for item in l:
            jojo.append(item)
    return set(jojo)


print(union(('S', 'A', 'M'), ['S', 'P', 'A', 'C']))

def intersect(*args) -> set:
    result = set.intersection(*map(set, args))
    return result

print(intersect({'S', 'C', 'A'}, {'P', 'S', 'C'}, {'H', 'G', 'S', 'C'}))