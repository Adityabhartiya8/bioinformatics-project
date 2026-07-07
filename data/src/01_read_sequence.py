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


# display all amino acid count and persentage

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


# calculates physicochemical proterties of a protein

print("_"*80)
protein = ProteinAnalysis(sequence)
print("Physicochemical properties")
print("_"*80)


print(f"molecular weight     : {protein.molecular_weight():.3f}")
print(f"Isoeletric point     : {protein.isoelectric_point():.3f}")
print(f"Instability index    : {protein.instability_index():.3f}")
print(f"GRAVY Score          : {protein.gravy():.3f}")
print(f"Aromaticity          : {protein.aromaticity():.3f}")

# Predict secondary structure fractions

helix,turn,sheet = protein.secondary_structure_fraction()

print("=" * 60)
print("Secondary Structure Prediction")
print("=" * 60)

print(f"Alpha Helix  : {helix:.2%}")
print(f"Beta Turn    : {turn:.2%}")
print(f"Beta Sheet   : {sheet:.2%}")
