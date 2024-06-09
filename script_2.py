from Bio.Seq import Seq


# Function to find all positions of a motif in a given sequence
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


# Reading the DNA sequence from the file
file_path = 'sequence.txt'
with open(file_path, 'r') as file:
    dna_sequence = file.read().strip()

# Creating a Seq object from the DNA sequence
sequence = Seq(dna_sequence)
motif = input("Podaj motyw: ")

# Finding positions of the motif in the sequence
position = find_motif(sequence, motif)

print("Szukany motyw:", motif)
if position:
    print("Pozycje:", ", ".join(map(str, position)))
else:
    print("Brak motywu")
