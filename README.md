# Computational Analysis of Hypothetical Protein WP_491523178.1 (*Helicobacter pylori*)

A bioinformatics portfolio project analyzing an uncharacterized "hypothetical protein" from *Helicobacter pylori* using Python (BioPython) for sequence-level analysis, combined with BLAST, multiple sequence alignment, conserved domain search (CDD), InterProScan, MotifFinder, and SWISS-MODEL for homology-based structural insight.

This was built as a second-year B.Sc. Biotechnology student project to practice a full sequence-to-structure bioinformatics workflow on a real, unannotated protein — not a textbook example with a known answer.

## Project Overview

WP_491523178.1 is a 363-amino-acid protein from *H. pylori* with no assigned function in NCBI beyond the label "hypothetical protein." This project runs it through a standard characterization pipeline to see what can reasonably be inferred about it using sequence-based methods alone:

- Amino acid composition and physicochemical properties (BioPython `ProteinAnalysis`)
- Predicted secondary structure fractions
- Sequence quality control checks
- BLASTP search against NCBI's `nr` database
- Multiple sequence alignment (Clustal Omega) of top BLAST hits
- Conserved domain search (NCBI CD-Search / CDD)
- Functional signature scan (InterProScan)
- Motif search (MotifFinder / Pfam)
- Homology-based 3D structure modelling (SWISS-MODEL)

No single tool gave a confident functional annotation, but five independent lines of evidence (composition, secondary structure prediction, InterPro's coiled-coil/transmembrane calls, MotifFinder's helical/membrane-associated motif hits, and the SWISS-MODEL structure) consistently point toward this protein being a long, helical, possibly membrane-associated protein rather than a compact globular enzyme. Full reasoning and discussion are in the report.

## Folder Structure

```
WP_491523178.1-hpylori-analysis/
├── README.md
├── data/
        └──├── blast_results.xml
           ├── clustal_result.aln
           ├── protein.fasta
│   ├── raw/
│     └── sequence.fasta
├── scr/
│   ├── 01_read_sequence.py
│   ├── 02_sequence_statistics.py
│   ├──03_quality_checks.py
│   ├── 04_amino_acid_composition.py
│   ├── 05_molecular_properties.py
│   ├── 06_blast_search.py
|   ├──07_blast_result.py
|   ├──8_multi_sequence_alignment.py
|   ├──09_visualization.py
```

## Requirements

- Python 3.10+
- [Biopython](https://biopython.org/)
- matplotlib
- An internet connection (for `blast_search.py`, which submits a live query to NCBI)

Install dependencies:

```bash
pip install biopython matplotlib
```

## How to Run

1. Place your protein FASTA file at `data/raw/sequence.fasta`.

2. Run the core sequence analysis (composition + physicochemical properties + secondary structure):
   ```bash
   python scripts/protein_info.py
   ```

3. Generate the amino acid composition chart:
   ```bash
   python scripts/amino_acid.py
   ```

4. Run the sequence quality control check:
   ```bash
   python scripts/quality_control.py
   ```

5. Run a live BLASTP search against NCBI (this can take a few minutes, since it queries NCBI's servers directly):
   ```bash
   python scripts/blast_search.py
   ```
   This produces `blast_results.xml` in the working directory.

6. Parse and summarize the top BLAST hits:
   ```bash
   python scripts/blast_result.py
   ```

7. For the multiple sequence alignment step, align your BLAST hits externally using [Clustal Omega](https://www.ebi.ac.uk/jdispatcher/msa/clustalo) and save the result as `data/scr/clustal_result.aln`, then run:
   ```bash
   python scripts/msa_analysis.py
   ```

8. For domain, motif, and structure analysis, submit the same sequence to:
   - [NCBI CD-Search](https://www.ncbi.nlm.nih.gov/Structure/cdd/wrpsb.cgi) for conserved domains
   - [InterProScan](https://www.ebi.ac.uk/interpro/) for functional signatures
   - [MotifFinder](https://www.genome.jp/tools/motif/) for Pfam motif matches
   - [SWISS-MODEL](https://swissmodel.expasy.org/) for homology-based structure prediction

## Results

| Analysis | Key finding |
|---|---|
| Amino acid composition | High K (11.6%) and E (11.3%), low P (1.1%) and W (0.8%) — composition consistent with helical regions |
| Physicochemical properties | MW ≈ 41.8 kDa, pI 6.03, instability index 46.59 (flagged unstable by ProtParam), GRAVY −0.48 (hydrophilic) |
| Secondary structure prediction | 38.8% alpha helix, 24.8% beta turn, 33.9% beta sheet |
| Quality control | Sequence passed all checks (length, no unknown residues, no stop codons, valid alphabet) |
| BLAST | Top hit 100% identical (EPZ97267.1, *H. pylori* strain UM077); all top 5 hits from *H. pylori* only |
| MSA | 5 sequences aligned, 614-column alignment; high conservation in the core region across strains |
| CDD | One weak superfamily hit (PTZ00341, E = 5.7×10⁻⁴) — likely not biologically meaningful |
| InterPro | No protein family predicted; coiled-coil and transmembrane regions flagged |
| MotifFinder | 8 Pfam motifs found, mostly weak E-values, thematically helical/membrane-associated |
| SWISS-MODEL | GMQE 0.79, monomer, elongated multi-helix bundle structure |

Full observation / interpretation / biological meaning / limitations for each result are documented in the report (`report/WP_491523178_Portfolio_Report.docx`).

## Future Improvements

- Extend the BLAST search beyond *H. pylori* (e.g. against other Helicobacter species or a wider taxonomic sample) to get a better sense of how deep the conservation of this protein actually goes.
- Automate the MSA step directly from Python instead of running Clustal Omega externally.
- Compare the SWISS-MODEL homology model against a *de novo* structure prediction, once compute resources allow.
- Wrap the individual scripts into a single command-line pipeline with proper argument parsing.
- Add unit tests for the parsing scripts (`blast_result.py`, `msa_analysis.py`) to make the pipeline more robust to malformed input files.

## Disclaimer

This project is a computational, sequence-based analysis only. No laboratory experiments were performed. All interpretations here are hypotheses based on bioinformatics evidence, not confirmed biological facts — see the report's Conclusion section for a full discussion of what this analysis can and cannot establish.
