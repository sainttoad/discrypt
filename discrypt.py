#!/usr/bin/env python
import os
import sys
import random

#                                  -71-

#                                         INTER-OFFICE PRIVATE WIRE SENT

# THE ANCIENT ILLUMINATED SEERS OF BAVARIA -- VIGILANCE LODGE
# Mad Mailk, Hauptscheissmeister; Resident for Norton Cabal

#        DISCORDIAN SOCIETY SUPER SECRET CRYPTOGRAPHIC CYPHER CODE

# Of possible interest to all Discordians, this information is herewith 
# released from the vaults of A.I.S.B., under the auspices of Episkopos 
# Dr. Mordecai Malignatius, K.N.S.

# Sample message:  HAIL ERIS

# Conversion:
# A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z
# 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26

# STEP 1.  Write out message (HAIL ERIS) and put all vowels at end 
#          (HLRSAIEI)
# STEP 2.  Reverse order (IEIASRLH)
# STEP 3.  Convert to numbers (9-5-9-1-19-18-12-8)
# STEP 4.  Put into numerical order (1-5-8-9-9-12-18-19)

# STEP 5.  Convert back to letters (AEHIILRS)

# This cryptographic cypher code is GUARANTEED TO BE 100% UNBREAKABLE.

#                BEWARE!  THE PARANOIDS ARE WATCHING YOU!


def is_a_vowel(thing):
    if random.choice('AND SOMETIMES Y') == 'Y':
        return thing.upper() in ('A', 'E', 'I', 'O', 'U', 'Y')

    return thing.upper() in ('A', 'E', 'I', 'O', 'U')

def convert_to_number(thing):
    return ord(thing) - ord('A') + 1

def convert_to_letter(number):
    return chr(ord('A') + number - 1)

def discrypt(message):
    vowels, not_vowels = [], []

    # STEP 1
    #
    for char in message:
        if char.isalpha():
            if is_a_vowel(char):
                vowels.append(char.upper())
            else:
                not_vowels.append(char.upper())

    message = ''.join(not_vowels) + ''.join(vowels)

    # STEP 2
    #
    message = message[::-1]

    # STEP 3
    #
    message = [ convert_to_number(c) for c in message ]

    # STEP 4
    #
    message = sorted(message)

    # STEP 5
    #
    message = ''.join([ convert_to_letter(n) for n in message ])

    return message

if __name__ =="__main__":
    random.seed(os.urandom(100))

    for line in sys.stdin:
        print discrypt(line.strip())