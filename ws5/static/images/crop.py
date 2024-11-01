import os
import cv2

path = './3.validating/'
dest_path = './output/'

# Create the folder if it does not exist
os.makedirs(dest_path, exist_ok=True)


for f in os.listdir(path):
    image = cv2.imread(os.path.join(path, f))
    height, width = image.shape[:2]
    imgcropped = image[125:1035, 0:width]

    cv2.imwrite(os.path.join(dest_path, f), imgcropped)
    print(os.path.join(path, f))