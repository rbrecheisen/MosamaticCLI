from mosamatic.tasks.task import Task


class SegmentMuscleFatL3Task(Task):
    def __init__(self, input, output, params=None, overwrite=False):
        super(SegmentMuscleFatL3Task, self).__init__(input, output, params=params, overwrite=overwrite)

    def run(self):
        pass
