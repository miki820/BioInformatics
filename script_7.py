def read_sam(path):
    with open(path, 'r') as f:
        for line in f:
            columns = line.strip().split('\t')
            seq = columns[9]
            cigar = columns[5]
    return seq, cigar


seq, cigar = read_sam('my_alignment.txt')

max_aligned = 0
aligned = 0
position = 0

for i, char in enumerate(cigar):
    if char.isdigit():
        aligned = aligned * 10 + int(char)
    else:
        if char == 'M':
            if aligned > max_aligned:
                max_aligned = aligned
                position = i - len(str(aligned))
        aligned = 0

print("Maksymalna długość dopasowania:", max_aligned)
print("Maksymalna pozycja dopasowania:", position)
