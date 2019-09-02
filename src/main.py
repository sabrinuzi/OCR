from text_scan import image_to_string
from text_scan import PSM_AUTO
from text_scan import TEMP_FILE
import os
import shutil

if __name__ =='__main__':
    filepath = '../unprocessed_docs'
    subfolder = 'test1'
    path = filepath + '/' + subfolder + '/'
    for file in os.listdir(path):
        if not file.endswith(".png"):
            TEMP_FILE += "/"+subfolder
            image_to_string(file, path + file, subfolder, "eng", PSM_AUTO)
            
