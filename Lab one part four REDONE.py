
# Write a program that performs the following actions:
# - Asks the user to enter a sequence of one-letter amino acid codes (see this chart).
# - Display the same sequence as a list of three-letter amino acid codes separated by dashes. For example, if the
# user enters “GGLYS”, the output of your program should be “Gly-Gly-Leu-Tyr-Ser”. For full credit, you must
# employ a “for” loop somewhere in your code

# User input of characters responding to one-letter amino acid chain.
Sequence = input("What's that amino acid sequence?         (NOTE: IF YOU PICK A LETTER THAT DOESNT CORRESPOND TO AN AA IT WILL BE OMITTED!\n")

# Ensuring uniformity in the string before we convert from 1 to 3 character codes.
capitalized_sequence = Sequence.upper()

# New list to store resulting chain.
newseq = []

code_dictionary = {
    'G':'Gly',
    'P':'Pro',
    'H':'His',
    'V':'val',
    'R':'Arg',
    'E':'Glu',
    'L':'Leu',
    'F':'Phe',
    'D':'Asp',
    'I':'Ile',
    'M':'Met',
    'C':'Cys',
    'T':'Thr',
    'Y':'Tyr',
    'W':'Trp',
    'S':'Ser',
    'K':'Lys',
    'A':'Ala',
    'Q':'Gln',
    'N':'Asn'
}
# Employing for loop to iterate across string, using if statement to ensure any non AA characters are omitted.
for letter in capitalized_sequence:
    if letter in code_dictionary:
        newseq.append(code_dictionary[letter])

# Taking list of 3- letter AA code and using join to create string object.
newseq2 = '-'.join(newseq)
# Printing the new sequence, using newline character to separate the responses.
print('Your sequence of amino acids is \n'  + newseq2 + '.')
