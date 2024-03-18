# How to run my analysis

First you should edit the `OUTPUTDIR` in `setup.sh`.
Then you can do:
```bash
> source setup.sh
```

All files for comparison cna be found in `/data/user/jlazar/bsm_example/data/` and will have the same name.

## 0. Run `first.py`

```bash
> python ../scripts/first.py --outfile $OUTDIR/first_output.h5 --seed 925
```

## 1. Run `next.py`

```bash
> python ../scripts/next.py --outfile $OUTDIR/next_output.h5 --seed 853
```

## 2. Run `finally.py`

```bash
> python ../scripts/finally.py --first_infile $OUTDIR/first_output.h5 --next_infile $OUTDIR/next_output.h5 --outfile $OUTDIR/finally_output.h5
```
