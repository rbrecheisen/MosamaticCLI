from mosamatic.tasks.task import Task


def test_me():
    # Input and output are directories
    Task(
        'D:\\Mosamatic\\CLI\\Input',
        'D:\\Mosamatic\\CLI\\Output\\Decompress',
        params=None,
        overwrite=True,
    )
    
    # Input is file and output is directory
    Task(
        'D:\\Mosamatic\\CLI\\Input\\CT.1.3.12.2.1107.5.1.4.75537.30000020012407082293400013519',
        'D:\\Mosamatic\\CLI\\Output\\Decompress',
        params=None,
        overwrite=True,
    )

    # Input is file and output is directory (overwrite=False)
    try:
        Task(
            'D:\\Mosamatic\\CLI\\Input\\CT.1.3.12.2.1107.5.1.4.75537.30000020012407082293400013519',
            'D:\\Mosamatic\\CLI\\Output\\Decompress',
            params=None,
            overwrite=False,
        )
    except:
        print('Task correct raised exception when trying to overwrite existing output directory')
        assert True
    
    # Input is file and output is file
    Task(
        'D:\\Mosamatic\\CLI\\Input\\CT.1.3.12.2.1107.5.1.4.75537.30000020012407082293400013519',
        'D:\\Mosamatic\\CLI\\Output\\Decompress\\some_file.txt',
        params=None,
        overwrite=True,
    )