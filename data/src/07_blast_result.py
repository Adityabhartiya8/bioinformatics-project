from Bio.Blast import NCBIXML

# Reads BLAST XML results and displays



print("=" * 60)
print("Parsing BLAST Results")
print("=" * 60)


with open ("blast_results.xml" ) as result_file:
    blasts_record = NCBIXML.read(result_file)
print("\ntop 5 BLAST Hits")


count = 0
for alignment in blasts_record.alignments:

    for hsp in alignment.hsps:
      
      identity = (hsp.identities / hsp.align_length) * 100
      query_coverage = (hsp.align_length / blasts_record.query_length) * 100

      print("=" * 90)
      print("Protein           :", alignment.title)
      print("Protein Length    :", alignment.length)
      print("Alignment Length  :", hsp.align_length)
      print("Identities        :", hsp.identities)
      print(f"Identity (%)      : {identity:.2f}%")
      print(f"Query Coverage    : {query_coverage:.2f}%")
      print("Gaps              :", hsp.gaps)
      print("Bit Score         :", hsp.bits)
      print("E-value           :", hsp.expect)
      count +=1
      if count==5:
        break

    if count==5:
        break   