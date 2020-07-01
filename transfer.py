############### For Luis ##################################

import os, sys
import json
import shutil
import labelme
from os.path import abspath
import pathlib


def transfer_to_folder(folder_path, outfold):

	img_dir = 'images'
	labels = 'labels'
	visualization = 'visualization'
	labelnames_txt = 'names_txt'

	im_path = os.path.join(outfold, img_dir)
	pathlib.Path(im_path).mkdir(exist_ok=True, parents=True)

	lab_path = os.path.join(outfold, labels)
	pathlib.Path(lab_path).mkdir(exist_ok=True, parents=True)

	viz_path = os.path.join(outfold, visualization)
	pathlib.Path(viz_path).mkdir(exist_ok=True, parents=True)

	text_path = os.path.join(outfold, labelnames_txt)
	pathlib.Path(text_path).mkdir(exist_ok=True, parents=True)



	print("Img_dir: ", (os.path.abspath(img_dir)))

	#directory = os.listdir(folder_path)
	directory = [ name for name in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, name)) ]
	for item in directory:
		print("Reading ", item)
		#counter = 0
		tmp = os.path.join(folder_path, item)
		
		shutil.move(os.path.join(tmp, "label.png"), os.path.join(lab_path, item) + ".png")
		shutil.move(os.path.join(tmp, "label_viz.png"), os.path.join(viz_path, item) + ".png")
		shutil.move(os.path.join(tmp, "img.png"), os.path.join(im_path, item) + ".png")
		shutil.move(os.path.join(tmp, "label_names.txt"), os.path.join(text_path, item) + ".txt")

		

if __name__ == "__main__":

    #folder_path = r'C:\Users\lcasado\Documents\Trainig'
    folder_path = r"C:\Users\lcasado\Documents\Backup\glove_overhand_1\json_files"
    outfold = r"C:\Users\lcasado\Documents\output_folder"

    transfer_to_folder(folder_path, outfold)

