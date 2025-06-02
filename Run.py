import nbformat
from nbconvert import HTMLExporter, NotebookExporter
from nbconvert.preprocessors import ExecutePreprocessor
import os

# Path to your notebook
notebook_path = "mental-health-in-tech.ipynb"
output_path = "mental-health-in-tech-output.ipynb"

# Load the notebook
with open(notebook_path, "r", encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=4)

# Set up the executor
ep = ExecutePreprocessor(timeout=600, kernel_name='python3')

# Execute the notebook
ep.preprocess(nb, {'metadata': {'path': os.path.dirname(notebook_path)}})

# Save the executed notebook
with open(output_path, "w", encoding="utf-8") as f:
    nbformat.write(nb, f)

print(f"Notebook executed and saved as: {output_path}")
