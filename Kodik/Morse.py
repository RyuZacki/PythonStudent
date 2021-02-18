
MorseAlphabet = ['*-', '-***', '*-*-', '-**', '*', '**-*',
                 '--*', '****', '**', '*---', '-*-', '*-**',
                 '--', '-*', '---', '*--*', '--*-', '*-*',
                 '***', '-', '**-', '***-', '*--', '-**-',
                 '-*--', '--**', '**--**-*']
Alphabet = ['A', 'B', 'C', 'D', 'E', 'F',
            'G', 'H', 'I', 'J', 'K', 'L',
            'M', 'N', 'O', 'P', 'Q', 'R',
            'S', 'T', 'U', 'V', 'W', 'X',
            'Y', 'Z', ' ']


def Adding(CyrillicValue, MorseValue):
    for i in MorseAlphabet:
        if MorseValue == i:
            Position = MorseAlphabet.index(i)
            Letter = Alphabet[Position]
            CyrillicValue += Letter


def Translate(MorseValue1, CyrillicValue):
    Cycle1 = True
    Morse = ''
    while Cycle1:
        Text = input()
        if Text == 'a':
            Adding(CyrillicValue, Morse)
            Morse = ''
        elif Text == 'e':
            Cycle1 = False
        elif len(Text) == 1:
            MorseValue1 += '*'
            Morse += '*'
        elif len(Text) > 1:
            MorseValue1 += '-'
            Morse += '-'


Cycle = True
Cycle2 = True
Cycle33 = True
while Cycle2:
    Cyrillic = ''
    MorseAlphabet = ''
    while Cycle33:
        print(Cyrillic)
        print(MorseAlphabet)
        Value = input('R: ')
        if Value == 'r':
            Cycle33 = False
        else:
            Translate(MorseAlphabet, Cyrillic)

    print(Cyrillic)
    print(MorseAlphabet)
    Cycle2 = False
