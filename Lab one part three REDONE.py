# Write a program that performs the following actions:
# - Asks the user to enter the name of an amino acid.
# - Report to the user whether that amino acid has the following:
# aliphatic, aromatic, acidic, basic, hydroxylic, sulfurcontaining, or amidic character.

# - Make your program accept answers in a case-insensitive manner (in other words, the name can be entered
# regardless of capitalization).
# - Display a custom message letting the user know if they typed in something other than an amino acid name.

# Using a dictionary since all AA have a 1:1 relationship with the characteristics.
listAmino = {
    'Alanine': 'Aliphatic',
    'Arginine': 'Basic',
    'Asparagine': 'Amidic',
    'Aspartate':'Acidic',
    'Cysteine': 'Sulfur-Containing',
    'Dametrine': 'Secret-Containing',
    'Glutamate': 'Acidic',
    'Glutamine': 'Amidic',
    'Glycine': 'Aliphatic',
    'Histidine': 'Basic',
    'Isoleucine': 'Aliphatic',
    'Leucine':'Aliphatic',
    'Lysine': 'Basic',
    'Methionine': 'Sulfur-Containing',
    'Phenylalanine': 'Aromatic',
    'Proline': 'Aliphatic',
    'Serine': 'Hydroxylic',
    'Threonine': 'Hydroxylic',
    'Tryptophan': 'Aromatic',
    'Tyrosine': 'Aromatic',
    'Valine': 'Aliphatic',
}
# Asks user to give an amino acid.
amino_acid = input("What amino acid we goin' with today?  \n")

# Ensuring an input is formatted to proper noun syntax.
lowercase = amino_acid.lower()
capitalized = lowercase.capitalize()

# If a match is found in the dictionary.
if capitalized in listAmino.keys():
    print('Your Amino Acid,' + capitalized + f' is: {listAmino[capitalized]}')
# If no match is found.
else:
    print("This is not a valid Amino acid, Try again!")