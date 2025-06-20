import os
import shutil
import click

from mosamatic.tasks.task import Task
from mosamatic.utils import (
    is_jpeg2000_compressed, 
    is_dicom, 
    load_dicom,
)


class DecompressTask(Task):
    def __init__(self, input, output, params=None, overwrite=False):
        super(DecompressTask, self).__init__(input, output, params=params, overwrite=overwrite)
        if not os.path.isfile(input):
            raise RuntimeError('Input is not a file, but probably a directory')
        if not os.path.isdir(output):
            raise RuntimeError('Output is not a directory')

    def run(self):
        if os.path.exists(self.input()) and os.path.isfile(self.input()):
            if is_dicom(self.input()):
                source_name = os.path.split(self.input())[1]
                target = os.path.join(self.output(), source_name)
                p = load_dicom(self.input())
                if is_jpeg2000_compressed(p):
                    p.decompress()
                    p.save_as(target)
                else:
                    shutil.copy(self.input(), target)


@click.command(help='Decompress a single DICOM file')
@click.option('--input', required=True, type=click.Path(exists=True), help='Input file path')
@click.option('--output', required=True, type=click.Path(), help='Output directory')
def decompress(input, output):
    task = DecompressTask(input, output)
    task.run()