import click

from mosamatic.pipelines import DefaultPipeline
from mosamatic.utils import param_dict_from_params


@click.command(help='Runs default body composition pipeline')
@click.option(
    '--input', 
    multiple=True,
    required=True, 
    type=click.Path(exists=True), 
    help='Named input directories: images, model_files',
)
@click.option(
    '--output', 
    required=True, 
    type=click.Path(), 
    help='Output directory'
)
@click.option(
    '--fullscan', 
    type=click.BOOL, 
    default=False, 
    help='Images correspond to single CT scan (true/false)'
)
@click.option(
    '--overwrite', 
    type=click.BOOL, 
    default=False, 
    help='Overwrite (true/false)'
)
def runpipeline(input, output, fullscan, overwrite):
    """
    Runs default body composition pipeline on images in input directory. The input 
    directory can either contain a set of L3 images (one for each patient) or a set
    of DICOM images corresponding to a single CT scan. In the latter case, provide
    the parameter full_scan=true.
    
    Parameters
    ----------
    input : dict
        Path to input directory with L3 images or CT scan files

        {
            'images': '/path/to/images',
            'model_files': '/path/to/model_files',
        }
    
    output : str
        Path to output directory

    fullscan : bool
        Wheter DICOM files in input directory correspond to L3 images (one for each
        patient) or a single CT scan
    
    overwrite : bool
        Overwrite contents output directory true/false
    """
    pipeline = DefaultPipeline(
        input, 
        output, 
        params=fullscan, 
        overwrite=overwrite,
    )
    pipeline.run()