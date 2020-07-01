import json
import cv2
import shutil
import os



def copy_json(folder_path):
    source = os.listdir(folder_path)

    for file in source:
        if file.endswith('.json'):
            '''
            with open(file, "r") as from, open("to.json", "r") as to:
                to_insert = json.load(from)
                destination = json.load(to)
                destination.append(to_insert) #The exact nature of this line varies. See below.
            with open("to.json", "w") as to:
                json.dump(to, destination)
                '''
            print(json)




if __name__ == "__main__":
		
	#Video in & out
    folder_path = (r"C:\Users\lcasado\Documents\Trainig")

    copy_json(folder_path)
	
