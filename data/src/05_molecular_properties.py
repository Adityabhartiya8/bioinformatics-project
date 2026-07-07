from Bio import SeqIO

from collections import Counter

from Bio.SeqUtils.ProtParam import ProteinAnalysis


record = SeqIO.read("data/raw/sequence.fasta","fasta")

sequence = str(record.seq)


print("_"*80)
protein = ProteinAnalysis(sequence)
print("Physicochemical properties")
print("_"*80)


print(f"molecular weight     : {protein.molecular_weight():.3f}")
print(f"Isoeletric point     : {protein.isoelectric_point():.3f}")
print(f"Instability index    : {protein.instability_index():.3f}")
print(f"GRAVY Score          : {protein.gravy():.3f}")
print(f"Aromaticity          : {protein.aromaticity():.3f}")