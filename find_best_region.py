import subprocess
import tempfile
from Bio import SeqIO

def run_rnafold(sequence):
    """Run RNAfold and return the minimum free energy (MFE)."""
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(sequence.encode())
        tmp.close()
        result = subprocess.run(['RNAfold', '--noPS', tmp.name], capture_output=True, text=True)
        mfe_line = result.stdout.strip().split('\n')[-1]
        mfe = float(mfe_line.split('(')[-1].strip(')'))
    return mfe

def sliding_window_analysis(sequence, window_size, step_size):
    """Analyze the sequence with a sliding window to find regions with minimal secondary structure."""
    min_mfe = float('inf')
    best_region = None

    for start in range(0, len(sequence) - window_size + 1, step_size):
        window_seq = sequence[start:start + window_size]
        mfe = run_rnafold(window_seq)
        if mfe < min_mfe:
            min_mfe = mfe
            best_region = (start, start + window_size, mfe)

    return best_region

# Load your target sequence
record = SeqIO.read("fastq/AJ293906.1.fasta", "fasta")
target_sequence = str(record.seq)

# Parameters for sliding window
window_size = 200
step_size = 20

# Find the region with minimal secondary structure
best_region = sliding_window_analysis(target_sequence, window_size, step_size)

# Output the best region
start, end, mfe = best_region
print(f"Best region: {start}-{end} with MFE: {mfe}")
print(f"Sequence: {target_sequence[start:end]}")
