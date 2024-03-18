import os
import numpy as np
import h5py as h5

def initialize_args():
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument(
        "--outfile",
        type=str,
        required=True
    )
    parser.add_argument(
        "-s",
        "--seed",
        dest="seed",
        type=int,
        required=True
    )
    return parser.parse_args()

def main():
    args = initialize_args()
    np.random.seed(args.seed)
    res = np.random.uniform(-5, 5, 1000)

    if not os.path.exists(args.outfile):
        with h5.File(args.outfile, "w") as _:
            pass

    with h5.File(args.outfile, "r+") as h5f:
        if "foo" in h5f.keys():
            del h5f["foo"]
        h5f.create_dataset("foo", data=res)

if __name__=="__main__":
    main()
