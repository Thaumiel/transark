Tools for transliterating between Latin text and the Elder/Younger Futhark runic alphabets.

Includes:
- lat2elder.py: translates latin text to the elder furthark.
- elder2lat.py: translates elder futhark text to latin script.
- lat2younger.py: translates latin text to younger furthark.
- younger2lat.py: translates younger futhark to latin script.

Each script can accept input from command-line arguments or stdin.

This is a small, focused project for experimenting with runic transliteration in Python.

Usage: 
./lat2elder.py "Your text here."
echo "Your text here" | lat2elder.py
cat file | lat2elder.py

./elder2lat.py "ᚢᛏᛁᚾ ᛏᚢᚱ ᚠᚱᛁᛁᛅ"
echo "ᚢᛏᛁᚾ ᛏᚢᚱ ᚠᚱᛁᛁᛅ" | elder2lat.py
cat file | elder2lat.py

./lat2younger.py "Your text here."
echo "Your text here" | lat2younger.py
cat file | lat2younger.py

./younger2lat.py "ᚢᛏᛁᚾ ᛏᚢᚱ ᚠᚱᛁᛁᛅ"
echo "ᚢᛏᛁᚾ ᛏᚢᚱ ᚠᚱᛁᛁᛅ" | younger2lat.py
cat file | younger2lat.py
