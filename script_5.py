import sys

from Bio.Seq import Seq

complementary = {
    'A':'T',
    'C':'G',
    'G':'C',
    'T':'A'
}

x = input("Podaj sekwencje: ")
y = input("Podaj drugą sekwencje: ")
seq1 = Seq(x)
seq2 = Seq(y)

if len(seq1) != len(seq2):
    print("Sekwencje musza byc sobie rowne")
    sys.exit()

pair = 0
for nuc1, nuc2 in zip(seq1, seq2):
    if nuc1 == complementary.get(nuc2):
        pair += 1

print(seq1)

for nuc1, nuc2 in zip(seq1, seq2):
    if nuc1 == complementary.get(nuc2):
        print('|', end='')
    else:
        print(' ', end='')
print("-> ", pair)

print(seq2)