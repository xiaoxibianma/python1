import sys
import pandas as pd


def re_order(in_file, out_file):
    df = pd.read_csv(in_file)
    idex = list(df.columns.values)
    title = [idex[1], idex[0]]
    for i in idex:
        if i not in title:
            title.append(i)
    df = df.reindex(columns=title)
    df.to_csv(out_file, encoding='utf-8', index=False)


if __name__ == "__main__":
    in_file = sys.argv[1]
    out_file = sys.argv[2]
    re_order(in_file, out_file)
