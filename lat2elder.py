#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# lat2elder.py – translittererar latinsk text till Elder Futhark-runor
# användning: ./lat2elder.py "text att översätta"

import sys

latin_to_rune = {
    'f': 'ᚠ', 'u': 'ᚢ', 'v': 'ᚢ', 'þ': 'ᚦ', 'th': 'ᚦ', 'a': 'ᚨ',
    'r': 'ᚱ', 'k': 'ᚲ', 'g': 'ᚷ', 'w': 'ᚹ', 'h': 'ᚺ', 'n': 'ᚾ',
    'i': 'ᛁ', 'j': 'ᛃ', 'y': 'ᛇ', 'p': 'ᛈ', 'z': 'ᛉ', 's': 'ᛋ',
    't': 'ᛏ', 'b': 'ᛒ', 'e': 'ᛖ', 'm': 'ᛗ', 'l': 'ᛚ', 'ŋ': 'ᛜ',
    'ng': 'ᛜ', 'd': 'ᛞ', 'o': 'ᛟ',
    # Svenska närapproximationer
    'å': 'ᚨ', 'ä': 'ᚨ', 'ö': 'ᛟ', 'æ': 'ᚨ', 'ø': 'ᛟ'
}

def to_runes(text):
    text = text.lower()
    out = ''
    i = 0
    while i < len(text):
        if text[i:i+2] in latin_to_rune:  # tvåtecken-runor
            out += latin_to_rune[text[i:i+2]]
            i += 2
        elif text[i] in latin_to_rune:
            out += latin_to_rune[text[i]]
            i += 1
        else:
            out += text[i]  # behåll skiljetecken, mellanslag etc.
            i += 1
    return out

def main():
    if len(sys.argv) > 1:
        text = ' '.join(sys.argv[1:])
    else:
        text = sys.stdin.read().strip()

    print(to_runes(text))

if __name__ == "__main__":
    main()
