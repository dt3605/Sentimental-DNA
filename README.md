Sentimental DNA

This is a project from the CS50x course.
The goal is to identify an individual from their DNA sequence by comparing Short Tandem Repeats (STRs) counts with a database of known individuals.

What it does

Reads a CSV file containing STR counts for multiple individuals.
Reads a text file containing a DNA sequence to identify.
Computes the longest run of each STR in the DNA sequence.
Compares the STR counts with those in the CSV database.
Prints the name of the matching individual, or No match if none match.

How to use
Organize your files as follows:

sentimental-dna/
├── dna.py
├── databases/
│   ├── small.csv
│   └── large.csv
└── sequences/
    ├── 1.txt
    ├── 2.txt
    └── ... (up to 20.txt)


Run the program with:

python dna.py databases/small.csv sequences/1.txt

The program will print either the name of the matching individual or No match.

About
This project helps practice:
Reading CSV and text files in Python.
Working with strings and sequences.
Using loops, conditionals, and functions.
Implementing a simple algorithm to match DNA sequences.

CS50x — Introduction to Computer Science by Harvard University
Project by Davi Teodoro
