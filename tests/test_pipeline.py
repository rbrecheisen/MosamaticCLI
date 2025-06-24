import os

from mosamatic.pipelines import DefaultPipeline
from mosamatic.utils import is_dicom

from tests.sources import get_sources
SOURCES = get_sources()


def test_default_pipeline():
    assert os.path.exists(SOURCES['input']), 'Input directory does not exist'
    pipeline = DefaultPipeline(
        input={
            'images': SOURCES['input'],
            'model_files': SOURCES['model_files'],
        }, output=SOURCES['output'],
        params={'target_size': '512', 'model_version': '2.2', 'fig_width': '10', 'fig_height': '10'}, overwrite=True,
    )
    pipeline.run()