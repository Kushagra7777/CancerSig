# CancerSig

**CancerSig**: This work proposes an evolutionary learning method called CancerSig to identify stage-specific miRNA signatures for cancer stage prediction. CancerSig obtains a small set of miRNA biomarkers as a signature and establishes a panel of miRNAs to predict cancer stage across 15 cancer types.

## Input Data

CSV format with miRNA expression (RPM log2). User can put their in-house miRNA expression into csv file.
| Dataset                               | Abbreviation | miRNA panel                |
|---------------------------------------|--------------|----------------------------|
| Bladder urothelial carcinoma          | BLCA         | [BLCA_input.csv](models/BLCA/BLCA_input.csv) |
| Breast invasive carcinoma             | BRCA         | [BRCA_input.csv](models/BRCA/BRCA_input.csv) |
| Colon adenocarcinoma                  | COAD         | [COAD_input.csv](models/COAD/COAD_input.csv) |
| Esophageal Carcinoma                  | ESCA         | [ESCA_input.csv](models/ESCA/ESCA_input.csv) |
| Head and neck squamous cell carcinoma | HNSC         | [HNSC_input.csv](models/HNSC/HNSC_input.csv) |
| Kidney renal clear cell carcinoma     | KIRC         | [KIRC_input.csv](models/KIRC/KIRC_input.csv) |
| Kidney renal papillary cell carcinoma | KIRP         | [KIRP_input.csv](models/KIRP/KIRP_input.csv) |
| Liver hepatocellular carcinoma        | LIHC         | [LIHC_input.csv](models/LIHC/LIHC_input.csv) |
| Lung adenocarcinoma                   | LUAD         | [LUAD_input.csv](models/LUAD/LUAD_input.csv) |
| Lung squamous cell carcinoma          | LUSC         | [LUSC_input.csv](models/LUSC/LUSC_input.csv) |
| Rectum adenocarcinoma                 | READ         | [READ_input.csv](models/READ/READ_input.csv) |
| Skin cutaneous melanoma               | SKCM         | [SKCM_input.csv](models/SKCM/SKCM_input.csv) |
| Stomach adenocarcinoma                | STAD         | [STAD_input.csv](models/STAD/STAD_input.csv) |
| Thyroid carcinoma                     | THCA         | [THCA_input.csv](models/THCA/THCA_input.csv) |
| Uveal melanoma                        | UVM          | [UVM_input.csv](models/UVM/UVM_input.csv)   |

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
  -t T        choose one of the cancer type(BLCA, BRCA, COAD, ESCA, HNSC, KIRC, KIRP, LIHC, LUAD, LUSC, READ, SKCM, STAD, THCA, UVM)
  -i I        the file of miRNA gene expression for specific cancer type
```

## Example of running CancerSig

```shell
python cancersig_main.py -t BLCA -i models/BLCA/BLCA_input.csv
```

## Contact

- Srinivasulu Yerukala Sathipati: sathipathi.srinivasulu@marshfieldclinic.org
- Ming-Ju Tsai: mingjutsai@hsl.harvard.edu
