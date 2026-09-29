# Rosalind Bioinformatics Armory

A collection of my Python solutions to problems from the [Rosalind
Bioinformatics
Armory](https://rosalind.info/problems/list-view/?location=bioinformatics-armory).

This repository is part of my practice in **bioinformatics,
computational biology, Python programming, and biological data
analysis**.

## About

The Rosalind Bioinformatics Armory focuses on using existing
bioinformatics tools, libraries, databases, and programming resources to
solve biological problems.

The problems in this repository cover areas such as:

-   Biological sequence analysis
-   FASTA and GenBank formats
-   NCBI databases and Entrez
-   Biopython
-   Sequence parsing and manipulation
-   Biological data processing
-   Computational biology workflows

## Repository Structure

``` text
rosalind-bioinformatics-armory/
│
├── README.md
├── requirements.txt
│
├── FRMT/
│   ├── input.txt
│   └── solution.py
│
├── [PROBLEM_ID]/
│   ├── input.txt
│   └── solution.py
│
└── ...
```

Each problem is organized into its own directory.

Typical files include:

-   `input.txt` --- input data for the problem
-   `solution.py` --- Python implementation of the solution

Additional files may be included when a problem requires them.

## Problems Solved

  till now 4 problems have been solved.
  ------------------------------------------------------------------------------------------

This table will be updated as more problems are completed.

## Technologies

-   **Python 3**
-   **Biopython**
-   **NCBI Entrez**
-   Python standard library

## Installation

Clone the repository:

``` bash
git clone https://github.com/YashrajManan/rosalind-bioinformatics-armory.git
cd rosalind-bioinformatics-armory
```

Create a virtual environment:

### Windows

``` bash
python -m venv venv
venv\Scripts\activate
```

### Linux/macOS

``` bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

``` bash
pip install -r requirements.txt
```

## Running a Solution

Navigate to the relevant problem directory:

``` bash
cd FRMT
```

Run the solution:

``` bash
python solution.py
```

Solutions that use external databases or APIs may require an active
internet connection.

## Example: FRMT - Data Formats

The FRMT problem provides GenBank accession IDs and asks for the
shortest associated sequence in FASTA format.

The workflow is:

``` text
Accession IDs
      ↓
NCBI Nucleotide Database
      ↓
Retrieve records
      ↓
Parse FASTA using Biopython
      ↓
Compare sequence lengths
      ↓
Select shortest sequence
      ↓
Output FASTA record
```

For example, the shortest record can be selected with:

``` python
shortest = min(records, key=lambda record: len(record.seq))
```

This uses Python's `min()` function with a key function to select the
`SeqRecord` having the smallest sequence length.

## Learning Goals

The main purpose of this repository is to build practical experience
with:

1.  Python programming for bioinformatics
2.  Biological sequence data
3.  FASTA and GenBank formats
4.  Biopython
5.  NCBI and biological databases
6.  Data parsing and processing
7.  Bioinformatics workflows
8.  Computational biology concepts

The goal is to understand both the **programming logic** and the
**biological data being processed**, rather than simply obtaining
accepted solutions.

## Progress

This repository is a work in progress. New Rosalind Bioinformatics
Armory problems will be added as I solve them and improve my
understanding of Python and computational biology.

## References

-   [Rosalind](https://rosalind.info/)
-   [Rosalind Bioinformatics
    Armory](https://rosalind.info/problems/list-view/?location=bioinformatics-armory)
-   [Biopython](https://biopython.org/)
-   [NCBI](https://www.ncbi.nlm.nih.gov/)

## Disclaimer

This repository is intended for educational and learning purposes.

Problem statements, biological records, and external database resources
belong to their respective providers. The code in this repository
represents my own implementations and may be revised as my understanding
and programming skills improve.

## License

This repository is intended primarily as an educational project.
