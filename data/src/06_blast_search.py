from Bio.Blast import NCBIWWW
from Bio import SeqIO

record = SeqIO.read("data/raw/sequence.fasta","fasta")

result = NCBIWWW.qblast(
    "blastp",
    "nr",
    record.seq
)   

with open ("blast_results.xml", "w") as file:
    file.write(result.read())

print("BLAST completed successfully!")



