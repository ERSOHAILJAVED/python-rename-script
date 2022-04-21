import os

# Function to rename multiple files
def main():
    folder = "J:\google-images-download-master\google-images-download-master\poidspdaspdi[p"
    for count, filename in enumerate(os.listdir(folder)):
        dst = f"000{str(count)}.jpg"
        src =f"{folder}/{filename}" # foldername/filename, if .py file is outside folder
        dst =f"{folder}/{dst}"
        # print(src)
		
		# rename() function will
		# rename all the files
        os.rename(src, dst)
        # print(src,dst)

# Driver Code
if __name__ == '__main__':
    # Calling main() function
    main()
