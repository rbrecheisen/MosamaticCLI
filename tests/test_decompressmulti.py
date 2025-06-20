from mosamatic.tasks.decompressmulti import DecompressMultiTask


def test_me():
    task = DecompressMultiTask(
        'D:\\Mosamatic\\CLI\\Input',
        'D:\\Mosamatic\\CLI\\Output\\Decompress',
        params=None,
        overwrite=True,
    )
    task.run()