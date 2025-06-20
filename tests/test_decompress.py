from mosamatic.tasks.decompress import DecompressTask


def test_me():
    task = DecompressTask(
        'D:\\Mosamatic\\CLI\\Input\\CT.1.3.12.2.1107.5.1.4.75537.30000020012407082293400013519',
        'D:\\Mosamatic\\CLI\\Output\\Decompress',
        params=None,
        overwrite=True,
    )
    task.run()