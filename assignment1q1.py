# Define a dictionary that maps DNA codons to mRNA codons
dna_to_mrna = {
    'A': 'U',
    'T': 'A',
    'G': 'C',
    'C': 'G'
}

# Define a dictionary that maps mRNA codons to amino acids (sideways layout)
mrna_to_amino_acid = {
    'UUU': 'Phe', 'UUC': 'Phe', 'UUA': 'Leu', 'UUG': 'Leu',
    'CUU': 'Leu', 'CUC': 'Leu', 'CUA': 'Leu', 'CUG': 'Leu',
    'AUU': 'Ile', 'AUC': 'Ile', 'AUA': 'Ile', 'AUG': 'Met',
    'GUU': 'Val', 'GUC': 'Val', 'GUA': 'Val', 'GUG': 'Val',
    'UCU': 'Ser', 'UCC': 'Ser', 'UCA': 'Ser', 'UCG': 'Ser',
    'CCU': 'Pro', 'CCC': 'Pro', 'CCA': 'Pro', 'CCG': 'Pro',
    'ACU': 'Thr', 'ACC': 'Thr', 'ACA': 'Thr', 'ACG': 'Thr',
    'GCU': 'Ala', 'GCC': 'Ala', 'GCA': 'Ala', 'GCG': 'Ala',
    'UAU': 'Tyr', 'UAC': 'Tyr', 'UAA': 'Stop', 'UAG': 'Stop',
    'CAU': 'His', 'CAC': 'His', 'CAA': 'Gln', 'CAG': 'Gln',
    'AAU': 'Asn', 'AAC': 'Asn', 'AAA': 'Lys', 'AAG': 'Lys',
    'GAU': 'Asp', 'GAC': 'Asp', 'GAA': 'Glu', 'GAG': 'Glu',
    'UGU': 'Cys', 'UGC': 'Cys', 'UGA': 'Stop', 'UGG': 'Trp',
    'CGU': 'Arg', 'CGC': 'Arg', 'CGA': 'Arg', 'CGG': 'Arg',
    'AGU': 'Ser', 'AGC': 'Ser', 'AGA': 'Arg', 'AGG': 'Arg',
    'GGU': 'Gly', 'GGC': 'Gly', 'GGA': 'Gly', 'GGG': 'Gly'
}

# dna to mrna translation
def dna_to_mrna_translation(dna_sequence):
    mrna_sequence = ''.join([dna_to_mrna.get(base.upper(), 'Unknown') for base in dna_sequence])
    return mrna_sequence

# mrna to amino acid translation
def mrna_to_amino_acid_translation(mrna_sequence):
    amino_acid_sequence = []

    # slice the mrna sequence to 3 word abbreviation
    for i in range(0, len(mrna_sequence), 3):
        codon = mrna_sequence[i:i+3]
        # mrna to amino acid
        if codon in mrna_to_amino_acid:
            amino_acid_sequence.append(mrna_to_amino_acid[codon])
        else:
            amino_acid_sequence.append('Unknown')
    return amino_acid_sequence

# Example DNA sequence
dna_sequence = "attacgattagc"

# print the dna to mrna result
mrna_sequence = dna_to_mrna_translation(dna_sequence)
print("DNA to mRNA Translation:")
print("DNA Sequence:   " + dna_sequence.upper())  # Convert to uppercase for display
print("mRNA Sequence:  " + mrna_sequence)

# print the amino acids of mrna result
amino_acids = mrna_to_amino_acid_translation(mrna_sequence)
print("\nAmino Acids:")
print(" - ".join(amino_acids))
