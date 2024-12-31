import numpy as np

def get_ndpi_slide_region(slide,level):
    width = int(slide.properties.get(f'openslide.level[{level}].width'))
    height = int(slide.properties.get(f'openslide.level[{level}].height'))
    img = slide.read_region((0,0),level,(width,height)).convert("RGB")
    return np.array(img)

def get_ndpi_slide_properties(slide):
    level_count = int(slide.properties.get('openslide.level-count'))
    leve_size = []
    width = int(slide.properties.get('openslide.level[0].width'))
    height = int(slide.properties.get('openslide.level[0].height'))
    x_resolution = float(slide.properties.get('openslide.mpp-x'))
    y_resolution = float(slide.properties.get('openslide.mpp-y'))
    unit = slide.properties.get('tiff.ResolutionUnit')
    resolution = [1000/x_resolution, 1000/y_resolution, unit]
    app_mag = float(slide.properties.get('openslide.objective-power'))
    tile_size = 512 # 注意到ndpi的tile size 不是正方形，并且看到我们已有的svs的tile size一般是512*512，所以这里统一设置为512
    desc = f"Aperio Image Library v10.0.51\r\n{width}x{height} [0,100 {width}x{height}] ({tile_size}x{tile_size}) JPEG/RGB Q=30|AppMag = {app_mag}|MPP = {(x_resolution + y_resolution)/2}|OriginalWidth = {width}|Originalheight = {height}"
    for i in range(level_count):
        width = int(slide.properties.get(f'openslide.level[{i}].width'))
        height = int(slide.properties.get(f'openslide.level[{i}].height'))
        leve_size.append({"width": width, "height": height})
    return {
        "level_count": level_count,
        "origin_width": width,
        "origin_height": height,
        "x_resolution": x_resolution,
        "y_resolution": y_resolution,
        "resolution": resolution,
        "app_mag": app_mag,
        "tile_size": tile_size,
        "level_size": leve_size,
        "desc": desc
    }