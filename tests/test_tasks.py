import os

from mosamatic.tasks import (
    DecompressDicomFilesTask, 
    RescaleDicomFilesTask,
    SegmentMuscleFatL3Task,
    CalculateScoresTask,
    CreatePngsFromSegmentationsTask,
)
from mosamatic.utils import is_dicom

from tests.sources import get_sources
SOURCES = get_sources()


def test_tasks():

    assert os.path.exists(SOURCES['input']), 'Input directory does not exist'

    task = DecompressDicomFilesTask(
        input=SOURCES['input'],
        output=SOURCES['output']['DecompressDicomFilesTask'],
        params=None,
        overwrite=True,
    )
    task.run()

    output_dir = SOURCES['output']['DecompressDicomFilesTask']
    assert os.path.exists(output_dir), 'Output directory does not exist'
    assert len(os.listdir(output_dir)) == 4, 'Output directory does not contain 4 files'
    for f in os.listdir(output_dir):
        assert is_dicom(os.path.join(output_dir, f)), f'File {f} is not DICOM'

    task = RescaleDicomFilesTask(
        input=SOURCES['output']['DecompressDicomFilesTask'],
        output=SOURCES['output']['RescaleDicomFilesTask'],
        params={'target_size': '512'},
        overwrite=True,
    )
    task.run()

    output_dir = SOURCES['output']['RescaleDicomFilesTask']
    assert os.path.exists(output_dir), 'Output directory does not exist'
    assert len(os.listdir(output_dir)) == 4, 'Output directory does not contain 4 files'
    for f in os.listdir(output_dir):
        assert is_dicom(os.path.join(output_dir, f)), f'File {f} is not DICOM'

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

    output_dir = SOURCES['output']['SegmentMuscleFatL3Task']
    assert os.path.exists(output_dir), 'Output directory does not exist'
    assert len(os.listdir(output_dir)) == 4, 'Output directory does not contain 4 files'
    for f in os.listdir(output_dir):
        assert f.endswith('.seg.npy'), f'File {f} is not a NumPy file'

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

    output_dir = SOURCES['output']['CalculateScoresTask']
    assert os.path.exists(output_dir), 'Output directory does not exist'
    assert len(os.listdir(output_dir)) == 2, 'Output directory does not contain 2 files'
    assert os.path.exists(os.path.join(output_dir, 'bc_scores.csv'))
    assert os.path.exists(os.path.join(output_dir, 'bc_scores.xlsx'))

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

    output_dir = SOURCES['output']['CreatePngsFromSegmentationsTask']
    assert os.path.exists(output_dir), 'Output directory does not exist'
    assert len(os.listdir(output_dir)) == 4, 'Output directory does not contain 4 files'
    for f in os.listdir(output_dir):
        assert f.endswith('.seg.npy.png'), f'File {f} is not a PNG file'
