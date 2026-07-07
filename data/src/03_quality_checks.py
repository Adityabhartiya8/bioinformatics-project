from Bio import SeqIO

# read the fasta file

record = SeqIO.read("data/raw/sequence.fasta","fasta")

sequence = str(record.seq)

valid_amino_acids = set("ACDEFGHIKLMNPQRSTVWY")
print("_"*60)
print("Protein quality control report")
print("_"*60)

# check 1 : sequence length

if len(sequence)>100:
    print("length (>100aa)    : PASS")
else:
    print("length(<100 aa)    : FAIL")

# check 2 : unknown residue

if "x" in sequence:
    print("unknown residue (x)       : FAIL")
else:
    print("NO unknown residue (x)    : PASS")

# Check 3: Stop Codons

if "*" in sequence:
    print("Stop Codons find(*)         : FAIL")
else:
    print("No Stop Codons  (*)         : PASS")

# Check 3 :  valid valid amino acids

invalid = []

for aa in sequence:
    if aa not in valid_amino_acids:
        invalid.append(aa)
if len(invalid)==0:
    print("valid symbols     :  PASS")
else:
    print(f"invalid sequennce found {set(invalid) }   : FAIL")
   
# overall result

if (
    len(sequence)>100
    and "x" not in sequence
    and "*" not in sequence
    and len(invalid)==0 
):
    print("\noverall result    : PASS")

else:
    print("\nover all result    : FAIL")