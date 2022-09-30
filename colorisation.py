import argparse
import cv2
import numpy as np


# set important paths
prototxt = "models/colorization_deploy_v2.prototxt"
model = "models/colorization_release_v2.caffemodel"
points = "models/pts_in_hull.npy"

# load the serialized coloriser model and cluster center points
net = cv2.dnn.readNetFromCaffe(prototxt, model)
pts = np.load(points)

# add the cluster centers as 1x1 convolutions to the model
class8 = net.getLayerId("class8_ab")
conv8 = net.getLayerId("conv8_313_rh")
pts = pts.transpose().reshape(2, 313, 1, 1)
net.getLayer(class8).blobs = [pts.astype("float32")]
net.getLayer(conv8).blobs = [np.full([1, 313], 2.606, dtype="float32")]


def process(imagePath):
    # load the image
    image = cv2.imread(imagePath)
    
    # preprocess the image in Lab color space
    scaled = image.astype("float32") / 255.0
    lab = cv2.cvtColor(scaled, cv2.COLOR_BGR2LAB)
    resized = cv2.resize(lab, (224, 224))
    
    # extract L channel and perform mean centering
    L = cv2.split(resized)[0]
    L -= 50
    
    # pass the input L channel through the network
    net.setInput(cv2.dnn.blobFromImage(L))
    
    # predict 'a' 'b' channels
    ab = net.forward()[0, :, :, :].transpose((1, 2, 0))
    
    # post processing
    # add the predicted ab channel with the original L channel
    ab = cv2.resize(ab, (image.shape[1], image.shape[0]))
    L = cv2.split(lab)[0]
    colorized = np.concatenate((L[:, :, np.newaxis], ab), axis=2)
    colorized = cv2.cvtColor(colorized, cv2.COLOR_LAB2BGR)
    colorized = np.clip(colorized, 0, 1)
    colorized = (255 * colorized).astype("uint8")    
    return colorized


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('inputPath', help='Input black and white image path')
    parser.add_argument('outputPath', help='Colorised output image path')
    args = parser.parse_args()
    output = process(args.inputPath)
    cv2.imwrite(args.outputPath, output)