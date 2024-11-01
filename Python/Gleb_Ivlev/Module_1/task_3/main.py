import string
symbols = string.printable
lst = []
for x in symbols:
    for y in symbols:
        for z in symbols:
            lst.append(f'{x}{y}{z}')
with open('gen_pas.txt', 'w') as f:
    f.write('\n'.join(lst))