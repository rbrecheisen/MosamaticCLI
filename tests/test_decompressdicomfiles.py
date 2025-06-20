from mosamatic.tasks import DecompressDicomFilesTask


def test_me():
    task = DecompressDicomFilesTask(
        input='D:\\Mosamatic\\AutomaticSliceSelection\\validation\\L3',
        output='D:\\Mosamatic\\CLI\\Output\\DecompressDicomFilesTask',
        params=None,
        overwrite=True,
    )
    task.run()