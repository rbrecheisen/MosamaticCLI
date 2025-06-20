import os
import click

from mosamatic.tasks.task import Task
from mosamatic.tasks.decompress import DecompressTask
from mosamatic.utils import (
    is_dicom, 
)


class DecompressMultiTask(Task):
    def __init__(self, input, output, params=None, overwrite=False):
        super(DecompressMultiTask, self).__init__(input, output, params=params, overwrite=overwrite)
        if not os.path.isdir(input):
            raise RuntimeError('Input is not a directory')
        if not os.path.isdir(output):
            raise RuntimeError('Output is not a directory')

    def run(self):
        input_files = []
        for f in os.listdir(self.input()):
            f_path = os.path.join(self.input(), f)
            if is_dicom(f_path):
                input_files.append(f_path)
        if len(input_files) == 0:
            raise RuntimeError('Input directory has no DICOM files')
        nr_steps = len(input_files)
        for step in range(nr_steps):
            source = input_files[step]
            task = DecompressTask(source, self.output(), overwrite=self.overwrite())
            task.run()
            self.set_progress(step, nr_steps)


@click.command(help='Decompress multiple DICOM files')
@click.option('--input', required=True, type=click.Path(exists=True), help='Input directory')
@click.option('--output', required=True, type=click.Path(), help='Output directory')
def decompressmulti(input, output):
    task = DecompressMultiTask(input, output)
    task.run()