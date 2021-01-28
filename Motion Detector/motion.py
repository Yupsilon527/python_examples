import cv2,time, datetime,pandas

times=[]
status_list=[None,None]
dataframe = pandas.DataFrame(columns=["Start","End"])

check_frame = None
video = cv2.VideoCapture(0)

recording = True

while recording:
    check, frame = video.read()
    status = 0
    
    grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    grayscale=cv2.GaussianBlur(grayscale,(21,21),0)
    
    if check_frame is None:
        check_frame = grayscale
        continue

    thresh_frame=cv2.threshold(cv2.absdiff(check_frame,grayscale), 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame=cv2.dilate(thresh_frame, None, iterations=2)

    (contours,_)=cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        if cv2.contourArea(contour)<10000:
            continue
        status = 1
        (x,y,w,h)=cv2.boundingRect(contour)
        cv2.rectangle(frame,(x,y),(w,h),(0,255,0),3)

    cv2.imshow("Image",frame)

    status_list.append(status)
    if status_list[-1] != status_list[-2]:
        times.append(datetime.datetime.now())
    key=cv2.waitKey(1)
    if key == ord('q'):
        recording = False

for i in range(0,len(times),2):
    dataframe=dataframe.append({"Start":times[i],"End":times[i+1]}, ignore_index=True)
dataframe.to_csv("Times.csv")

video.release()
cv2.destroyAllWindows()