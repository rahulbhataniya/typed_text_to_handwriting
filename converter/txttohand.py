#some spacial character are remaining  like ; is not presant in images
#gap represent particular column and _ represent row number in page
from PIL import Image
from fpdf import FPDF
import cv2
import os
img=Image.open("converter\\static\\pre_train_data\\file\\bg.png")
sizeOfSheet=img.width
gap,_=50,0
allowedchar='qwertyuiopasdfghjklzxcvbnm(),.?;1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits='0123456789'
#default_path_to_read="E:\\txttohandwritting-master\\file\\"
def Write(char,path_to_character):
    #make special case for space
    if char=='\n':
        pass
    else:
        global gap,_
        split_char=char.split('_')
        try:
            path_to_open=str()
            if split_char[1] not in ['digit','small','upper']:
                path_to_open=f'/text_to_hand/converter/static/pre_train_data/file/{split_char[1]}.png'
            else:
                path_to_open=os.path.join(path_to_character,f'{char}.png')
            cases=Image.open(path_to_open)
        except Exception as ex:
            cases=char
    
        img.paste(cases,(gap,_))
        size=cases.width
        gap+=size
        del cases

def Letters(word,path_to_character):
    global gap,_
    if gap > sizeOfSheet-95*(len(word)):
        gap=50
        _+=200
    for letter in word:
        if letter in allowedchar:
            if letter in digits:
                letter+='_digit'
            elif letter.islower():
                letter+='_small'
            elif letter.isupper():
                letter+='_upper'
            elif letter=='.' or letter==";":
                letter="_fullstop"
            elif letter==',':
                letter="_comma"
            elif letter==':':
                letter="_colon"
            elif letter=='!':
                letter="_exclamation"
            elif letter=='?':
                letter="_question"
            elif letter=='(':
                letter="_bracketclose"
            elif letter==')':
                letter="_bracketclose"
            Write(letter,path_to_character)
def Word(Input,i,path_to_character):
    wordlist=Input.split(' ')
    for i in wordlist:
        Letters(i,path_to_character)
        Write('_space',path_to_character)

        
def convert_to_pdf(path,file_name,path_to_character="/text_to_hand/media/res/rahul"):
    name=file_name
    print(name)
    print(path)
    path_to_blank="converter\\static\\pre_train_data\\file\\bg.png"
    try:
        with open(path,'r') as file:
            data=file.read().replace('\\r',' ').strip()
            l=len(data)
            np=len(data)//600+1
            chunks,chunk_size=len(data),(len(data)//np+1)
            p=[data[i:i+chunk_size] for i in range(0,chunks,chunk_size)]
            global gap,_
            for i in range(0,len(p)):
                Word(p[i],i,path_to_character)
                Write('\n',path_to_character)
                path_to_save="media\\safe_for_convertion\\"+name+'_'+str(i)+".png"
                global img
                img.save(path_to_save)
                img1=Image.open(path_to_blank)
                img=img1
                
                gap , _ =50,0
    except ValueError as E:
        print("{}\nTry again",format(E))
    imageList=[]
    img1_convert=Image.open(path_to_blank)
    for i in range(0,len(p)):
        path="media\\safe_for_convertion\\"+name+"_"+str(i)
        img1=Image.open(path+".png")
        img1_convert=img1.convert('RGB')
        #img1_convert.save(path+".pdf")
        imageList.append(img1_convert)
    path_to_pdf='media\\safe_for_convertion\\' +name+'.pdf'
    imageList[0].save(path_to_pdf,save_all=True,append_images=imageList[1:])
    print('processing  for image conversion ...............')
    return path_to_pdf
if __name__=="__main__":
    file_name='rahul'
    path='/text_to_hand/converter/static/upload/input_for_project.txt'
    path_to_character="/text_to_hand/media/res/rahul"
    convert_to_pdf(path,file_name,path_to_character)

#print(convert_to_pdf("E:\\txttohandwritting-master\\file\\black.txt",'baba'))
