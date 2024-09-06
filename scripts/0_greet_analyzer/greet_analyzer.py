from example_bsm import f

def initialize_args():
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument(
        "--name",
        required=True,
        help="Who the code should greet"
    )
    parser.add_argument(
        "-n",
        default=1,
        help="How many times to greet the person"
    )

def main(args=None):
    if args is None:
        args = initialize_args()
    for _ in range(args.n):
        f(args.name)

if __name__=="__main__":
    main()
