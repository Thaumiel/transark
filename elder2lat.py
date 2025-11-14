#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# elder2lat.py – translittererar Elder Futhark-runor till latinska tecken
# användning: ./elder2lat.py "ᚠᚢᚦᚨᚱᚲ"

import sys

rune_to_latin = {
    'ᚠ': 'f', 'ᚢ': 'u', 'ᚦ': 'þ', 'ᚨ': 'a', 'ᚱ': 'r', 'ᚲ': 'k',
    'ᚷ': 'g', 'ᚹ': 'w', 'ᚺ': 'h', 'ᚾ': 'n', 'ᛁ': 'i', 'ᛃ': 'j',
    'ᛇ': 'y', 'ᛈ': 'p', 'ᛉ': 'z', 'ᛋ': 's', 'ᛏ': 't', 'ᛒ': 'b',
    'ᛖ': 'e', 'ᛗ': 'm', 'ᛚ': 'l', 'ᛜ': 'ng', 'ᛞ': 'd', 'ᛟ': 'o'
}

def to_latin(text):
    return ''.join(rune_to_latin.get(ch, ch) for ch in text)

def main():
    if len(sys.argv) > 1:
        text = ' '.join(sys.argv[1:])
    else:
        text = sys.stdin.read().strip()

    print(to_latin(text))

if __name__ == "__main__":
    main()