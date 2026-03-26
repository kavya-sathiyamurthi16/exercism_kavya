def to_rna(dna_strand):
    complement = {
        'G': 'C',
        'C': 'G',
        'T': 'A',
        'A': 'U'
    }
    
    rna_strand = ""
    for nucleotide in dna_strand:
        if nucleotide not in complement:
            raise ValueError("Invalid DNA strand")
        rna_strand += complement[nucleotide]
    return rna_strand