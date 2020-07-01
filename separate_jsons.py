### For Luis ###########
import glob
import shutil
import json


def filter_jsons(folder_path, outfolder):
	folder_path = folder_path + r"\\*.json"
	file_list = glob.glob(folder_path)
	for fname in file_list:
		name = fname.strip().split(r'\\')[-1]
		shutil.move(fname, outfolder + "\\" + name)

	
if __name__ == "__main__":
	
	#args
	folder_path = r"C:\Users\lcasado\Documents\Trainig"
	outfolder = r"C:\Users\lcasado\Documents\Trainig\jsons"
		
	#func call
	filter_jsons(folder_path, outfolder)
	
