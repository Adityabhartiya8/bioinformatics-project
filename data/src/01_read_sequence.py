from Bio import SeqIO

from collections import Counter

from Bio.SeqUtils.ProtParam import ProteinAnalysis

# read the fasta file

record = SeqIO.read("data/raw/sequence.fasta","fasta")

# displays information about the protein

print("-"*80)
print("protein information")
print("-"*80)

print(f"protein ID      : {record.id}")
print(f"description     : {record.description}")
print(f"sequence length : {len(record.seq)}")

print(f"\nprotein sequence :\n{record.seq}")
print(f"\nAnalysis complete.")
