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
    def __init__(self, input_dir, output_dir, params=None, overwrite=False):
        super(DecompressTask, self).__init__(input_dir, output_dir, params=params, overwrite=overwrite)

    def run(self):
        input_files = []
        for f in os.listdir(self.input()):
            f_path = os.path.join(self.input(), f)
            if os.path.isfile(f_path):
                if is_dicom(f_path):
                    input_files.append(f_path)
        if len(input_files) == 0:
            raise RuntimeError(f'No DICOM files found in input directory')
        nr_steps = len(input_files)
        for step in range(nr_steps):
            source = input_files[step]
            source_name = os.path.split(source)[1]
            target = os.path.join(self.output(), source_name)
            p = load_dicom(source)
            if is_jpeg2000_compressed(p):
                p.decompress()
                p.save_as(target)
            else:
                shutil.copy(source, target)
            self.set_progress(step, nr_steps)


@click.command()
@click.option('--input-dir', required=True, type=click.Path(exists=True), help='Input directory')
@click.option('--output-dir', required=True, type=click.Path(), help='Output directory')
def decompress(input_dir, output_dir):
    task = DecompressTask(input_dir, output_dir)
    task.run()