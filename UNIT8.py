import json

# 3 new items
newitem1 = 8
newitem2 = 9
newitem3 = 10
# gematria key dictionary
apple = {
    1: ('a', 'm', 'n', 'z'),
    2: ('b', 'l', 'o', 'y'),
    3: ('c', 'k', 'p', 'x'),
    4: ('d', 'j', 'q', 'w'),
    5: ('e', 'i', 'v', 'r'),
    6: ('f', 'h', 's', 'u'),
    7: ('g', 't'),
    newitem1: ('rewind', 'forward'),
    newitem2: ('play', 'pause'),
    newitem3: ('stop', 'start')
}
# format dictionary into text string in input file
with open('original.txt', 'w') as gematriatext:
    json.dump(apple, gematriatext)
# convert input string into dictionary item
with open('original.txt', 'r') as gematriatext:
    string_input_to_dict = json.load(gematriatext)
    print(string_input_to_dict)


def gematriakey(name):
    # inverse function
    def invert_dict(d):
        inverse = dict()
        for key in d:
            val = d[key]
            for i in val:
                if i not in inverse:
                    inverse[i] = [key]
                else:
                    inverse[i].append(key)
        return inverse

    invertlist = invert_dict(string_input_to_dict)
    # Format each item in inverted dictionary as text string
    with open('inverted.txt', 'w') as gematriainverted:
        json.dump(invertlist, gematriainverted)
    mynumber = 0
    # this adds the gematric value of each letter to 'mynumber'
    for i in name:
        addit = invertlist[i][0]
        mynumber += int(addit)
    return mynumber


print(gematriakey('vincent'))
