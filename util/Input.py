import argparse
def init():
    global kwd, limit
parser = argparse.ArgumentParser(description='Social media data extraction.')
parser.add_argument("-k", "--keyword", type=str, required=True, dest='kwd', help='Enter a keyword to search')
parser.add_argument("-l", "--limits", type=int, default=20, dest='limit', help='number of results to return')
args = parser.parse_args()
kwd =args.kwd
limit=args.limit
