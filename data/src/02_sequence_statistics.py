from Bio import SeqIO

from collections import Counter


from Bio.SeqUtils.ProtParam import ProteinAnalysis


record = SeqIO.read("data/raw/sequence.fasta","fasta")

sequence = str(record.seq)

protein = ProteinAnalysis(sequence)

helix,turn,sheet = protein.secondary_structure_fraction()

print("=" * 60)
print("Secondary Structure Prediction")
print("=" * 60)

print(f"Alpha Helix  : {helix:.2%}")
print(f"Beta Turn    : {turn:.2%}")
print(f"Beta Sheet   : {sheet:.2%}")
