#some spacial character are remaining  like ; is not presant in images
#gap represent particular column and _ represent row number in page
from PIL import Image
from fpdf import FPDF
import cv2
img=Image.open("E:\\txttohandwritting-master\\file\\bg.png")
sizeOfSheet=img.width
gap,_=50,0
allowedchar='qwertyuiopasdfghjklzxcvbnm(),.?;1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#default_path_to_read="E:\\txttohandwritting-master\\file\\"
def Write(char):
    if char=='\n':
        pass
    else:
        global gap,_
        char=char.lower()
        try:
            cases=Image.open("E:\\txttohandwritting-master\\file\\%s.png"%char)
            cases=Image.open("E:\\txttohandwritting-master\\file\\%s.png"%char)
        except Exception as ex:
            cases=char
    
        img.paste(cases,(gap,_))
        size=cases.width
        gap+=size
        del cases

def Letters(word):
    global gap,_
    if gap > sizeOfSheet-95*(len(word)):
        gap=50
        _+=200
    for letter in word:
        if letter in allowedchar and letter !=';':
            if letter.islower():
                pass
            elif letter.isupper():
                letter.lower()
                letter+='upper'
            elif letter=='.':
                letter="fullstop"
            elif letter==',':
                letter="comma"

            elif letter==':':
                letter="colon"
            elif letter=='!':
                letter="exclamation"
            elif letter=='?':
                letter="question"

            elif letter=='(':
                letter="bracketclose"
            elif letter==')':
                letter="bracketclose"

            Write(letter)
def Word(Input,i):
    wordlist=Input.split(' ')
    for i in wordlist:
        Letters(i)
        Write('space')

        
def convert_to_pdf(path,file_name):
    name=file_name
    print(name)
    print(path)
    path_to_blank="E:\\txttohandwritting-master\\file\\bg.png"
    try:
        with open(path,'r') as file:
            data=file.read().replace('\\r',' ').strip()
            l=len(data)
            np=len(data)//600+1
            chunks,chunk_size=len(data),(len(data)//np+1)
            p=[data[i:i+chunk_size] for i in range(0,chunks,chunk_size)]
            global gap,_
            for i in range(0,len(p)):
                Word(p[i],i)
                Write('\n')
                path_to_save="E:\\txttohandwritting-master\out\\"+name+'_'+str(i)+".png"
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
        path="E:\\txttohandwritting-master\out\\"+name+"_"+str(i)
        img1=Image.open(path+".png")
        img1_convert=img1.convert('RGB')
        #img1_convert.save(path+".pdf")
        imageList.append(img1_convert)
    path_to_pdf='E:\\txttohandwritting-master\out\\' +name+'.pdf'
    img1_convert.save(path_to_pdf,save_all=True,append_images=imageList)
    print('processing  for image conversion ...............')
    return path_to_pdf

#print(convert_to_pdf("E:\\txttohandwritting-master\\file\\black.txt",'baba'))

   