import imgaug.augmenters as iaa
import cv2
import glob

# img = cv2.imread("images\\ng 2.jpg")
# cv2.imshow("Image", img)
# cv2.waitKey(0)
#1. Load Dataset
images = []
images_path = glob.glob("images/EI/*.png")
for img_path in images_path:
    img = cv2.imread(img_path)
    images.append(img)
#2. Image Augmentation
augmentation = iaa.Sequential([
    #iaa.Fliplr(0.8), # horizontal flips
    #iaa.Crop(percent=(0, 0.1)), # random crops
    # Small gaussian blur with random sigma between 0 and 0.5.
    # But we only blur about 50% of all images.
    iaa.Resize((1.0, 2.0))])

augmented_images = augmentation(images = images)
i = 381
ng = 'Chip_Crack '
dir = 'C:\\Users\\user\\Desktop\\result_img_02\\'
#3. Show images
for img in augmented_images:
    name = dir + ng + str(i) +'.png'
    cv2.imwrite(name, img)
    i+=1
    #cv2.imshow("Image", img)
    #cv2.waitKey(0)
