from mosamatic.tasks.decompress import DecompressTask


def test_me():
    task = DecompressTask(
        'D:\\Mosamatic\\CLI\\Input',
        'D:\\Mosamatic\\CLI\\Output\\Decompress',
        params=None,
        overwrite=True,
    )
    task.run()