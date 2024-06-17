import os, hashlib, base64

PREFIX = "https://raw.githubusercontent.com/schwartzh2017/CC_Week5/main/books/"

BK_DIR = "/Users/Haleigh/Documents/MSDS/Cloud_Computing/week5/books"

for i in BK_DIR:
    if i.endswith(".txt"): #check if the file is a text file
        with open(i, "r") as f: #open the file in read mode

            text = f.read() #read the contents of the file

            m = hashlib.md5() #initiale the md5 hash object
            m.update(text.encode('utf-8')) #convert the text to bytes and update the hash object (update method requres a bytes-like object)
            digest = m.digest() #return a bytes object representing the hash
            b64 = base64.b64encode(digest).decode('utf-8') #first convert the bytes object to a base64 encoded bytes object, then decode it to a utf-8 string

            f.seek(0, os.SEEK_END) #go to the end of the file
            size = f.tell() #find size of file in bytes

            print(f"{PREFIX}{i}\t{size}\t{b64}") #print raw github content url, size of file, and base64 encoded md5 hash