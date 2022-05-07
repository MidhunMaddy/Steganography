from logging import raiseExceptions
from PIL import Image

def mod_pix(binary,p):
    pix=list(p)
    for num in range(0,8):
        if(binary[num]=='1'):
            if(pix[num]%2==0):
                if(pix[num]==0):
                   pix[num]+=1
                else:
                    pix[num]-=1
        else:
            if(pix[num]%2!=0):
                pix[num]+=1
        
    if(pix[8]%2!=0):
        pix[8]-=1

    return pix

def encode():
    im_name=input("Enter image path (in valid format):")
    data=input("Enter data :")

    im=Image.open(im_name)
    b_data=[]
    for i in data:
        b_data.append(format(ord(i),'08b'))
    new_imag=im.copy()

    k=iter(list(new_imag.getdata()))
    new_pix=[]

    for binary in b_data:
        new_pix+=mod_pix(binary,k.__next__()*3)
        
    if(new_pix[-1]==0):
        (new_pix[-1])-=1
    else:
        (new_pix[-1])-=1

    w=new_imag.size[0]
    a=new_imag.load()
    color=iter(new_pix)
    length=len(new_pix)
    x=0
    y=0
    while(length!=0):

        a[x,y]=(int(next(color)),int(next(color)),int(next(color)))
        if(x==w-1):
            x = 0
            y += 1
		
        else:
            x+=1
        length-=3
    new_image_name=input("Enter new file name:")
    new_imag.save(new_image_name)

def decode():
    image_name=input("Enter image path (with vaild format):")
    imag=Image.open(image_name)
    w,h=imag.size
    imag_pix_data=[]
    for r in range(0,h,1):
        for c in range(0,w,1):
            imag_pix_data+=imag.getpixel((c,r))
    c=1
    data=''
    bin_data=''
    while(True):
        values=imag_pix_data[c-1]
        if (c%9==0):
            data +=chr(int(bin_data, 2))
            bin_data=''
            if (values%2!=0):
                return data
        else:
            if(values%2==0):
                bin_data+='0'
            else:
                bin_data+='1'
        c+=1



def main():
    
    print("Note: Use foramts such as .bmp,.png,etc")
    i=int(input("1. Encode\n2. Decode\n"))
    if(i==1):
        encode()
    elif(i==2):
        print('Decoded data:'+ decode())
    else:
        raiseExceptions("Enter vaild input!!")


main()