import click

from mosamatic.tasks import CalculateScoresTask


@click.command(help='Calculates body composition scores')
@click.option(
    '--input', 
    multiple=True,
    required=True, 
    type=click.Path(exists=True), 
    help='Named input directories: images, segmentations',
)
@click.option(
    '--output', 
    required=True, 
    type=click.Path(), 
    help='Output directory'
)
@click.option(
    '--overwrite', 
    type=click.BOOL, 
    default=False, 
    help='Overwrite (true/false)'
)
def calculatescores(input, output, overwrite):
    """
    Calculates the following body composition scores from muscle and fat
    segmentations extracted using the "segmentmusclefatl3" command:
    
    - Skeletal muscle area
    - Skeletal muscle radiation attenuation
    - Subcutaneous fat area
    - Subcutaneous fat radiation attenuation
    - Visceral fat area
    - Visceral fat radiation attenuation
    
    Parameters
    ----------
    input : dict
        Dictionary specifying directory where images are located. Can be the output
        of the "decompress" or "rescale" commands:
        
        {
            'images': '/path/to/images',
            'segmentations': '/path/to/segmentations',
        }
    
    output : str
        Path to output directory.
    
    overwrite : bool
        Overwrite contents output directory true/false
    """
    task = CalculateScoresTask(input, output, overwrite=overwrite)
    task.run()