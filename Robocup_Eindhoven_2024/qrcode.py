import cv2
import numpy as np
from pyzbar import decode
def main():
    tomb = []
    def decoder(image):
        gray_img = cv2.cvtColor(image,0)
        barcode = decode(gray_img)

        for obj in barcode:
            points = obj.polygon
            (x,y,w,h) = obj.rect
            pts = np.array(points,np.int32)
            pts = pts.reshape((-1,1,2))
            cv2.polylines(image, [pts], True, (0, 255, 0), 3)

            barcodeData = obj.data.decode("utf-8")
            string = "Data" + str(barcodeData) + "\n"

            if string is not tomb:
                return tomb.append(string)


    cap = cv2.VideoCapture(0)
    cap.set(3,700)
    cap.set(4,700)

    while True:
        ret,frame = cap.read()
        decoder(frame)
        cv2.imshow('Image',frame)
        code = cv2.waitKey(10)

        if code == ord('q'):
            break

    tomb = list(set(tomb))
    kimenet = open("QR_codes_read","w")
    for i in tomb:
        kimenet.write(i)
    kimenet.close
if __name__ == '__main__':
    main()