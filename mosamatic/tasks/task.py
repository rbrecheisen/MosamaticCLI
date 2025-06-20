import os

from mosamatic.logging import LogManager

LOG = LogManager()


class Task:
    def __init__(self, input, output, params=None, overwrite=False):
        self._input = input
        self._output = output
        self._params = params
        self._overwrite = overwrite
        if os.path.exists(self._output) and not self._overwrite:
            raise RuntimeError(f'Output already exists')
        if os.path.isdir(self._output):
            os.makedirs(self._output, exist_ok=True)

    def input(self):
        return self._input
    
    def output(self):
        return self._output
    
    def params(self):
        return self._params
    
    def param(self, name):
        if self._params and name in self._params.keys():
            return self._params[name]
        raise RuntimeError(f'Parameter "{name}" does not exist')
    
    def overwrite(self):
        return self._overwrite
    
    def set_progress(self, step, nr_steps):
        LOG.info(f'step {step} from {nr_steps}')
    
    def run(self):
        raise NotImplementedError()