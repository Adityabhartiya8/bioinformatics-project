import matplotlib.pyplot as plt
from Bio import SeqIO
from collections import Counter
from Bio.SeqUtils.ProtParam import ProteinAnalysis

record = SeqIO.read("data/raw/sequence.fasta","fasta")
counts = Counter(str(record.seq))

# amino acid composition charts

amino_acid = sorted(counts.keys())
frequency = [counts[aa] for aa in amino_acid]


plt.figure(figsize=(10,5))
plt.bar(amino_acid,frequency)

plt.title("amino acid composition")
plt.xlabel("amino acid")
plt.ylabel("frequency")

plt.show()






protein = ProteinAnalysis(record)



helix,turn,sheet = protein.secondary_structure_fraction()


helix = helix * 100
sheet = sheet * 100
turn = turn * 100

# Labels
labels = [
    "Alpha Helix",
    "Beta Sheet",
    "Beta Turn"
]

# Values
sizes = [
    helix,
    sheet,
    turn
]

# Create the figure
plt.figure(figsize=(7, 7))

# Draw the pie chart
plt.pie(
    sizes,
    labels=labels,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Predicted Secondary Structure Composition")


plt.show()




