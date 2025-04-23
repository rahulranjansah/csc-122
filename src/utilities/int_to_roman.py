# """
#    * Write a succinct, meaningful description of the file here. You should avoid wordiness
#    * and redundancy.
#    *
#    * Bugs: (a list of bugs and / or other issues)
#    *
#    * @author Rahul Ranjan Sah
#    * @date   01/15/2025
# """

#
# We limit Roman numerals to between 1 and 5999, inclusive.
LOWER_ROMAN_LIMIT = 1
UPPER_ROMAN_LIMIT = 5999

# TODO: thousands, hundreds, tens, ones


def to_thousands(num):
    val_thousands = ''
    dict_romans = {1000: "M"}
    for value in (dict_romans.keys()):
        while num >= value:
            num -= value
            val_thousands += dict_romans[value]

    return val_thousands, num

def to_hundreds(num):
    val_hundreds = ''
    dict_romans = {900: "CM", 500: "D", 400: "CD", 100: "C"}
    for value in (dict_romans.keys()):
        while num >= value:
            num -= value
            val_hundreds += dict_romans[value]

    return val_hundreds, num

def to_tens(num):
    val_tens = ''
    dict_romans = {90: "XC", 50: "L", 40: "XL", 10:"X"}
    for value in (dict_romans.keys()):
        while num >= value:
            num -= value
            val_tens += dict_romans[value]

    return val_tens, num

def to_ones(num):
    val_ones = ''
    dict_romans = {9: "IX", 5: "V", 4: "IV", 1: "I"}
    for value in dict_romans.keys():
        while num >= value:
            num -= value
            val_ones += dict_romans[value]

    return val_ones



def to_roman(n : int) -> str:

    #     """Convert an input integer to its Roman Numeral representation.
    #         e.g., 1 -> I, 4 -> IV
    if n < LOWER_ROMAN_LIMIT or n > UPPER_ROMAN_LIMIT:
        return ''

    val_thousands, num = to_thousands(n)
    val_hundreds, num = to_hundreds(num)
    val_tens, num = to_tens(num)
    val_ones = to_ones(num)

    return val_thousands + val_hundreds + val_tens + val_ones

