import random

import Bio

print(Bio.__version__)


n = int(input("Podaj ile ciągów wygenerowac: "))
k = int(input("Podaj jakiej mają być długości: "))

# Opening a file to write the generated sequences
f = open("sequences.txt", "w")

for i in range(n):
    # Generating a random DNA sequence of length k and writing it to the file
    f.write(("".join([random.choice("ACTG") for _ in range(k)])))
    f.write("\n")

f.close()
