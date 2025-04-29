from itertools import chain

# https://ru.wikipedia.org/wiki/Греческий_алфавит#Буквы (24 буквы)
up_gr_symb=['Α', 'Β', 'Γ', 'Δ', 'Ε', 'Ζ', 'Η', 'Θ', 'Ι', 'Κ', 'Λ', 'Μ', 'Ν', 'Ξ', 'Ο', 'Π', 'Ρ', 'Σ', 'Τ', 'Υ', 'Φ', 'Χ', 'Ψ', 'Ω']
lw_gr_symb=['α', 'β', 'γ', 'δ', 'ε', 'ζ', 'η', 'θ', 'ι', 'κ', 'λ', 'μ', 'ν', 'ξ', 'ο', 'π', 'ρ', 'σ', 'τ', 'υ', 'φ', 'χ', 'ψ', 'ω']

def all_greek_symbols_print():
    """
    stackoverflow.com/questions/47956451/get-a-list-of-all-greek-unicode-characters
    """
    greek_codes   = chain(range(0x370, 0x3e2), range(0x3f0, 0x400))
    greek_symbols = (chr(c) for c in greek_codes)
    greek_letters = [c for c in greek_symbols if c.isalpha()]
    print(greek_letters)

def tst_gr_symb():
    print(f'{len(up_gr_symb)=}')
    print(f'{len(lw_gr_symb)=}')

if __name__=='__main__':
    # all_greek_symbols_print()
    tst_gr_symb()
