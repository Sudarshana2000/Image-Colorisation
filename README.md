# Image-Colorisation

With the power of deep learning and computer vision, now it is possible to colorise black and white / gray-scale images. The results are fascinating and plausibe for most of the images, such that it can even fool humans to distinguish between the real and fake images!


## Technique

It's based on Richard Zhang's work in 2016 ECCV paper, [Colorful Image Colorization](http://richzhang.github.io/colorization/). Please do check out his EECV Talk where he discussed everything about his work!


## Requirements

- OpenCv
- numpy
- [pre-trained colorisation model](models/)


# Results

- colorise pictures from black and white era
<div style="float:left"><img width="45%" src="https://github.com/Sudarshana2000/Image-Colorisation/blob/master/images/classic.jpg" />
<img width="45%" src="https://github.com/Sudarshana2000/Image-Colorisation/blob/master/images/output_classic.jpg" />
</div>
<br /><br />

- get a random colored image from grayscale image
<div style="float:left"><img width="45%" src="https://github.com/Sudarshana2000/Image-Colorisation/blob/master/images/rose.jpg" />
<img width="45%" src="https://github.com/Sudarshana2000/Image-Colorisation/blob/master/images/output_rose.jpg" />
</div>
<br /><br />

- remove unwanted colors and normalise the image
<div style="float:left"><img width="30%" src="https://github.com/Sudarshana2000/Image-Colorisation/blob/master/images/orig_dog.jpg" />
<img width="30%" src="https://github.com/Sudarshana2000/Image-Colorisation/blob/master/images/dog.jpg" />
<img width="30%" src="https://github.com/Sudarshana2000/Image-Colorisation/blob/master/images/output_dog.jpg" />
</div>
<br /><br />

- few unrealistic outcomes
<div style="float:left"><img width="45%" src="https://github.com/Sudarshana2000/Image-Colorisation/blob/master/images/rose.png" />
<img width="45%" src="https://github.com/Sudarshana2000/Image-Colorisation/blob/master/images/output_rose.png" />
</div>
<br /><br />
