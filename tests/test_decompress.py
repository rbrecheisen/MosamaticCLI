from mosamatic.tasks import DecompressDicomFilesTask


def test_me():
    task = DecompressDicomFilesTask(
        'D:\\Mosamatic\\AutomaticSliceSelection\\validation\\L3',
        'D:\\Mosamatic\\CLI\\Output\\DecompressDicomFilesTask',
        params=None,
        overwrite=True,
    )
    task.run()