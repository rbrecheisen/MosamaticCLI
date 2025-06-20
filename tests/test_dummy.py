from mosamatic.tasks.dummy import DummyTask


def test_me():
    task = DummyTask(
        {'images': [], 'model': ''},
        'D:\\Mosamatic\\CLI\\Output\\Decompress',
        params=None,
        overwrite=True,
    )
    task.run()