from mosamatic.tasks.segmentmusclefatl3task import SegmentMuscleFatL3Task


def test_me():
    task = SegmentMuscleFatL3Task(
        'D:\\Mosamatic\\CLI\\Input',
        'D:\\Mosamatic\\CLI\\Output\\Decompress',
        params=None,
        overwrite=True,
    )
    task.run()