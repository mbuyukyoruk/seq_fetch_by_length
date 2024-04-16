# seq_fetch_by_length

Author: Murat Buyukyoruk

        seq_fetch_by_length help:

This script is developed to fetch sequences based on their length from a multifasta file. 

SeqIO package from Bio is required to fetch flank sequences. Additionally, tqdm is required to provide a progress bar since some multifasta files can contain 
long and many sequences.

Syntax:

        python seq_fetch_by_length.py -i demo.fasta -o demo_200000bp.fasta -l 200000

seq_fetch_by_length dependencies:

Bio module and SeqIO available in this package          refer to https://biopython.org/wiki/Download

tqdm                                                    refer to https://pypi.org/project/tqdm/

Input Paramaters (REQUIRED):
----------------------------
	-i/--input		FASTA			Specify a input fasta file.

	-o/--output		FASTA			Specify a output fasta file name.

	-l/--length		Number			Specify a minimum length of sequences you would like in output fasta.

Basic Options:
--------------
	-h/--help		HELP			Shows this help text and exits the run.

