import os
import nbformat
from nbconvert import HTMLExporter


def convert_notebook(eda_in_path, eda_out_path, **kwargs):

    print(' => Executing EDA notebook')
    curdir = os.path.abspath(os.getcwd())
    indir, _ = os.path.split(eda_in_path)
    outdir, _ = os.path.split(eda_out_path)
    os.makedirs(outdir, exist_ok=True)

    config = {
        "ExecutePreprocessor": {"enabled": True},
        "TemplateExporter": {"exclude_output_prompt": True, "exclude_input": True, "exclude_input_prompt": True},
    }

    nb = nbformat.read(open(eda_in_path), as_version=4)
    html_exporter = HTMLExporter(config=config)

    # change dir to notebook dir, to execute notebook
    os.chdir(indir)
    body, resources = (
        html_exporter
        .from_notebook_node(nb)
    )

    # change back to original directory
    os.chdir(curdir)

    with open(eda_out_path, 'w') as fh:
        fh.write(body)
    
    print(' => Done! See the result HTML file in ' + eda_out_path)
    
def convert_notebook_report(report_in_path, report_out_path, **kwargs):

    print(' => Executing Report notebook')
    curdir = os.path.abspath(os.getcwd())
    indir, _ = os.path.split(report_in_path)
    outdir, _ = os.path.split(report_out_path)
    os.makedirs(outdir, exist_ok=True)

    config = {
        "ExecutePreprocessor": {"enabled": True},
        "TemplateExporter": {"exclude_output_prompt": True, "exclude_input": True, "exclude_input_prompt": True},
    }

    nb = nbformat.read(open(report_in_path), as_version=4)
    html_exporter = HTMLExporter(config=config)
    
    # Preparing the manual runned 
    
    
    
    # change dir to notebook dir, to execute notebook
    os.chdir(indir)
    body, resources = (
        html_exporter
        .from_notebook_node(nb)
    )

    # change back to original directory
    os.chdir(curdir)

    with open(report_out_path, 'w') as fh:
        fh.write(body)
    
    print(' => Done! See the result HTML file in ' + report_out_path)
    
