import pandas as pd
import subprocess

# Path settings
input_file = "models/BRCA/20250327_rpm_matrix_mapped.csv"
output_file = "models/BRCA/cancersig_results.txt"
script_path = "cancersig_main.py"
cancer_type = "BRCA"

# Load the expression matrix
df = pd.read_csv(input_file)

# Get sample names (columns) excluding 'miRNA'
sample_names = [col for col in df.columns if col != 'miRNA']

with open(output_file, "w") as out_f:
    for sample in sample_names:
        # Save current sample as a temporary input CSV
        temp_input_path = "models/BRCA/temp_single_sample.csv"
        temp_df = df[['miRNA', sample]]

        temp_df.to_csv(temp_input_path, index=False)

        # Run the command
        cmd = ["python", script_path, "-t", cancer_type, "-i", temp_input_path]
        result = subprocess.run(cmd, capture_output=True, text=True)

        # Write the output
        out_f.write(f"=== Sample: {sample} ===\n")
        out_f.write(result.stdout)
        out_f.write("\n\n")
