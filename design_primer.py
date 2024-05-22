import primer3

# The given 200bp template sequence
template_sequence = ("GAACAGGGCGGGGGTGGCGCAGGCGGCGGCAACAACAGTGGCAGCGGCGCGGAAGAGAACTCC"
                     "AACGCGGCAGCCGCGGCAATGCAGCCGGTGGAGGACATGAACGATCATGCCATTCGCGGCGAC"
                     "ACCTTTGCCACACGGGCGGAGGAGAAGCGCGCTGAGGCCGAGGCAGCGGCAGAAGCTGCCGCC"
                     "CCCCGCTGCGCA")

# Define primer design parameters
seq_args = {
    'SEQUENCE_ID': 'example',
    'SEQUENCE_TEMPLATE': template_sequence,
}

global_args = {
    'PRIMER_OPT_SIZE': 20,
    'PRIMER_MIN_SIZE': 18,
    'PRIMER_MAX_SIZE': 25,
    'PRIMER_OPT_TM': 60.0,
    'PRIMER_MIN_TM': 57.0,
    'PRIMER_MAX_TM': 63.0,
    'PRIMER_MAX_NS_ACCEPTED': 1,
    'PRIMER_PRODUCT_SIZE_RANGE': [[100, 200]],
    'PRIMER_NUM_RETURN': 5,
}

# Design primers
primer_results = primer3.bindings.designPrimers(seq_args, global_args)

# Print designed primers
for i in range(primer_results['PRIMER_PAIR_NUM_RETURNED']):
    print(f"Left primer {i}: {primer_results[f'PRIMER_LEFT_{i}_SEQUENCE']}")
    print(f"Right primer {i}: {primer_results[f'PRIMER_RIGHT_{i}_SEQUENCE']}")
    print(f"Product size: {primer_results[f'PRIMER_PAIR_{i}_PRODUCT_SIZE']}")
    print(f"Left primer Tm: {primer_results[f'PRIMER_LEFT_{i}_TM']:.2f} °C")
    print(f"Right primer Tm: {primer_results[f'PRIMER_RIGHT_{i}_TM']:.2f} °C")
    print(f"Left primer GC%: {primer_results[f'PRIMER_LEFT_{i}_GC_PERCENT']:.2f} %")
    print(f"Right primer GC%: {primer_results[f'PRIMER_RIGHT_{i}_GC_PERCENT']:.2f} %")
    print()
