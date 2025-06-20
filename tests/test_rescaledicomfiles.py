from mosamatic.tasks import RescaleDicomFilesTask


def test_me():
    task = RescaleDicomFilesTask(
        input='D:\\Mosamatic\\AutomaticSliceSelection\\validation\\L3',
        output='D:\\Mosamatic\\CLI\\Output\\RescaleDicomFilesTask',
        params={'target_size': '512'},
        overwrite=True,
    )
    task.run()