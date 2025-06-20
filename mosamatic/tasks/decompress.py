import click


class DecompressTask:
    def __init__(self, input_dir, output_dir):
        self._input_dir = input_dir
        self._output_dir = output_dir

    def run(self):
        click.echo(f'Running DecompressTask(input_dir={self._input_dir}, output_dir={self._output_dir})')


@click.command()
@click.option('--input-dir', required=True, type=click.Path(exists=True), help='Input directory')
@click.option('--output-dir', required=True, type=click.Path(), help='Output directory')
def decompress(input_dir, output_dir):
    task = DecompressTask(input_dir, output_dir)
    task.run()