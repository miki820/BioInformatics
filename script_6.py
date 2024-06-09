from Bio import Align

seqA = "AACCTTGGAA"
seqB = "AAACCCTGG"

# Performing pairwise alignment
aligner = Align.PairwiseAligner()
alignments = aligner.align(seqA, seqB)

# Printing the alignments with mismatches
for alignment in alignments:
    if alignment.counts()[2] != 0:
        print(alignment, alignment.counts())
