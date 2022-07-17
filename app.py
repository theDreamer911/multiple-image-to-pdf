from pathlib import Path 
from PIL import Image

loc = input("Folder location: ")

imageList = []
for p in Path(loc).glob("*.[jpg][png]*"):
    imageList.append(Image.open(f"{loc}\{p.name}").convert("RGB"))
    
im1 = imageList[0]
im2 = imageList[1::1]

filename = input("What name of file to be saved: ")

im1.save(filename, save_all=True, append_images=im2)