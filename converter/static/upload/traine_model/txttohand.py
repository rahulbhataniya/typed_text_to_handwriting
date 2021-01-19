#some spacial character are remaining  like ; is not presant in images
#gap represent particular column and _ represent row number in page

from PIL import Image
from fpdf import FPDF
img=Image.open("E:\studymaterial\python\project\\txttohandwritting-master\\file\\bg.png")
sizeOfSheet=img.width
gap,_=50,0
allowedchar='qwertyuiopasdfghjklzxcvbnm(),.?;1234567890'

def Write(char):
    if char=='\n':
        pass
    else:
        global gap,_
        char.lower()
        try:
            cases=Image.open("E:\studymaterial\python\project\\txttohandwritting-master\\file\\%s.png"%char)
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
                letter+='Upper'
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




def convert_to_pdf():
    name="babu"
    try:
        with open("E:/studymaterial/python/project/txttohandwritting-master/file/black.txt",'r') as file:
            data=file.read().replace('\n','')
            l=len(data)
            np=len(data)//600
            chunks,chunk_size=len(data),(len(data)//np+1)
            p=[data[i:i+chunk_size] for i in range(0,chunks,chunk_size)]
            global gap,_
            for i in range(0,len(p)):
                Word(p[i],i)
                Write('\n')
                path="E:\studymaterial\python\project\\txttohandwritting-master\out\\"+name+'_'+str(i)+".png"
                global img
                
                img.save(path)
                img1=Image.open("E:\studymaterial\python\project\\txttohandwritting-master\\file\\bg.png")
                img=img1
                
                gap , _ =50,0
    except ValueError as E:
        print("{}\nTry again",format(E))
    imageList=[]
    img1_convert=Image.open("E:\studymaterial\python\project\\txttohandwritting-master\\file\\bg.png")
    for i in range(0,len(p)):
        path="E:\studymaterial\python\project\\txttohandwritting-master\out\\"+name+"_"+str(i)
        img1=Image.open(path+".png")
        img1_convert=img1.convert('RGB')
        #img1_convert.save(path+".pdf")
        imageList.append(img1_convert)
    img1_convert.save('E:\studymaterial\python\project\\txttohandwritting-master\out\\' +name+'.pdf',save_all=True,append_images=imageList)
    print('processing  for image conversion ...............')
    print('hii')

convert_to_pdf()

   