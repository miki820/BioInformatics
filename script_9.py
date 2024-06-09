import primer3

sequences = []

with open("primers.txt", "r") as file:
    for line in file:
        sequences.append(line.strip())

print("Primer".ljust(20), "Tm".ljust(10), "Homodimer".ljust(15), "Hairpin")
for sequence in sequences:
    tm = round(primer3.calc_tm(sequence), 2)
    homodimer = "Yes" if primer3.calc_homodimer(sequence).structure_found else "No"
    hairpin = "Yes" if primer3.calc_hairpin(sequence).structure_found else "No"
    print(sequence.ljust(15), str(tm).ljust(10), str(homodimer).ljust(15), str(hairpin))
