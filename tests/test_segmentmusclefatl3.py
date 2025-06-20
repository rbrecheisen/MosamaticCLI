from mosamatic.tasks import SegmentMuscleFatL3Task


def test_me():
    task = SegmentMuscleFatL3Task(
        input={
            'images': 'D:\\Mosamatic\\AutomaticSliceSelection\\validation\\L3',
            'model_files': 'D:\\Mosamatic\\PyTorchModelFiles\\leroyvolmer\\2.2\\L3',
        },
        output='D:\\Mosamatic\\CLI\\Output\\SegmentMuscleFatL3Task',
        params={'model_version': '2.2'},
        overwrite=True,
    )
    task.run()