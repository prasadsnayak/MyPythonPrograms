import os
import re
import shutil

path_filetype = input('Enter file type extension seperated by comma: ')
extension = re.split("[, \-!?:]+", path_filetype)
path_src = input('Enter source path: ')
path_dest = input('Enter destination path: ')

for (dirpath, dirnames, filenames) in os.walk(path_src):
	for filename in filenames:
		for ext in extension:
			if filename.endswith(ext):
				src_file = os.path.join(dirpath, filename)
				shutil.copy(src_file, path_dest)