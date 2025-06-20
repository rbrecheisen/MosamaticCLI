from mosamatic.tasks import CalculateScoresTask


def test_me():
    task = CalculateScoresTask(
        input={
            'images': 'D:\\Mosamatic\\CLI\\Output\\RescaleDicomFilesTask',
            'segmentations': 'D:\\Mosamatic\\CLI\\Output\\SegmentMuscleFatL3Task',
        },
        output='D:\\Mosamatic\\CLI\\Output\\CalculateScoresTask',
        params=None,
        overwrite=True,
    )
    task.run()