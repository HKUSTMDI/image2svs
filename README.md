# SVS Image Generation

## Aperio Format

Files with the .svs extension are generally digital images scanned from pathological slides by the ScanScope system of Aperio Technologies. You can refer to the Aperio format documentation on the openslide website [https://openslide.org/formats/aperio/](https://openslide.org/formats/aperio/)

The Aperio format has three rules:

1. The file is a TIFF.
2. The initial image is tiled.
3. The ImageDescription tag starts with Aperio.

According to the documentation, the first image in an SVS file is always the baseline image (full resolution). This image is always tiled, usually with a tile size of 240 x 240 pixels.  The second image is always a
thumbnail, typically with dimensions of about 1024 x 768 pixels.

Some quantities used in image descriptions:

- Aperio.appMag: The magnification of the objective lens, usually 20x or 40x.
- Resolution: Sometimes there are XResolution and YResolution (e.g., Hamamatsu format), which indicate the size of each pixel. For a 20x magnification image, the resolution is .46 microns, and for a 40x image, it is .23 microns.
- tiff.ResolutionUnit: The unit of resolution, usually cm or inch.
- aperio.MPP: Equivalent to resolution. openslide.mpp-x and openslide.mpp-y correspond to XResolution and YResolution, respectively.

## Converting Images to SVS Format

- Pyramid-shaped image data.
- Use tifffile to write the data from large to small sequentially.
- When writing the first full-resolution image, also write a thumbnail.

## Code Usage

- Install the Python packages listed in requirements.txt.
- NDPI format files can be directly used with example.py.
- Other formats can be converted to numpy and then called with numpy2svs.py.
