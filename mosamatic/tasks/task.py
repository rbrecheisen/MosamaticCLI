import os

from mosamatic.logging import LogManager

LOG = LogManager()


class Task:
    def __init__(self, input, output, params=None, overwrite=False):
        if input == output:
            raise RuntimeError(f'Input cannot be same as output')
        if os.path.exists(output) and not overwrite:
            raise RuntimeError(f'Output already exists')
        if os.path.isdir(output):
            os.makedirs(output, exist_ok=True)
        self._input = input
        self._output = output
        self._params = params

    def input(self):
        return self._input
    
    def output(self):
        return self._output
    
    def param(self, name):
        if self._params and name in self._params.keys():
            return self._params[name]
        raise RuntimeError(f'Parameter "{name}" does not exist')
    
    def set_progress(self, step, nr_steps):
        LOG.info(f'step {step} from {nr_steps}')
    
    def run(self):
        raise NotImplementedError()