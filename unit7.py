alphabet = "abcdefghijklmnopqrstuvwxyz"
test_dups = ["zzz","dog","bookkeeper","subdermatoglyphic","subdermatoglyphics"]
test_miss = ["zzz","subdermatoglyphic","the quick brown fox jumps over the lazy dog"]
def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d
def has_duplicates(b):
    for key, value in b.items():
        if value > 1:
            return True
        else:
            pass
    return False
    return has_duplicates()
for i in test_dups:
    if has_duplicates(histogram(i)) == True:
        print(f'{i} has duplicates')
    else:
        print(f'{i} has no duplicates')
print('PART 2 -------------------------------------')
print('PART 2 -------------------------------------')
print('PART 2 -------------------------------------')
def missing_letters(runit):
    alphadict = histogram(alphabet)
    missing = ()
    for i in runit:
        for key, value in alphadict.items():
            if key == i:
                alphadict[i] += 1
    for key, value in alphadict.items():
        if value > 1:
            pass
        else:
            missing += key,
    return ''.join(missing)
for i in test_miss:
    whatmissing = missing_letters(i)
    if whatmissing == '':
        print(f'{i} uses all the letters')
    else:
        print(f'{i} is missing letters {whatmissing}')