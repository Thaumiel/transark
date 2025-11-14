#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# younger2lat.py – translittererar Younger Futhark-runor till latinska tecken
# användning: ./younger2lat.py "ᚠᚢᚦᚬᚱᚴ"

import sys

rune_to_latin = {
    'ᚠ': 'f', 'ᚢ': 'u', 'ᚦ': 'þ', 'ᚬ': 'a', 'ᚭ': 'å', 'ᚯ': 'ø',
    'ᚱ': 'r', 'ᚴ': 'k', 'ᚼ': 'h', 'ᚾ': 'n', 'ᛁ': 'i', 'ᛅ': 'æ',
    'ᛋ': 's', 'ᛏ': 't', 'ᛒ': 'b', 'ᛘ': 'm', 'ᛚ': 'l', 'ᛜ': 'ng', 'ᛦ': 'y'
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
