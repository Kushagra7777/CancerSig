# CancerSig

**CancerSig**: This work proposes an evolutionary learning method called CancerSig to identify stage-specific miRNA signatures for cancer stage prediction. CancerSig obtains a small set of miRNA biomarkers as a signature and establishes a panel of miRNAs to predict cancer stage across 15 cancer types.

## Input Data

CSV format (e.g., [BLCA_input.csv](models/BLCA/BLCA_input.csv))

## Getting start

```shell
git clone https://github.com/mingjutsai/CancerSig.git
cd CancerSig
```

build LIBSVM

```shell
cd src/libsvm
make
```

## Options of CancerSig

```shell
python cancersig_main.py -h
usage: cancersig_main.py [-h] -t T -i I

CancerSig obtains a small set of miRNA biomarkers as a signature and establishes a panel of miRNAs to predict cancer stage across 15 cancer
types.

optional arguments:
  -h, --help  show this help message and exit
  -t T        choose one of the cancer type(BLCA, BRC, COAD, ESCA, HNSC, KIRC, KIRP, LIHC, LUAD, LUSC, READ, SKCM, STAD, THCA, UVM)
  -i I        the file of miRNA gene expression for specific cancer type
```

## Example of running CancerSig

```shell
python cancersig_main.py -t BLCA -i models/BLCA/BLCA_input.csv
```

## Contact

- Srinivasulu Yerukala Sathipati: sathipathi.srinivasulu@marshfieldclinic.org
- Ming-Ju Tsai: mingjutsai@hsl.harvard.edu
