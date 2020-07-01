import os
# Function to rename multiple files
def main():
   path=r"C:\Users\lcasado\Documents\webcam images\glove_overhand_1\copy\images"
   frame_counter = 0
   for filename in os.listdir(path):
      my_dest =(str(frame_counter).zfill(4)) + ".json"
      my_source =path + filename
      my_dest =path + my_dest
      # rename() function will
      # rename all the files
      os.rename(my_source, my_dest)
      frame_counter += 4
# Driver Code
if __name__ == '__main__':
   # Calling main() function
   main()