# Renexp
A simple script to rename files in a folder using regular expressions.
Does not support recursive searching and renaming at the moment.

## Example usage
#### Input files: 
* 1first1.txt
* 2second2.png
* 3third3.exe
* 4fourth4.py
  
```
renexp [--sim] "[1-9]([a-z]*)[1-9](\.[a-z]+)?" "\1\2"
```

#### Output files:
* first.txt
* second.png
* third.exe
* fourth.py

\1 and \2 and equivalent to the traditionnal $1 and $2

Remember to surround the regular expressions with double quotes.

Use the __--sim__ option to simulate the execution before renaming files definitively
