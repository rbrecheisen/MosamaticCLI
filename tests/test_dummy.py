from mosamatic.tasks.dummy import DummyTask


def test_me():
    task = DummyTask(
        {'images': [], 'model': ''},
        'D:\\Mosamatic\\CLI\\Output\\Decompress',
        params={'param1': '1'},
        overwrite=True,
    )
    task.run()