import random
from matplotlib import pyplot as plt


# Function to find positions and percentage of a nucleotide in a sequence
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
        percentage_at_position.append(round(count / len(sequence) * 100, 2))
        current += 1

    return position, percentage_at_position

# List of nucleotides and their respective weights and colors for plotting
nucleotides = ['A', 'C', 'T', 'G']
weight = [0.1, 0.3, 0.4, 0.2]
color = ['blue', 'red', 'green', 'purple']

seq = "".join(random.choices(nucleotides, weight, k=200))

# Plotting the percentage distribution of each nucleotide in the sequence
plt.figure(figsize=(12, 8))
for i, nuc in enumerate(nucleotides):
    position, percentage = find_nucleotide(seq, nuc)
    plt.plot(position, percentage, label=nuc, color=color[i])

plt.xlabel('Pozycja')
plt.ylabel('Procentowy rozkład (%)')
plt.title('Rozkład procentowy')
plt.legend()
plt.grid(True)
plt.savefig('fig_4.png')
plt.close()
