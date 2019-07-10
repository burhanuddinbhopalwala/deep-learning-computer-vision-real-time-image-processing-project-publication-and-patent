import cv2
import sys
import os
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

"""file=open('W:\\MAJOR PROJECt\\Python\\MajorProje\\nof.txt','r')#NAME OF FOLDER saved in FILE
a=int(file.read())
a1=a+1
file.close()
file=open('W:\\MAJOR PROJECt\\Python\\MajorProje\\nof.txt','w')
file.write((str)(a1))
file.close()
newpath = r'W:\\MAJOR PROJECt\\Python\\MajorProje\\s'+(str)(a)
if not os.path.exists(newpath):
    os.makedirs(newpath)#MAKE FOLDER FOR TRAINING SET"""

k=0
array5=[]
array6=[]
#GET AVERAGE VALUE OF FACE
while i<100:
    print "AMIT"
    #img = cv2.imread(img)
    ret, frame = cap.read() # Capture frame-by-frame
    img = frame
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray1 = cv2.fastNlMeansDenoising(img, None,3,7,11)
    print "HELLO"
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
                sum1=sum1+(float)(ew*eh)/(w*h)
                array5.append((float)(ew*eh)/(w*h))
                print ew 
                print ex
                print ey
                cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0,255,0), 1)
            elif i1==1:
                sum3=sum3+(float)(ew*eh)/(w*h)
                array6.append((float)(ew*eh)/(w*h))
                k=k+1
                print ew
                print ex
                print ey
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
             
            print g
            
            print "HAHA"
        

    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.imshow('image',gray)
    cv2.imshow('image1',gray1)
    #cv2.waitKey(0)
    c = cv2.cv.WaitKey(7) % 0x100
    if c == 27:
        break
print k
array5.sort()
array6.sort()
#print array5[len(array5)/2]
#print array6[len(array6)/2]
print (float)(sum1)/k
print (float)(sum3)/k
print (float)(sum2)/3
print m
print "JAJAJAJAJAJJAJAJJAJAAAAAAAAAAAAAAAAAAAAAAAAAA"


#PROPER TESTING OF EMOTION
i=0
while i<100:
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
        
        i1=0
        for (ex,ey,ew,eh) in eyes:
            if i1==0:#LEFT EYE
                array3.append((float)(ew*eh)/(w*h))#FOR LEFT EYE
                print ex
                print ey
                print ew
            elif i1==1:#RIGHT EYE
                array4.append((float)(ew*eh)/(w*h))#FOR RIGHT EYE
                print ex
                print ey
                print ew
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
            if my>(h/2):#CHECK THE APPOROPIATE MOUTH POSITION As Mouth is present after half of face
                r=mx
                s=my
                g=mw
                h1=mh

        if flag==1:#CHECK WHETHER MOUTH  IS DETECTED OR NOT
            cv2.rectangle(roi_color, (r, s), (r + g, s + h1), (0, 0, 0), 1)
            print " MOUTH"
            file =newpath+"/imageimage"+str(i)+".png"

            # A nice feature of the imwrite method is that it will automatically choose the
            # correct format based on the file extension you provide. Convenient!
            cv2.imwrite(file,img)#WRITE IN FOLDER
            
            print g
            print h1
           
            array2.append((float)(g*h1)/(w*h))#RATIO OF MOUTH AND FACE OF BODY
            m=m+1
            print "HAHA"

    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.imshow('image',img)
    #cv2.waitKey(0)
    c = cv2.cv.WaitKey(7) % 0x100
    if c == 27:
        break
cap.release()#END WEBCAM
cv2.destroyAllWindows()#DESTROY WEBCAM WINDOW



#***********************SMILING****************************
r=0
print "HELLLO"
array2.sort()#sort an array in sorted array
count=0
count1=0
str11=""
while r<len(array2):#Check smile 
    if array2[r]!=0:
        count1=count1+1
        if array2[r]>((float)(sum2)/3):#check mouth size greater than average size set
            count=count+1
        print array2[r]
        l=array2[r]
        str11=str11+(str)(l)+"\n"
        '''print "YES"
        print array[r]
        print array1[r]
        print (array[r]*array1[r])
        print (array[r]/array1[r])'''
        
    r=r+1
print "EYES"
print sum1
print sum3
km=newpath+"\\mouth.txt"
file=open(km,'w')
file.write(str11)
file.close()

print "SMILING"
print (float)(count*100)/len(array2)# To print percentage smiling
# less than 50 no smiling
#greater than 50 smiling


#***************************SHOCKED*********************************
def minftn(a,b):
    if a!=0 and b!=0:
        if a>b:
            return b
        else:
            return a
    elif a!=0 and b==0:
        return a
    elif b!=0 and a==0:
        return b
    else:
        return 0
count3=0
count4=0
count5=0
count6=0
r=0
km1=newpath+"\\eyes.txt"
file=open(km1,'w')
str12=""
while r<(len(array3) and len(array4)):
    print "YES"
    if array3[r]!=0:
        print array3[r]
        str12=str12+(str)(array3[r])+" "
    if array4[r]!=0:
        print array4[r]
        str12=str12+(str)(array4[r])+"\n"
    if array3[r]!=0 and array3[r]>=(array5[len(array5)/2]):
        count4=count4+1
    if array4[r]!=0 and array4[r]>=(array6[len(array6)/2]):
        count3=count3+1
    if array4[r]!=0 and array3[r]!=0 and (((array4[r]+array3[r]))>=(array5[len(array5)/2]+array6[len(array6)/2])):
        count5=count5+1
    k=minftn(array4[r],array3[r])
    if (k*2)>=(array4[r]+array3[r]):
        count6=count6+1
    r=r+1
file.write(str12)
file.close()
print (float)(count3*100)/r
print (float)(count4*100)/r
print (float)((count4+count3)*100)/(2*r)
print (float)(count5*100)/r
print (float)(count6*100)/r
print count3
print count4
print r
'''if __name__ == '__main__':
    #img = sys.argv[1]
    facedet('W:\MAJOR PROJECt\Python\33.png')'''
