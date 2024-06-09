import matplotlib.pyplot as plt
from Bio.Seq import Seq


def find_nucleotide(sequence, nucleotide):
    position = []
    percentage_at_position = []

    count = 0
    current = 0
    while current < len(sequence):
        current = sequence.find(nucleotide, current)
        if current != -1:
            count += 1
        else:
            break
        position.append(current)
        percentage_at_position.append(round(count/len(sequence) * 100, 2))
        current += 1

    return position, percentage_at_position


def plot(positions, percentage, nucleotide):
    plt.figure(figsize=(12, 8))
    plt.plot(positions, percentage)
    plt.xlabel('Pozycja w sekwencji')
    plt.ylabel('Procentowy udział (%)')
    plt.title(f'Rozkład procentowy nukleotydu {nucleotide}')
    plt.grid(True)
    plt.savefig('fig_3.png')
    plt.close()


file_path = 'sequence.txt'
with open(file_path, 'r') as file:
    dna_sequence = file.read().strip()

sequence = Seq(dna_sequence)
nucleotide = input("Podaj nukleotyd: ")
length_of_seq = len(sequence)
nucleotide_composition = sequence.count(nucleotide)

print("Percentage: ", round(nucleotide_composition/length_of_seq * 100, 2), "%")

find_nucleotide(sequence, nucleotide)
positions, percentage = find_nucleotide(sequence, nucleotide)
plot(positions, percentage, nucleotide)
