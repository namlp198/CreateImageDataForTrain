import cv2
import glob

# img = cv2.imread("images\\ng 2.jpg")
# cv2.imshow("Image", img)
# cv2.waitKey(0)
#1. Load Dataset
images = []
images_path = glob.glob("C:\\Users\\user\\Desktop\\original_img\\*.png")
for img_path in images_path:
    img = cv2.imread(img_path)
    images.append(img)

i = 256
ng = 'Chip_Crack '
dir = 'C:\\Users\\user\\Desktop\\original_img\\img_renamed\\'
#3. Show images
for img in images:
    name = dir + ng + str(i) +'.png'
    cv2.imwrite(name, img)
    i+=1
    #cv2.imshow("Image", img)
    #cv2.waitKey(0)