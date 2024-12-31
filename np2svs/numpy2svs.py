import numpy as np
from tifffile import TiffWriter

compression = ['JPEG', 95, dict(outcolorspace='YCbCr')]
kwargs = dict(subifds=0,photometric='rgb',planarconfig='contig',compression=compression,dtype=np.uint8,metadata=None)

def numpy2tiff(tiff,np_data,level,properties):
    width = properties["level_size"][level]["width"]
    height = properties["level_size"][level]["height"]
    tile_size = properties["tile_size"]
    resolution = properties["resolution"]
    desc = properties["desc"]
    tiff.write(np_data,shape=(height, width, 3),tile=(tile_size,tile_size),resolution=resolution,description=desc, **kwargs)

def write_thumbnail(tiff,thumb_data):
    tiff.write(thumb_data,description='', **kwargs)
