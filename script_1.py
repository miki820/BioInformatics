import random

import Bio

print(Bio.__version__)

n = int(input("Podaj ile ciągów wygenerowac: "))
k = int(input("Podaj jakiej mają być długości: "))

f = open("sequences.txt", "w")

for i in range(n):
    f.write(("".join([random.choice("ACTG") for _ in range(k)])))
    f.write("\n")

f.close()
