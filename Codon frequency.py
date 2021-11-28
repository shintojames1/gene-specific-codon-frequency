import re
import itertools

sequences = []

# path to .fna file
file_path = 'E:/ecoli.fna'

with open(file_path, 'r') as ecoli:
    sequence = ''
    for line in ecoli:
        if line.startswith('>'):
            sequences.append(sequence)
            sequence = ''
        else:
            sequence += line.strip()
sequences.pop(0)

pos = 0
for x in sequences:
    b = [_.start() for _ in re.finditer("TCA", x)]
    c = [_.start() for _ in re.finditer("TTA", x)]
    d = [_.start() for _ in re.finditer("CTA", x)]
    bcd = b+c+d
    
    for y in bcd:
        if y % 3 == 0:
            pos += 1
            break
    if x  ==  sequences[-1]:
        print (pos, len (sequences))
        print (pos/len(sequences))
