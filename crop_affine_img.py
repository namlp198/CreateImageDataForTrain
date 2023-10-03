import imgaug.augmenters as iaa
import cv2
import glob

# img = cv2.imread("images\\ng 2.jpg")
# cv2.imshow("Image", img)
# cv2.waitKey(0)
#1. Load Dataset
images = []
images_path = glob.glob("C:\\Users\\user\\Desktop\\aug_img_2\\*.png")
for img_path in images_path:
    img = cv2.imread(img_path)
    images.append(img)
#2. Image Augmentation
augmentation = iaa.Sequential([
    iaa.CropAndPad(
    percent=(0, 0.1),
    pad_mode=["constant", "edge"],
    pad_cval=(0, 128)),
    iaa.Affine(
         scale={"x": (0.8, 1.2), "y": (0.8, 1.2)},
         translate_percent={"x": (-0.2, 0.2), "y": (-0.2, 0.2)},
         rotate=(-15, 15),
         shear=(-8, 8)
     )
])

augmented_images = augmentation(images = images)
i = 681
ng = 'Chip_Crack '
dir = 'C:\\Users\\user\\Desktop\\aug_img_2\\auged_img\\'
#3. Show images
for img in augmented_images:
    name = dir + ng + str(i) +'.png'
    cv2.imwrite(name, img)
    i+=1
    #cv2.imshow("Image", img)
    #cv2.waitKey(0)