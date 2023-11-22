# Write a program that takes a DNA sequence and outputs an amino acid chain.
'''
The goal of this updated version was to avoid the twenty loops and 64 conditionals that I had!
I wanted to see how I might minimize the use of 64 dictionary keys.
If you look at a codon table, you'll notice three patterns in the codon to Amino acid, these patterns are as follows.

1) The first two nucleotides guarantee a specific AA (dict1) CU_ -> Leu
2) The third letter picks one of two AA (dict2) i.e.  GA_ -> Asp or Glu  (GAU & GAC = Asp)  (GAG & GAA = Glu)
3) Special cases AU* & UG* which require all three nucleotides.
'''

# Asking for DNA sequence, and subsequently making it uniform with the string lower method.
sequence_dna = input("Need an AA chain? give me that DNA!").lower()

# Iterating over non-nucleotide characters and replacing all instances of that character in our sequence.
non_actg = ' bdefhijklmnopqrsuvwxyz'
for char in non_actg:
    sequence_dna = sequence_dna.replace(char, '')

# Uppercase copy of our sequence.
sequencedna_uppercase = sequence_dna.upper()
# Trick to avoid having to go from Encoding > complement > RNA is Replacement of Thymine to Uracil.
sequence_rna = sequencedna_uppercase.replace('T', 'U')  # transcribed > rna.

SequenceU = sequence_rna.upper()
num_aminos = len(sequence_rna)/3  # Using this as the length to iterate. Any remainder treated as imperfect sequence.

aa_chain = []  # empty list to be filled with our AA's
# Case 1: Third position not determinate of resulting AA (CUA,CUU,CUG,CUC -> Leu)
dict1 = {
    'CU': 'Leu', 'GU': 'Val', 'UC': 'Ser', 'CC': 'Pro',
    'AC': 'Thr', 'GC': 'Ala', 'GG': 'Gly', 'CG': 'Arg'
}
# Case 2: Third Letter is determined by U/C and G/A. Halves necessary key/value pairs in this category.
dict2 = {
    'UAG': '***', 'UAC': 'Tyr', 'CAG': 'Gln', 'CAC': 'His',
    'AAG': 'Lys', 'AAC': 'Asn', 'GAG': 'Glu', 'GAC': 'Asp',
    'AGG': 'Arg', 'AGC': 'Ser', 'UUG': 'Leu', 'UUC': 'Phe',
}
# Case 3: Third character matters. Not able to reduce number of Key pairs significantly without hassle.
dict3 = {
    'AUG': 'Met', 'AUU': 'Ile', 'AUC': 'Ile', 'AUA': 'Ile',
    'UGG': 'Trp', 'UGU': 'Cys', 'UGC': 'Cys', 'UGA': '***',
}
replacement = {
    'AG': '', 'UU': ''
}
# For the number of resulting Amino Acids in chain.
for i in range(int(num_aminos)):
    # For every 3 character groupings 0-2, 3-5, 6-8... If its case one append resulting value.
    if SequenceU[3*i:3*i+2] in dict1:  # checks if case one.
        aa_chain.append(dict1[SequenceU[3*i:3*i+2]])  # add to chain.
        continue
    #  All _A_, AG_, and UU_ are case two.
    elif SequenceU[3*i+1] == 'A' or SequenceU[3*i:3*i+2] in replacement:
        codon = SequenceU[3*i:3*i+3]
        # No difference between U/A and A/G in position 3 for case two i.e. UUU is equivalent to UUC
        codon = codon[:2] + codon[2].replace('U', 'C')
        codon = codon[:2] + codon[2].replace('A', 'G')
        aa_chain.append(dict2[codon])
    # The two case three examples, straightforward. If you are okay with a long dict, just do this with no conditional.
    elif SequenceU[3*i:3*i+2] == 'AU' or SequenceU[3*i:3*i+2] == 'UG':
        aa_chain.append(dict3[SequenceU[3*i:3*i+3]])

chain = '-'.join(aa_chain)
print(chain)
# This is the dictionary you would use assuming you just wanted to replace nucleotides with corresponding AA.
'''
codon_table = {
    'UUU': 'Phe', 'UUC': 'Phe', 'UUA': 'Leu', 'UUG': 'Leu',
    'UCU': 'Ser', 'UCC': 'Ser', 'UCA': 'Ser', 'UCG': 'Ser',
    'UAU': 'Tyr', 'UAC': 'Tyr', 'UAA': '***', 'UAG': '***',
    'UGU': 'Cys', 'UGC': 'Cys', 'UGA': '***', 'UGG': 'Trp',
    'CUU': 'Leu', 'CUC': 'Leu', 'CUA': 'Leu', 'CUG': 'Leu',
    'CCU': 'Pro', 'CCC': 'Pro', 'CCA': 'Pro', 'CCG': 'Pro',
    'CAU': 'His', 'CAC': 'His', 'CAA': 'Gln', 'CAG': 'Gln',
    'CGU': 'Arg', 'CGC': 'Arg', 'CGA': 'Arg', 'CGG': 'Arg',
    'AUU': 'Ile', 'AUC': 'Ile', 'AUA': 'Ile', 'AUG': 'Met',
    'ACU': 'Thr', 'ACC': 'Thr', 'ACA': 'Thr', 'ACG': 'Thr',
    'AAU': 'Asn', 'AAC': 'Asn', 'AAA': 'Lys', 'AAG': 'Lys',
    'AGU': 'Ser', 'AGC': 'Ser', 'AGA': 'Arg', 'AGG': 'Arg',
    'GUU': 'Val', 'GUC': 'Val', 'GUA': 'Val', 'GUG': 'Val',
    'GCU': 'Ala', 'GCC': 'Ala', 'GCA': 'Ala', 'GCG': 'Ala',
    'GAU': 'Asp', 'GAC': 'Asp', 'GAA': 'Glu', 'GAG': 'Glu',
    'GGU': 'Gly', 'GGC': 'Gly', 'GGA': 'Gly', 'GGG': 'Gly',
}
'''