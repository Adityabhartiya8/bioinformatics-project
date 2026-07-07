# read and analyzes a clustal omega alignment


from Bio import AlignIO

print("=" * 70)
print("Multiple Sequence Alignment")
print("=" * 70)

alignment = AlignIO.read("clustal_result.aln","clustal")

print(f"number of sequence  : {len(alignment)}")
print(f"alignment length  : {alignment.get_alignment_length()}amino acid")

for record in alignment:
    print(record.id)
    print(record.seq)
    print("_"*70)

