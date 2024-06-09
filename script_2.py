from Bio.Seq import Seq


def find_motif(sequence, motif):
    position = []

    current = 0
    while current < len(sequence):
        current = sequence.find(motif, current)
        if current == -1:
            break
        position.append(current)
        current += 1

    return position


file_path = 'sequence.txt'
with open(file_path, 'r') as file:
    dna_sequence = file.read().strip()

sequence = Seq(dna_sequence)
motif = input("Podaj motyw: ")
position = find_motif(sequence, motif)

print("Szukany motyw:", motif)
if position:
    print("Pozycje:", ", ".join(map(str, position)))
else:
    print("Brak motywu")
