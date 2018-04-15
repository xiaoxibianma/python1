
import sys
import pandas as pd


def re_sort(in_file, out_file):
    df = pd.read_csv(in_file)
    idex = list(df.columns.values)
    af = df.sort_values(idex[1])
    af.to_csv(out_file, encoding='utf-8', index=False)


if __name__ == "__main__":
    in_file = sys.argv[1]
    out_file = str(in_file).split('.')[0]
    out_file = out_file + '_sort.csv'
    re_sort(in_file, out_file)
