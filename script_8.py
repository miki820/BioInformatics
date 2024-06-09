from Bio import Align
import numpy as np

seq_1 = "AAGAAATTCCAAGTCCAGGGATACACAAACAGGTGTACAGCAAATCATGTAGGTGGTACTTTTCCCCTAAGTTATAATTT\
AATCTATACCCTAGGAAAATGCCAAAGTCACAATTGGGTGGATTGGGTGATTTTCCAGTAGAAAGAAAATTCCATCCCAT\
CTTTGTTCTCAAAACGTTTTTTCTTTGCATATAGGTAAGGGTTTACAGATCAATAATCTTCTTGATTTCAGTATGAAATT\
ACTTTCTCTTTGCTTGAGTTACTCTGAGTTATGCAGAAGGCTCCCTGTTCTGAATCCACTAGTATTTCTTTTTTTCTGA\
GAATATTTCAGTGTATGTTGAAAACAAGGAACATTATGGAAACTTTCAGTCCTTAATTGTGTCAAGATATTAATGTTAGT\
GATATACAAATTAGATGGTGATGGGAAACTTGAGCCTGGCTTTATAGGAGGTAATTTTTTTTTCTTCCTTCCTTTTTTTG\
CAGGGGTGGGGGTTATGATACAGGGATACAGGTAAGATAGTCCTATAAACTCATCTGCTGATAGTTCATATGAAGGCTTT\
TGACTAGAAAACTTCCATTAATAGTGCTGAGATATAAACATATGGTAAAACTGCTTTCCATATTAAGATACCTTGCCAC\
CCACTCCTTTTCTTTGAGACAAGGTCTTGCTCTGTTAGCCAGGCTGGAGTGCAGTCATGTGATCTTGATGCACCGCAGCC\
TCCACCTCCCGGACTCAAGCGATCCTTCCGCCTCAGACCTCCAAATAGCTGGGACCACAGGCATGCACAGGGACCATACC\
TGGCTAATTTTTGTATTTTTTGTAGAGACGGGTTTTCACCATGTTGCCCAAGCTGGTTCAAACTCCTGAGCTCAAGCAA\
TCTGCCCACCTTGGTCTCCCAGAATGCTGGGATTACAGGCATGAGCCACCACCACGTCTGGCTTCCCCCTACTTGTTTTT"
seq_2 = "AAGAAATTCACAGTCCAGGGATACACAAACAGGTGTACAAAGCAAATCATGTAGGTGGTACTTTTCCCCTAAGTTATAATTT\
AATCTATACCCTAGGAAAATGCCAAAGTCGGAATTGGGTGATTGGGTGTTTCCAGTAGAAAGAAAATTCCATCCCAT\
CTTTGTTCTCAAAACGTTTTTTCTTTGCATATAGCTAAGGGTTTACAGATCAATAATCTCTTGATTTCAGTATGAAATT\
ACTTTCTCTTTGCTTGAGTTACTCTGAATTATGCAGAAGGCTCCCTGTTCTGAATCCACTTATGTATTTCTTTTTTTCTGA\
GAATATTTCAGTGTATGTTGAAAACAAGGAACATTATGGAAACTTTCAGTTCCTTAATTGTGTCAAATATTAATGTTAGT\
GATATACAAATTAGATGGTGATGGGAAACTTGAGCCTGGCTTTATAGGAGGTAATTTTTTTTTCTTCCTTCCTTTTTTTG\
CAGGGGTGGGGGTTATGATACAGGGATACAGGTAAGAGTCCTATAACTCATCTGCTGATAGTTCATATGAAGGCTTT\
TGACTAGAATAACTTCCATTAATAGTGCTGAAGATATAAACATATGGTAAAACTGCTTTCCATATTAAGATACCTTGCCAC\
CCACTCCTTTTCTTTGAGACAAGCCTTGCTCTGTATATAGCCAGGCTGGAGTGCAGTCATGTGATCTTGATGCACCGCAGCC\
TCCACCTCCCGGACTCAAGCGATCTTCCGCCTCAGACTCCAAATAGCTGGGACCACAGGCATGCACAGGGACCATACC\
TGGCTAATTTTTGTATTTTTTGTAGAGACGGCCCCTCCCATGTTGCCCAAGCTGGTCTCAAACTCCTGAGCTCAAGCAA\
TCTGCCCACCTTGGTCCCCATTTGCTGGGATTACAGCATGAGCGACCACCAGTCTGTTGCCCCCTACTTGTTTTT"

aligner = Align.PairwiseAligner()
alignments = aligner.align(seq_1, seq_2)

x = int(input("Podaj N: "))

f = open('alignment_info.txt', 'w')

count = 1
for alignment in alignments:
    if count == x:
        f.write(str(alignment.counts()))
        f.write("\n")
        f.write(str(alignment.coordinates))
        f.write("\n")
        f.write(str(alignment))
        break
    count += 1