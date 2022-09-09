import os
import shutil
import face_recognition as fr
import numpy as np

cwd=os.getcwd()


def move(src,des):
    des=os.path.join(cwd,des)
    if os.path.isdir(des)==False:
        os.mkdir(des)
    des=os.path.join(des,src)
    if os.path.isfile(des)==True:
        print("File already exist wih same name!!")
        return
    src=os.path.join(cwd,src)
    if os.path.isfile(src)==False:
        print(src+"Source File Does Not Exist!!")
      
        return
    shutil.move(src,des)
    





Face_list=[] 
for file in os.listdir():
    if os.path.isfile(os.path.join(cwd,file))==False:
        continue
    try:
        img=fr.load_image_file(file)    
    except: 
        continue
    locations=fr.face_locations(img)
    if len(locations)==0:
        move(file,"other")
        continue
    area=0
    for ls in locations:
        ar=(ls[1]-ls[3])*(ls[2]-ls[0])
        if(ar>area):
            area=ar
            pt=ls
   
    fe=fr.face_encodings(img,[pt])[0]
    if len(Face_list)==0: 
        Face_list.append(fe)

    comparison=fr.compare_faces(Face_list,fe)
    cmpdist=fr.face_distance(Face_list,fe)
    matchIndex=np.argmin(cmpdist)
    if comparison[matchIndex]==False:
        Face_list.append(fe)
        move(file,str(len(Face_list)-1))
       
    else:
        move(file,str(matchIndex))
   
 