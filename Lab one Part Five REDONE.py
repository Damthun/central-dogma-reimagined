# Write a program that displays the complementary sequence for a DNA sequence entered by the user. Again, for full
# credit, you must employ a “for” loop somewhere in your code

# Function that takes a sequence as an input and replaces given nucleotides.
def complementary_string(sequence):
    for nucleotide in sequence:
        if actg.get(nucleotide) is not None:
            complementary_nucleotide = actg[nucleotide]
            sequence = sequence.replace(nucleotide, complementary_nucleotide)
        else:
            sequence = sequence.replace(nucleotide, '')
    return sequence


# Ask the user how many DNA sequences are to be used.
num_sequences = input('I heard you have DNA, How many strings ya got?')
actg = {
    't': 'A',
    'a': 'T',
    'g': 'C',
    'c': 'G'
}
# For loop that iterates through the number of sequences and produces a corresponding complementary sequence.
for sequences in range(int(num_sequences)):

    input_sequence = input('I heard you have DNA, ENTER Sequence here:')
    sequence2 = input_sequence.lower()
    complementary_sequence = complementary_string(sequence2)
    print("The complementary string is: \n" + complementary_sequence)
