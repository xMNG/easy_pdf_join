#! python3
# easy_pdf_join.py - Joins entire pdfs together easily because no open source software exists (that I can find).
# Usage: python easy_pdf_join.py --output=new_pdf.pdf --merge "pdf to merge 1" "pdf to merge 2" ...
import argparse
from PyPDF2 import PdfFileMerger

parser = argparse.ArgumentParser()
# need a filename for output
parser.add_argument('--output_file', action='store', default='new_pdf.pdf', help='Provide filename for output pdf')
# need a list for documents to merge, in order
parser.add_argument('--merge', action='append', nargs='+',
                    help='Provide filenames for pdfs to merge (in sequential order, must be in current working directory')
# parse args
args = parser.parse_args()

# pdf list as a constant
PDFS = args.merge
PDFS = [item for sublist in PDFS for item in sublist]

# init the merger class
merger = PdfFileMerger()

# add all pdfs to the merger class
for pdf in PDFS:
    merger.append(pdf)
    print(f'Merging {pdf}...')

with open(args.output_file, 'wb') as f:
    merger.write(f)

print('Merge complete.')
