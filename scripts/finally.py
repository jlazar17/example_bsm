import os
import numpy as np
import h5py as h5

def initialize_args():
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument(
        "--first_infile",
        type=str,
        required=True
    )
    parser.add_argument(
        "--next_infile",
        type=str,
        required=True
    )
    parser.add_argument(
        "--outfile",
        type=str,
        required=True
    )
    return parser.parse_args()


def main():
    args = initialize_args()
    with h5.File(args.first_infile) as h5f:
        data1 = h5f["foo"][:]

    with h5.File(args.next_infile) as h5f:
        data2 = h5f["bar"][:]

    res = data1 * data2

    if not os.path.exists(args.outfile):
        with h5.File(args.outfile, "w") as _:
            pass

    with h5.File(args.outfile, "r+") as h5f:
        if "baz" in h5f.keys():
            del h5f["baz"]
        h5f.create_dataset("baz", data=res)


if __name__=="__main__":
    main()
