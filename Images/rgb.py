from PIL import Image # PIL: Python Imaging Library
import numpy as np
import pandas as pd
import os # operating system module for file and directory

folder_path = r'C:\Users\nathan-mekuria\Desktop\A\Desktop\Project\Project Chemometrics\Cropped'
#data = []
#image_path = os.path.join(folder_path, "1.jpg")
#image = Image.open(image_path)
#np_image = np.array(image)
#average_rgb = np_iamge.mean(axis= (0,1))
#data.append([image_name, *average_rgb])
#df = pd.DataFrame(data, columns= ['Image Name', 'Average R', 'Average G', 'Average B'])
#print(df)

data = []

for image_name in os.listdir(folder_path):
    if image_name.endswith(('jpg')):
        # getting the address and name of the image
        image_path = os.path.join(folder_path, image_name)
        image = Image.open(image_path)
        
        np_image = np.array(image)
    
        average_rgb = np_image.mean(axis= (0,1))
    
        data.append([image_name, *average_rgb])
    
df = pd.DataFrame(data, columns= ['Image Name', 'Average R', 'Average G', 'Average B'])

print(df)

#df.to_excel('average_rgb_values.xlsx', index= False) # index False excludes df index in the excel file
