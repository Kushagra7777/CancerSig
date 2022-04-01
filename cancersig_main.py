#!/usr/bin/python
import argparse
import os
import csv

def parse_arguments():
    str = 'CancerSig obtains a small set of miRNA biomarkers as a signature and establishes a panel of miRNAs to predict cancer stage across 15 cancer types. '
    parser = argparse.ArgumentParser(prog='cancersig_main.py', description=str)
    parser.add_argument("-t", required=True, help="choose one of the cancer type(BLCA, BRCA, COAD, ESCA, HNSC, KIRC, KIRP, LIHC, LUAD, LUSC, READ, SKCM, STAD, THCA, UVM)")
    parser.add_argument("-i", required=True, help="the file of miRNA gene expression for specific cancer type")

    return parser

def main(args=None):
    args = parse_arguments().parse_args(args)
    cancer_type = args.t
    expression = args.i
    svmpredict = "libsvm/svm-predict"
    svmscale = "libsvm/svm-scale"
    if os.path.exists(svmpredict):
        print("svm-predict exist:" + svmpredict)
    else:
        print("svm-predict doesn't exist, please build it in libsvm folder")
        quit()
    if os.path.exists(svmscale):
        print("svm-scale exist:" + svmscale)
    else:
        print("svm-scale doesn't exist, please build it in libsvm folder")
        quit()
    print('cancer type:' + cancer_type)
    print('expression file:' + expression)
    svm_format = expression + ".svm"
    wfile = open(svm_format, "w")
    wfile.write('0 ')
    f_no = 1
    #efile = open(expression, "r")
    with open(expression, "r") as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)
        for row in csvreader:
            miRNA_expression = row[1]
            wfile.write(str(f_no) + ":" + miRNA_expression + " ")
            f_no += 1
    
    wfile.close()
    model = ""
    scale = ""
    if cancer_type == "BLCA":
        model = "models/BLCA/BLCA.model"
        scale = "models/BLCA/BLCA.feature.scale"
    elif cancer_type == "LUAD":
        model = "models/LUAD/LUAD.model"
        scale = "models/LUAD/LUAD.feature.scale"
    elif cancer_type == "KIRP":
        model = "models/LUAD/LUAD.model"
        scale = "models/LUAD/LUAD.feature.scale"
    elif cancer_type == "COAD":
        model = "models/COAD/COAD.model"
        scale = "models/COAD/COAD.feature.scale"
    elif cancer_type == "ESCA":
        model = "models/ESCA/ESCA.model"
        scale = "models/ESCA/ESCA.feature.scale"
    elif cancer_type == "HNSC":
        model = "models/HNSC/HNSC.model"
        scale = "models/HNSC/HNSC.feature.scale"
    elif cancer_type == "KIRC":
        model = "models/KIRC/KIRC.model"
        scale = "models/KIRC/KIRC.feature.scale"
    elif cancer_type == "LUSC":
        model = "models/LUSC/LUSC.model"
        scale = "models/LUSC/LUSC.feature.scale"
    elif cancer_type == "READ":
        model = "models/READ/READ.model"
        scale = "models/READ/READ.feature.scale"
    elif cancer_type == "SKCM":
        model = "models/SKCM/SKCM.model"
        scale = "models/SKCM/SKCM.feature.scale"
    elif cancer_type == "STAD":
        model = "models/STAD/STAD.model"
        scale = "models/STAD/STAD.feature.scale"
    elif cancer_type == "THCA":
        model = "models/THCA/THCA.model"
        scale = "models/THCA/THCA.feature.scale"
    elif cancer_type == "UVM":
        model = "models/UVM/UVM.model"
        scale = "models/UVM/UVM.feature.scale"
    elif cancer_type == "BRCA":
        model = "models/BRCA/BRCA.model"
        scale = "models/BRCA/BRCA.feature.scale"
    elif cancer_type == "LIHC":
        model = "models/LIHC/LIHC.model"
        scale = "models/LIHC/LIHC.feature.scale"
    else:
        print("Please type the correct cancer type")
        quit()

    if os.path.exists(model):
        print("model exist:" + model)
    else:
        print("model doesn't exist:" + model)
        quit()
    svm_format_scl = svm_format + ".scl"
    svm_prediction_results = svm_format_scl + ".predict"
    cmd = svmscale + " -r " + scale + " " + svm_format + " > " + svm_format_scl
    os.system(cmd)
    cmd = svmpredict + " -b 1 -q " + svm_format_scl + " " + model + " " + svm_prediction_results
    os.system(cmd)
    rfile = open(svm_prediction_results,"r")
    for line in rfile:
        clean_line = line.rstrip('\r\n')
        ele = clean_line.split(' ')
        labels = ele[0]
        if labels == 'labels':
            continue
        prediction_score = ele[1]
    print("prediction score:" + prediction_score)

    

        


if __name__ == "__main__":
    main()