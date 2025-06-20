from mosamatic.tasks import CreatePngsFromSegmentationsTask


def test_me():
    task = CreatePngsFromSegmentationsTask(
        input='D:\\Mosamatic\\CLI\\Output\\SegmentMuscleFatL3Task',
        output='D:\\Mosamatic\\CLI\\Output\\CreatePngsFromSegmentationsTask',
        params={
            'fig_width': '10',
            'fig_height': '10',
        },
        overwrite=True,
    )
    task.run()