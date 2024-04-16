import argparse
import sys
import os
import subprocess
import textwrap

try:
    from Bio import SeqIO
except:
    print("SeqIO module is not installed! Please install SeqIO and try again.")
    sys.exit()

try:
    import tqdm
except:
    print("tqdm module is not installed! Please install tqdm and try again.")
    sys.exit()

parser = argparse.ArgumentParser(prog='python seq_fetch_by_length.py',
                                 formatter_class=argparse.RawDescriptionHelpFormatter,
                                 epilog=textwrap.dedent('''\

# seq_fetch_by_length

Author: Murat Buyukyoruk

        seq_fetch_by_length help:

This script is developed to fetch sequences based on their length from a multifasta file. 

SeqIO package from Bio is required to fetch flank sequences. Additionally, tqdm is required to provide a progress bar since some multifasta files can contain long and many sequences.

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

      	'''))
parser.add_argument('-i', '--input', required=True, type=str, dest='filename',
                    help='Specify a original fasta file.\n')
parser.add_argument('-o', '--output', required=True, dest='out',
                    help='Specify a output fasta file name.\n')
parser.add_argument('-l', '--length', required=True, dest='length', type=int,
                    help='Specify a length for sequences.\n')

results = parser.parse_args()
filename = results.filename
leng = results.length
out = results.out

seq_id_list = []
seq_list = []
seq_description_list = []

os.system('> ' + out)

proc = subprocess.Popen("grep -c '>' " + filename, shell=True, stdout=subprocess.PIPE, text=True)
length = int(proc.communicate()[0].split('\n')[0])

with tqdm.tqdm(range(length)) as pbar:
    pbar.set_description('Reading...')
    f = open(out, 'a')
    sys.stdout = f
    for record in SeqIO.parse(filename, "fasta"):
        pbar.update()
        if len(record.seq) >= leng:
            print(record.format("fasta"))




