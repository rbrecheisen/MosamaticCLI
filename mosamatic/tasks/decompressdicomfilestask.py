import os
import shutil

from mosamatic.tasks.task import Task
from mosamatic.utils import (
    is_dicom, 
    load_dicom,
    is_jpeg2000_compressed,
)


class DecompressDicomFilesTask(Task):
    def __init__(self, input, output, params=None, overwrite=False):
        super(DecompressDicomFilesTask, self).__init__(input, output, params=params, overwrite=overwrite)
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
            source_name = os.path.split(source)[1]
            target = os.path.join(self.output(), source_name)
            p = load_dicom(source)
            if is_jpeg2000_compressed(p):
                p.decompress()
                p.save_as(target)
            else:
                shutil.copy(source, target)
            self.set_progress(step, nr_steps)
