import click
import numpy as np
from PIL import Image
from numpy import asarray

def convert(infile, outfile=None):
	image = Image.open(infile)
	data = asarray(image)
	print(f"Image size: {data.shape}")
	with open(outfile, 'wb') as f:
		for y in range(data.shape[0]):
			for x in range(data.shape[1]):
				v = np.uint16(data[y][x])
				f.write(v)

@click.command()
@click.argument("infile")
@click.option("--outfile", default=None, help="specify output filename (default: replace filename extension with .raw)")
def cli(infile, outfile):
	if outfile is None:
		parts = infile.split('.')
		parts[-1] = "raw"
		outfile = ".".join(parts)
	convert(infile, outfile)