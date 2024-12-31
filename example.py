import openslide
from tifffile import TiffWriter
from image2np.ndpiSlide2numpy import get_ndpi_slide_region, get_ndpi_slide_properties
from np2svs.numpy2svs import numpy2tiff, write_thumbnail

def ndpi2svs(input_file, output_file):
    slide = openslide.OpenSlide(input_file)
    thumb_data = slide.get_thumbnail((512, 512))
    properties = get_ndpi_slide_properties(slide)

    with TiffWriter(output_file, bigtiff=True) as tiff:
        for i in range(properties["level_count"]):
            np_data = get_ndpi_slide_region(slide, i)
            numpy2tiff(tiff, np_data, i, properties)
            if i == 0:
                write_thumbnail(tiff, thumb_data)


if __name__ == "__main__":
    ndpi_file = "your_ndpi_file.ndpi"
    svs_file = "new_svs_file.svs"
    ndpi2svs(ndpi_file, svs_file)