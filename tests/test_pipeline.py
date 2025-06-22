from mosamatic.tasks import (
    DecompressDicomFilesTask, 
    RescaleDicomFilesTask,
    SegmentMuscleFatL3Task,
    CalculateScoresTask,
    CreatePngsFromSegmentationsTask,
)

from tests.sources import get_sources
SOURCES = get_sources()


def test_pipeline():

    task = DecompressDicomFilesTask(
        input=SOURCES['input'],
        output=SOURCES['output']['DecompressDicomFilesTask'],
        params=None,
        overwrite=True,
    )
    task.run()
    assert False, 'You need to test the task output!!!'

    task = RescaleDicomFilesTask(
        input=SOURCES['output']['DecompressDicomFilesTask'],
        output=SOURCES['output']['RescaleDicomFilesTask'],
        params={'target_size': '512'},
        overwrite=True,
    )
    task.run()

    task = SegmentMuscleFatL3Task(
        input={
            'images': SOURCES['output']['RescaleDicomFilesTask'],
            'model_files': SOURCES['model_files'],
        },
        output=SOURCES['output']['SegmentMuscleFatL3Task'],
        params={'model_version': '2.2'},
        overwrite=True,
    )
    task.run()

    task = CalculateScoresTask(
        input={
            'images': SOURCES['output']['RescaleDicomFilesTask'],
            'segmentations': SOURCES['output']['SegmentMuscleFatL3Task'],
        },
        output=SOURCES['output']['CalculateScoresTask'],
        params=None,
        overwrite=True,
    )
    task.run()

    task = CreatePngsFromSegmentationsTask(
        input=SOURCES['output']['SegmentMuscleFatL3Task'],
        output=SOURCES['output']['CreatePngsFromSegmentationsTask'],
        params={
            'fig_width': '10',
            'fig_height': '10',
        },
        overwrite=True,
    )
    task.run()