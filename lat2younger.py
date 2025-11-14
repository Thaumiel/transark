#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# lat2younger.py – translittererar latinsk text till Younger Futhark (vikingatida runor)
# användning: ./lat2younger.py "text att översätta"

import sys

latin_to_rune = {
    'f': 'ᚠ', 'v': 'ᚠ', 'u': 'ᚢ', 'w': 'ᚢ',
    'þ': 'ᚦ', 'th': 'ᚦ', 'ð': 'ᚦ',
    'a': 'ᚬ', 'o': 'ᚬ', 'å': 'ᚭ', 'æ': 'ᛅ', 'ä': 'ᛅ', 'e': 'ᛁ',
    'r': 'ᚱ', 'k': 'ᚴ', 'g': 'ᚴ',
    'h': 'ᚼ', 'n': 'ᚾ', 'i': 'ᛁ', 'j': 'ᛁ', 'y': 'ᛦ',
    'p': 'ᛒ', 'b': 'ᛒ', 't': 'ᛏ', 'd': 'ᛏ',
    's': 'ᛋ', 'l': 'ᛚ', 'm': 'ᛘ', 'ŋ': 'ᛜ',
    'ø': 'ᚯ', 'ö': 'ᚯ'
}

def to_runes(text):
    text = text.lower()
    out = ''
    i = 0
    while i < len(text):
        if text[i:i+2] in latin_to_rune:
            out += latin_to_rune[text[i:i+2]]
            i += 2
        elif text[i] in latin_to_rune:
            out += latin_to_rune[text[i]]
            i += 1
        else:
            out += text[i]
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
