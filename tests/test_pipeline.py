import os

from mosamatic.pipelines import (
    Pipeline,
    DefaultPipeline,
)
from mosamatic.utils import is_dicom

from tests.sources import get_sources
SOURCES = get_sources()


def test_default_pipeline():
    assert os.path.exists(SOURCES['input']), 'Input directory does not exist'


def test_pipeline_from_config():
    assert os.path.exists(SOURCES['input']), 'Input directory does not exist'