import cv2
import sys
import numpy as np
#def facedet(img):
face_cascade = cv2.CascadeClassifier('W:\MAJOR PROJECt\Python\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('W:\MAJOR PROJECt\Python\haarcascade_eye.xml')
mouth_cascade = cv2.CascadeClassifier('W:\MAJOR PROJECt\Python\haarcascade_mcs_mouth.xml')
#nose_cascade = cv2.CascadeClassifier('W:\MAJOR PROJECt\Python\haarcascade_mcs_nose.xml')
cap = cv2.VideoCapture(0)
cap.set(3,400)
cap.set(4,260)
i=0
m=0
array=[]
array1=[]
array2=[]
array3=[]
array4=[]
i=0
sum1=0
sum3=0
sum2=0
m=0
while i<3:
    
    #img = cv2.imread(img)
    ret, frame = cap.read() # Capture frame-by-frame
    img = frame
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        #nose =  nose_cascade.detectMultiScale(roi_gray,1.3,5)
        mouth = mouth_cascade.detectMultiScale(roi_gray,1.3,5)
        '''print "FACE"
        print y
        print h
        print x
        print w'''
        i1=0
        print "EYES"
        for (ex,ey,ew,eh) in eyes:
            print "YES"
            if i1==0:
                sum1=sum1+ew
                print ew
            elif i1==1:
                sum3=sum3+ew
                print ew
            cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0,255,0), 1)
            i1=i1+1
            '''print "EYES"
            print ex
            print ey'''
        '''for (nx, ny, nw, nh) in nose:
            cv2.rectangle(roi_color, (nx, ny), (nx + nw, ny + nh), (0, 0, 255), 1)
            print "nose"
            print nh
            print nw'''
        max2=-900000
        r=0
        s=0
        g=0
        h1=0
        flag=0
        max1=-90000
        for (mx, my, mw, mh) in mouth:
            #cv2.rectangle(roi_color, (mx, my), (mx + mw, my + mh), (255, 255, 255), (2))
            
            
            print "BURHAN"
            
            '''if max1<(mw-mh):
                max1=(mw-mh)
                if max2<(mw*mh):
                    max2=mw*mh
                    r=mx
                    s=my
                    g=mw
                    h=mh'''
            '''print "MY"
            print my
            print "Mx"
            print mx'''
            if my>(h/2):
                flag=1
                r=mx
                s=my
                g=mw
                h1=mh
        if flag==1:
            sum2=sum2+(float)(mw*mh)/(w*h)
            cv2.rectangle(roi_color, (r, s), (r + g, s + h1), (0, 0, 0), 1)
            m=m+1
            print " MOUTH"
            i=i+1
            #print r 
            #print s
            print g
            #print h1
            #array.append((float)(g)/(w))
            #array1.append((float)(h1)/h)
            #array2.append(g)
            #m=m+1
            print "HAHA"
        

    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.imshow('image',img)
    #cv2.waitKey(0)
    c = cv2.cv.WaitKey(7) % 0x100
    if c == 27:
        break
print sum1/m
print sum3/m
print (float)(sum2)/3
print m
print "JAJAJAJAJAJJAJAJJAJAAAAAAAAAAAAAAAAAAAAAAAAAA"
i=0
while i<200:
    i=i+1
    #img = cv2.imread(img)
    ret, frame = cap.read() # Capture frame-by-frame
    img = frame
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        #nose =  nose_cascade.detectMultiScale(roi_gray,1.3,5)
        mouth = mouth_cascade.detectMultiScale(roi_gray,1.3,5)
        '''print "FACE"
        print y
        print h
        print x
        print w'''
        i1=0
        for (ex,ey,ew,eh) in eyes:
            if i1==0:
                array3.append(ew)
            elif i1==1:
                array4.append(ew)
            i1=i1+1
            cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0,255,0), 1)
            '''print "EYES"
            print ex
            print ey'''
        '''for (nx, ny, nw, nh) in nose:
            cv2.rectangle(roi_color, (nx, ny), (nx + nw, ny + nh), (0, 0, 255), 1)
            print "nose"
            print nh
            print nw'''
        max2=-900000
        r=0
        s=0
        g=0
        h1=0
        flag=0
        max1=-90000
        for (mx, my, mw, mh) in mouth:
            #cv2.rectangle(roi_color, (mx, my), (mx + mw, my + mh), (255, 255, 255), (2))
            flag=1
            '''if max1<(mw-mh):
                max1=(mw-mh)
                if max2<(mw*mh):
                    max2=mw*mh
                    r=mx
                    s=my
                    g=mw
                    h=mh'''
            '''print "MY"
            print my
            print "Mx"
            print mx'''
            if my>(h/2):
                r=mx
                s=my
                g=mw
                h1=mh
        if flag==1:
            cv2.rectangle(roi_color, (r, s), (r + g, s + h1), (0, 0, 0), 1)
            print " MOUTH"
            
            #print r 
            #print s
            print g
            #print h1
            #array.append((float)(g)/(w))
            #array1.append((float)(h1)/h)
            array2.append((float)(g*h1)/(w*h))
            m=m+1
            print "HAHA"

    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.imshow('image',img)
    #cv2.waitKey(0)
    c = cv2.cv.WaitKey(7) % 0x100
    if c == 27:
        break
cap.release()
cv2.destroyAllWindows()
r=0
print "HELLLO"
array2.sort()
count=0
while r<len(array2):
    if array2[r]!=0:
        if array2[r]>((float)(sum2)/3):
            count=count+1
        print array2[r]
        '''print "YES"
        print array[r]
        print array1[r]
        print (array[r]*array1[r])
        print (array[r]/array1[r])'''
        
    r=r+1
print "EYES"
print sum1
print sum3
r=0
print "SMILING"
print (float)(count*100)/len(array2)
while r<len(array3):
    print "YES"
    if array3[r]!=0:
        print array3[r]
    if array4[r]!=0:
        print array4[r]
    r=r+1

#0.35 - 0.47 No smile
#0.36 - 0.59 Smile
'''if __name__ == '__main__':
    #img = sys.argv[1]
    facedet('W:\MAJOR PROJECt\Python\33.png')'''
