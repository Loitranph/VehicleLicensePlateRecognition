# Created by Tran Phuoc Loi

import cv2 as cv
import pytesseract

'''
Fix tesseractNotFondError()

[WINDOW] download and extract file in this link https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-5.3.3.20231005.exe
Run 'tesseract-ocr-w64-setup-5.3.3.20231005.exe' 
Copy path of 'tesseract.exe' and paste in r' path here '

'''
pytesseract.pytesseract.tesseract_cmd = r'\YOUR_PATH\tesseract.exe' # If you don't have an tesseractNotFoundError(), don't use this line

cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
    cv.putText(frame, "KHUNG BIEN SO:", (40, 40), cv.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0))

    contours, h = cv.findContours(thresh, 1, 2)
    largest_rectangle = [0, 0]

    for cnt in contours:
        length = 0.01 * cv.arcLength(cnt, True)
        approx = cv.approxPolyDP(cnt, length, True)
        if len(approx) == 4:
            area = cv.contourArea(cnt)
            if area > largest_rectangle[0]:
                largest_rectangle = [cv.contourArea(cnt), cnt, approx]
    x, y, w, h = cv.boundingRect(largest_rectangle[1])

    x = int(0.995*x)
    y = int(0.995*y)
    w = int(1.005*w)
    h = int(1.005*h)

    image = frame[y:y + h, x:x + w]
    cv.drawContours(frame, [largest_rectangle[1]], 0, (0, 255, 0), 8)
    cropped = frame[y:y + h, x:x + w]
    cv.putText(frame, "BIEN SO :", (x,y), cv.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255))
    cv.imshow('DINH VI BIEN SO :', frame)
    cv.drawContours(frame, [largest_rectangle[1]], 0, (255, 255, 255), 18)

    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (3, 3), 0)
    thresh = cv.threshold(blur, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)[1]
    cv.imshow('BIEN SO XE LA :', thresh)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
    opening = cv.morphologyEx(thresh, cv.MORPH_OPEN, kernel, iterations=1)
    invert = 255 - opening
    data = pytesseract.image_to_string(invert, lang='eng', config='--psm 6')
    print("Bien so xe la : ")
    print(data)
    key = cv.waitKey(1)
    if key == 27:
        break
cap.release()
cv.destroyAllWindows()
