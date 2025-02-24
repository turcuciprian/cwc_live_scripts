import numpy as np
import cv2

img = np.zeros((500,500), dtype=np.uint8)
cv2.circle(img=img, 
              center=(250, 250), 
              radius=100, 
              color=(255,255,255), 
              thickness=1)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
