# svs图片生成

## Aperio format

.svs格式后缀的文件一般是由Aperio Technologies公司的ScanScope系统将病理切片扫描成的数字图像。Aperio format可以参考openslide文档[https://openslide.org/formats/aperio/](https://openslide.org/formats/aperio/)

Aperio格式有3条规则：

1. 图片是TIFF。
2. 初始图像是分块的。
3. 图片描述的tag以Aperio开头

同时根据文档的描述：svs文件的第一张图像始终是baseline图像（全分辨率）。图像永远是分块的，且一般块的大小是240\*240。第二张图是缩略图，一般为1024\*768

一些图像描述中会用到的量

- Aperio.appMag: 物镜的放大倍率，一般为20x或者40x。
- resulotion：分辨率。有时候有XResolution和YResolution（例如Hamamatsu format），指每个pixel的大小，一张20x倍率的图片，resolution为 .46 microns，40x的图片为.23 microns。
- tiff.ResolutionUnit: 分辨率的单位一般为cm或者inch。
- aperio.MPP：等于resulotion。openslide.mpp-x和openslide.mpp-y分别对应XResolution和YResolution。

## 把图片转成svs格式

- 有金字塔状的图片数据。
- 使用tifffile，将数据从大到小依次写入。
- 写入第一张全分辨率图时，同时写入一张缩略图。

## 代码使用

- 安装requirements.txt里的python包。
- ndpi格式的文件可以直接使用example.py。
- 其他格式可以转成numpy后调用numpy2svs.py。
