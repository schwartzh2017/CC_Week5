import os, hashlib, base64

PREFIX = "https://raw.githubusercontent.com/schwartzh2017/CC_Week5/main/books/" #prefix to use for the raw github content url, update this for desired output

BK_DIR = "/Users/Haleigh/Documents/MSDS/Cloud_Computing/week5/books" #directory where the txt files are stored, update this for desired output

OUTPUT_FILE = "/Users/Haleigh/Documents/MSDS/Cloud_Computing/week5/output.tsv" #output file to write the results to, update this for desired output


with open(OUTPUT_FILE, "w") as output_file: #open the output file in write mode
    output_file.write("TsvHttpData-1.0\n") #write the header to the output file, don't want it to repeat with each instance of the loop

    for i in os.listdir(BK_DIR): #go through each file in directory
        if i.endswith(".txt"): #check if the file is a text file
            path = os.path.join(BK_DIR, i) #get full path of file
            with open(path, "r") as f: #open the file in read mode

                text = f.read() #read the contents of the file

                m = hashlib.md5() #initiale the md5 hash object
                m.update(text.encode('utf-8')) #convert the text to bytes and update the hash object (update method requres a bytes-like object)
                digest = m.digest() #return a bytes object representing the hash
                b64 = base64.b64encode(digest).decode('utf-8') #first convert the bytes object to a base64 encoded bytes object, then decode it to a utf-8 string

                f.seek(0, os.SEEK_END) #go to the end of the file
                size = f.tell() #find size of file in bytes

                output_file.write(f"{PREFIX}{i}\t{size}\t{b64}\n") #save raw github content url, size of file, and base64 encoded md5 hash to the output file
