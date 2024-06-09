from Bio import Align

seqA = "AACCTTGGAA"
seqB = "AAACCCTGG"

aligner = Align.PairwiseAligner()
alignments = aligner.align(seqA, seqB)

for alignment in alignments:
    if alignment.counts()[2] != 0:
        print(alignment, alignment.counts())
