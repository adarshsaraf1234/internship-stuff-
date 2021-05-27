import cv2
import sys
import numpy as np

path=sys.argv[1]
def rice_counter(path):
    img = cv2.imread(path)
    img = cv2.resize(img, (800, 800))

    gray = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2GRAY)
    thresh =cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,31,-15)

    element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))

    #kernel = np.ones((5,5), np.uint8)

    erosion = cv2.erode(thresh, element)
    #erosion=  cv2.erode(erosion,element)
    cv2.imshow("eroded image", erosion)
    cv2.waitKey(0)
    # ret,thresh=cv2.threshold(erosion, 127, 255, 0)
    contours, hierachy = cv2.findContours(erosion, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    m=[]
    a = []
    for contour in contours:
        area = cv2.contourArea(contour)
        rect = cv2.boundingRect(contour)
        cv2.rectangle(img, rect, (0, 0, 0xff), 1)
        m.append(area)
        if area<37:
            a.append(area)
    print("mean",np.mean(m))
    output_contour = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    cv2.drawContours(output_contour, contours, -1, (0, 0, 255), 2)
    print("Number of Rice Grains:-", len(contours))
    print("percentage of broken rice", len(a) / len(contours) * 100)
    cv2.imshow("Contours", output_contour)
    cv2.waitKey(0)
    cv2.imshow("rects", img)
    cv2.waitKey(0)

rice_counter(sys.argv[1])
