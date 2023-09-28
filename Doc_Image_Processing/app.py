import sys, fitz  # import the bindings
import os


def pdf2img(file_name):
    folder_name = file_name.split(".")[0] #Extracting Folder Name from file name
  
    isExisting = os.path.exists(f"./output/{folder_name}") #Checking if the path with folder name exist or not.

    if isExisting == False:                                #If the path doesn`t exist then create the path`                         
        os.mkdir(f"./output/{folder_name}")

    doc = fitz.open(file_name)  # open document
    for page in doc:  # iterate through the pages
        pix = page.get_pixmap()  # render page to an image
        pix.save(f"./output/{folder_name}/page-{page.number}.png")  # store image as a PNG
        print(f"page-{page.number}.png saved")
    print("PDF to Image Conversion Done")

    
# pdf2img("sample.pdf")
pdf2img("Learning_Python.pdf")