#coding=utf-8
import numpy as py
import cv2 as cv

def test():
    cap = cv.VideoCapture(0)

    # cap = cv.VideoCapture("mv.avi")

    # 可以修改一些参数设置
    # 默认：640x480
    # cap.set(cv.CAP_PROP_FRAME_WIDTH, 320)
    # cap.set(cv.CAP_PROP_FRAME_HEIGHT, 240)

    # cap may not have initialized the capture.
    # In that case, this code shows error.
    # You can check whether it is initialized or not by the method cap.isOpened().
    # If it is True, OK. Otherwise open it using cap.open().

    while (cap.isOpened()):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Our operations on the frame come here
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        # Display the resulting frame
        cv.imshow("frame", gray)
        if cv.waitKey(0) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv.destroyAllWindows()



def save():
    cap =cv.VideoCapture(0)
    fourcc = cv.VideoWriter_fourcc(*'XVID')
    out = cv.VideoWriter('output.avi',fourcc,20.0,(640,480))
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            out.write(frame)
            cv.imshow('frame',frame)
            if cv.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    out.release()
    cv.destoryAllWindows()

save()