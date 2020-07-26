import glob
import os
import os.path
import re

imNames = glob.glob(os.path.join('train', "*"))
i=0

# print(((imNames[i].split('\\')[1]).split('.'))[0])



names = list()
for i in range(len(imNames)):
    name = re.split(r'[\\,.]',imNames[i])[1]
    names.append(name+'\n')
      
file = open('codes.txt','w+')
file.writelines(names)

