import openslide
from image2np.ndpiSlide2numpy import get_ndpi_slide_pyramidal_data, get_ndpi_slide_properties
from np2svs.numpy2svs import numpy2tiff

def ndpi2svs(input_file, output_file):
    slide = openslide.OpenSlide(input_file)
    pyramidal_np_data = get_ndpi_slide_pyramidal_data(slide)
    thumb_data = slide.get_thumbnail((512, 512))
    properties = get_ndpi_slide_properties(slide)

    numpy2tiff(pyramidal_np_data,thumb_data,output_file,properties)


if __name__ == "__main__":
    ndpi_file = "your_ndpi_file.ndpi"
    svs_file = "new_svs_file.svs"
    ndpi2svs(ndpi_file, svs_file)