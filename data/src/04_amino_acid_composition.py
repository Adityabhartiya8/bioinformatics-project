from Bio import SeqIO

from collections import Counter



record = SeqIO.read("data/raw/sequence.fasta","fasta")

sequence = str(record.seq)

total_length = len(sequence)

count = Counter(sequence)



amino_acid = {
        "A": "Alanine",
        "C": "Cysteine",
        "D": "Aspartic Acid",
        "E": "Glutamic Acid",
        "F": "Phenylalanine",
        "G": "Glycine",
        "H": "Histidine",
        "I": "Isoleucine",
        "K": "Lysine",
        "L": "Leucine",
        "M": "Methionine",
        "N": "Asparagine",
        "P": "Proline",
        "Q": "Glutamine",
        "R": "Arginine",
        "S": "Serine",
        "T": "Threonine",
        "V": "Valine",
        "W": "Tryptophan",
        "Y": "Tyrosine"
}

print("_"*80)
print("amino acid composition")
print("_"*80)


for aa in amino_acid:
    counts = count.get(aa,0)
    percentage = (counts/total_length)*100
    print(f"{aa} ({amino_acid[aa]})  :  {count.get(aa,0)}  :  {percentage}%")