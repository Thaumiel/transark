# transark

## What is transark? ##

Tools for transliterating between Latin text and the Elder/Younger Futhark runic alphabets.

Each script can accept input from command-line arguments or stdin.

This is a small, focused project for experimenting with runic transliteration in Python.

## Included files ##

- **lat2elder.py**: translates latin text to the elder furthark.
- **elder2lat.py**: translates elder futhark text to latin script.
- **lat2younger.py**: translates latin text to younger furthark.
- **younger2lat.py**: translates younger futhark to latin script.

## Version history ##
### 1.0 ###
**November 14, 2025**. First functional version.

## Usage ##
`./lat2elder.py` "Your text here." \
`echo` "Your text here" `| lat2elder.py`\
`cat file | lat2elder.py`

`./elder2lat.py` "ᚢᛏᛁᚾ ᛏᚢᚱ ᚠᚱᛁᛁᛅ"\
`echo` "ᚢᛏᛁᚾ ᛏᚢᚱ ᚠᚱᛁᛁᛅ" `| elder2lat.py`\
`cat file | elder2lat.py`

`./lat2younger.py` "Your text here."\
`echo` "Your text here" `| lat2younger.py`\
`cat file | lat2younger.py`

`./younger2lat.py` "ᚢᛏᛁᚾ ᛏᚢᚱ ᚠᚱᛁᛁᛅ"\
`echo` "ᚢᛏᛁᚾ ᛏᚢᚱ ᚠᚱᛁᛁᛅ" `| younger2lat.py`\
`cat file | younger2lat.py`
