# Assuming any Sample could be partial, there are three ways to read a sequence, these are known as ORF's.
# Given a sample of DNA, give all possible polypeptides in each ORF both forwards and backwards

class DNA:
    def __init__(self, coding_sequence):
        # Class attributes for a DNA sequence.
        self.coding_sequence = coding_sequence
        self.mrna_sequence = coding_sequence.replace("T", "U")

    # Class method that gives us the codons for each ORF.
    def codons(self):  # Goes through each Nucleotide and finds all three letter sequences (codons) in the RNA Sequence.
        frames = {
            0: [], 1: [], 2: []
        }

        for nucleotide in range(len(self.mrna_sequence)-2):
            current_codon = self.mrna_sequence[nucleotide:nucleotide+3]  # For "ACTACT" grab ACT, CTA, TAC, ACT
            # Since we are looking at i:i+3 each iteration, i % 3 gives 0, 1 or 2 which relates to which ORF we are in.
            frames[nucleotide % 3].append(current_codon)

        return frames

    # Class method that uses the codon class method to get codons, and then assigns start/stop codons to a dictionary.
    def start_stop(self):  # loop through the codon list and find stops/starts
        codon_list = self.codons()  # Using class method to get dictionary with possible codons for each ORF.
        # Variables that denote starts and stops that could form a fragment/ Amino Acid sequence.
        stop_codes = ["UAA", "UGA", "UAG"]
        start_code = "AUG"
        # Creating dictionaries to hold resulting stop and start locations.
        starts = {
            0: [], 1: [], 2: []
        }
        stops = {
            0: [], 1: [], 2: []
        }
        # For frames 0, 1, & 2...
        for key in codon_list:
            # Using enumerate to allow us to keep an index of location.
            for index, item in enumerate(codon_list[key]):
                # If the codon is UAA, UGA, or UAG, add the index of the codon to the respective key in the stops dict.
                if item in stop_codes:
                    stops[key].append(index)
                # If the codon is AUG, add the index to the respective key in the starts dictionary.
                elif item == start_code:
                    starts[key].append(index)
        return starts, stops

    # Class method that uses start_stop results to find subsequences in the form of Start-AminoAcids-Stop of min_length.
    def valid_subsequences(self, min_length=0):
        starts, stops = self.start_stop()
        subsequences = {
            0: [], 1: [], 2: []
        }
        # For each frame, loop through the stops and starts and conditionally add pairs of valid subsequences to dict.
        for key in starts:
            previous = 0
            for stop in stops[key]:
                for start in starts[key]:
                    # Only appends [start, stop] if the start is after the previous stop and range start-stop > min_len.
                    if start > previous and start + min_length < stop:
                        subsequences[key].append([start, stop])
                previous = stop
        # Using codons class method to grab all possible codons.
        frames = self.codons()
        # Counter used for formatting output.
        subsequence_count = 1
        print("Here's a list of all valid subsequences in your sequence:")
        for key in frames:
            # For each valid subsequence, create the polypeptide string and print out information pertaining to it.
            for index, sub in enumerate(subsequences[key]):
                valid_aa = polypeptide(frames[key][sub[0]:sub[1]+1])
                print(f'Subsequence: {subsequence_count:>2d}  |'
                      f'  Frame: {key + 1}  |'
                      f' Length: {sub[1]-sub[0]:>2d}  |'
                      f' Range: {subsequences[key][index]}  |'
                      f' {valid_aa}')

                subsequence_count = subsequence_count+1
        return subsequences


# Utilizing function from other script to take mRNA and convert into polypeptide chain.
def polypeptide(rna):
    peptide_chain = []
    codon_table = {

        'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
        'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
        'UAU': 'Y', 'UAC': 'Y', 'UAA': '*', 'UAG': '*',
        'UGU': 'C', 'UGC': 'C', 'UGA': '*', 'UGG': 'W',
        'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
        'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
        'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
        'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
        'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
        'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
        'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
        'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
        'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
    }
    if isinstance(rna, list):
        # For each 3 nucleotide pairing, append the corresponding AA to the list peptide_chain.
        for item in rna:
            peptide_chain.append(codon_table[item])
        poly = '-'.join(peptide_chain)
    else:
        for nucleotide in range(int(len(rna)/3)):
            codon = rna[3 * nucleotide:3 * nucleotide+3]
            peptide_chain.append(codon_table[codon])
        poly = '-'.join(peptide_chain)
    return poly


# Example usage of the class using the variable sequence.
def main():

    sequence = 'AGATTAATGACAATGAGATTCATCAGTTTAACAAAAACAACTCCAATCAAGCAGTAGCTGTAACTT' \
               'TCACAAAGTGTGAAGAAGAACCTTTAGATTTAATTACAAGTCTTCAGAATGCCAGAGATATACAGGA' \
               'TATGCGAATTAAGAAGAAACAAAGGCAACGCGTCTTTCCACAGCCAGGCAGTCTGTATCTTGCAAAA' \
               'ACATCCACTCTGCCTCGAATCTCTCTGAAAGCAGCAGTAGGAGGCCAAGTTCCCTCTGCGTGTTCTC' \
               'ATAAACAGCTGTATACGTATGGCGTTTCTAAACATTGCATAAAAATTAACAGCAAAAATGCAGAGTC' \
               'TTTTCAGTTTCACACTGAAGATTATTTTGGTAAGGAAAGTTTATGGACTGGAAAAGGAATACAGTTG' \
               'GCTGATGGTGGATGGCTCATACCCTCCAATGATGGAAAGGCTGGAAAAGAAGAATTTTATAGGGCTC' \
               'TGTGTGACACTCCAGGTGTGGATCCAAAGCTTATTTCTAGAATTTGGGTTTATAATCACTATAGATG' \
               'GATCATATGGAAACTGGCAGCTATGGAATGTGCCTTTCCTAAGGAATTTGCTAATAGATGCCTAAGC' \
               'CCAGAAAGGGTGCTTCTTCAACTAAAATACAGATATGATACGGAAATTGATAGAAGCAGAAGATCGG' \
               'CTATAAAAAAGATAATGGAAAGGGATGACACAGCTGCAAAAACACTTGTTCTCTGTGTTTCTGACAT' \
               'AATTTCATTGAGCGCAAATATATCTGAAACTTCTAGCAATAAAACTAGTAGTGCAGATACCCAAAAA' \
               'GTGGCCATTATTGAACTTACAGATGGGTGGTATGCTGTTAAGGCCCAGTTAGATCCTCCCCTCTTAG' \
               'CTGTCTTAAAGAATGGCAGACTGACAGTTGGTCAGAAGATTATTCTTCATGGAGCAGAACTGGTGGG' \
               'CTCTCCTGATGCCTGTACACCTCTTGAAGCCCCAGAATCTCTTATGTTAAAGATTTCTGCTAACAGT' \
               'ACTCGGCCTGCTCGCTGGTATACCAAACTTGGAAGTA'
    my_sequence = DNA(sequence)
    my_sequence.valid_subsequences()



if __name__ == '__main__':
    main()
