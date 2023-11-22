# There are seven useful metrics gathered from a user input Amino Acid chain here.
# Chain length, Molec. Mass, max/min charge, pka(sorted/unsorted) & isoelectronic points.

"""
 11/21/23
My main focus was changing possibleAA to a dict, using fstrings, changing how I
ensured non AA codes didn't affect Molec Mass, removing now unnecessary loops
due to the dictionary, and making the script & iterators more legible.
"""

aa_chain = input("I Need an AA chain if you want those stats.").lower()
non_amino = ' bjuoxz'  # Letters not assigned to an amino acid.
# Removing non amino-acid characters.
for char in non_amino:
    aa_chain = aa_chain.replace(char, '')

uaa_chain = aa_chain.upper()  # user proofing to remove case sensitivity.


# "AA": Count, Mass, COOH, NH3] Where COOH and NH3 are pKa for functional grp.
possibleAA = {
    'A': [0, 89, 2.34, 9.69], 'R': [0, 174, 2.17, 9.04],
    'E': [0, 147, 2.19, 9.67], 'G': [0, 75, 2.34, 9.60],
    'H': [0, 155, 1.82, 9.17], 'I': [0, 131, 2.36, 9.68],
    'L': [0, 131, 2.36, 9.60], 'K': [0, 146, 2.18, 8.95],
    'M': [0, 149, 2.28, 9.21], 'F': [0, 165, 1.83, 9.13],
    'T': [0, 119, 2.11, 9.62], 'W': [0, 204, 2.38, 9.39],
    'Y': [0, 181, 2.20, 9.11], 'V': [0, 117, 2.32, 9.62],
    'N': [0, 132, 2.02, 8.80], 'D': [0, 133, 1.88, 9.60],
    'C': [0, 121, 1.96, 10.28], 'Q': [0, 146, 2.17, 9.13],
    'P': [0, 115, 1.99, 10.96], 'S': [0, 105, 2.21, 9.15],
}

# functional groups with potential charges (neg on top pos on bottom).
charged_r_groups = [
     ['D', 3.65], ['E', 4.07], ['C', 8.18], ['Y', 10.07],
     ['H', 6.00], ['K', 10.53], ['R', 12.48]
]

# Counting each amino acid
for key in possibleAA:  # for each amino acid.
    possibleAA[key][0] = uaa_chain.count(key)  # count occurrences and assign.

# Molec Mass calculation Note: AA1+AA2 removes water (18 Da) via hydrolysis.
molar_mass = (-18 * (len(uaa_chain)-1))  # -18 * total hydrolysis reactions.
for key in possibleAA:
    molar_mass = molar_mass + (possibleAA[key][0] * possibleAA[key][1])
    # Molec Mass polypeptide = current + (# AA * Molec Mass peptide).
# Max/Min charge calculation
max_charge = 1
min_charge = -1
# Max charge is 1 by default + 1 * number of R,H,K amino acids.
for charged in range(3):
    max_charge = max_charge + uaa_chain.count(charged_r_groups[charged+4][0])

# Min charge is similar except we are subtracting one for each Y,D,C,E AA.
for charged in range(4):

    min_charge = min_charge - uaa_chain.count(charged_r_groups[charged][0])

# pKa list calculations
pka_list = []  # we want a list of pKas that will help us estimate pI.
firstAA = uaa_chain[0]  # First one only one to have N terminus. 
pka_list.append(possibleAA[firstAA][3])

lastAA = uaa_chain[-1:]  # Last AA only one to have C terminus.
pka_list.append(possibleAA[lastAA][2])

for charged_aminos in charged_r_groups:
    # for each charged side group AA...
    for count in range(uaa_chain.count(charged_aminos[0])):
        # for the number of that charged side group AA...
        pka_list.append(charged_aminos[1])  # append the pka value.

# Isoelectric point estimation, uses pKa values.
sortList = sorted(pka_list)
# pI = (pka + pkb)/2
isoelectronic_point = (sortList[max_charge-1] + sortList[max_charge])/2

print(f'The chain length is : {len(uaa_chain)}')
print(f'The Molecular Mass is : {molar_mass} Da')
print(f'The maximum charge is :{max_charge}')
print(f'The minimum charge is : {min_charge}')
print('\nThis is the unsorted pKa list:')   # that new line looking nice!
print(pka_list)
print("\nThis is the sorted list of pKa's:")
print(sorted(pka_list))
print(f'\nThe isoelectronic point of this chain is: {isoelectronic_point:.2f}')
