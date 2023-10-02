# define a dictionary to map amino acid codes to RNA codons
amino_acid_to_rna = {
    'A': 'GCU', 'R': 'CGU', 'N': 'AAU', 'D': 'GAU',
    'C': 'UGU', 'Q': 'CAA', 'E': 'GAA', 'G': 'GGU',
    'H': 'CAU', 'I': 'AUU', 'L': 'UUG', 'K': 'AAA',
    'M': 'AUG', 'F': 'UUU', 'P': 'CCU', 'S': 'UCU',
    'T': 'ACU', 'W': 'UGG', 'Y': 'UAU', 'V': 'GUU',
    'STOP': 'UAA',
}

# function to convert amino acid code sequence to RNA sequence
def amino_acid_to_rna_sequence(amino_acid_sequence):
    rna_sequence = ""
    for amino_acid in amino_acid_sequence:
        if amino_acid in amino_acid_to_rna:
            rna_sequence += amino_acid_to_rna[amino_acid]
        else:
            raise ValueError(f"Invalid amino acid code: {amino_acid}")
    return rna_sequence

# function to count the frequencies of RNA codons
def count_rna_codon_frequencies(rna_sequence):
    rna_codon_frequencies = {}
    for i in range(0, len(rna_sequence), 3):
        rna_codon = rna_sequence[i:i+3]
        if rna_codon in rna_codon_frequencies:
            rna_codon_frequencies[rna_codon] += 1
        else:
            rna_codon_frequencies[rna_codon] = 1
    return rna_codon_frequencies

# input amino acid code sequence
amino_acid_sequence = input("Please enter letter code sequence: ")

# convert amino acid sequence to RNA sequence
rna_sequence = amino_acid_to_rna_sequence(amino_acid_sequence)

# count the frequencies of RNA codons
rna_codon_frequencies = count_rna_codon_frequencies(rna_sequence)

# print result of rna codon sequence
print("RNA Sequence:", rna_sequence)
print("RNA Codon Frequencies:")
for codon, frequency in rna_codon_frequencies.items():
    print(f"{codon}: {frequency}")
