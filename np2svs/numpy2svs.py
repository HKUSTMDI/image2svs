import numpy as np
from tifffile import TiffWriter

compression = ['JPEG', 95, dict(outcolorspace='YCbCr')]
kwargs = dict(subifds=0,photometric='rgb',planarconfig='contig',compression=compression,dtype=np.uint8,metadata=None)

def tiff_write_np(tiff,np_data,level,properties):
    width = properties["level_size"][level]["width"]
    height = properties["level_size"][level]["height"]
    tile_size = properties["tile_size"]
    resolution = properties["resolution"]
    desc = properties["desc"]
    tiff.write(np_data,shape=(height, width, 3),tile=(tile_size,tile_size),resolution=resolution,description=desc, **kwargs)

def write_thumbnail(tiff,thumb_data):
    tiff.write(thumb_data,description='', **kwargs)

def numpy2tiff(pyramidal_np_data,thumb_data,output_file,properties):
    with TiffWriter(output_file, bigtiff=True) as tiff:
        for i in range(properties["level_count"]):
            np_data = pyramidal_np_data[i]
            numpy2tiff(tiff, np_data, i, properties)
            if i == 0:
                write_thumbnail(tiff, thumb_data)
