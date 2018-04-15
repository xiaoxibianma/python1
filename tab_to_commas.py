import sys


def tab_to_commas(in_file, out_file):
    with open(in_file) as inf:
        contents = inf.read()
    with open(out_file, 'wt') as ouf:
        ouf.write(contents)


if __name__ == "__main__":
    in_file = sys.argv[1]
    out_file = str(in_file).split('.')[0]
    out_file = out_file + '_commas.csv'
    tab_to_commas(in_file, out_file)
