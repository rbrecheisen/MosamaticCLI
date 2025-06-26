import os

from mosamatic.tasks import CalculateScoresTask
from tests.sources import get_sources
SOURCES = get_sources()


def test_npy():
    pass


def test_tag():
    task = CalculateScoresTask(
        input={
            'images': SOURCES['input'],
            'segmentations': SOURCES['input'],
        }, output=SOURCES['output'], params={'file_type': 'npy'}, overwrite=True,
    )
    task.run()