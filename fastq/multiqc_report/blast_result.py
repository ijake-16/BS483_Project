import pandas as pd

# Load BLAST results
blast_results = pd.read_csv('AJ293906_blast_results.out', sep='\t', header=None,
                            names=['query_id', 'subject_id', 'identity', 'alignment_length', 'mismatches',
                                   'gap_opens', 'q_start', 'q_end', 's_start', 's_end', 'evalue', 'bit_score'])

# Filter for high identity and long alignments
conserved_regions = blast_results[(blast_results['identity'] > 90) & (blast_results['alignment_length'] > 100)]

print(conserved_regions[['q_start', 'q_end', 'identity', 'alignment_length']])
