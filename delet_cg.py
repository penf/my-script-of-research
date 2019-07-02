# -*- coding: utf-8 -*-
import shutil, os

# the function of this script is to delete "cg" in  directory.
apk_file_directory = r"D:\malware_family"
print("Reading apks from", apk_file_directory)

for root, dirs, fnames in os.walk(apk_file_directory):
     for  dir in dirs:
         if (dir == "cg" ):
             path_del=os.path.join(root,dir)
             shutil.rmtree(path_del)