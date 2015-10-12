__author__ = 'avinash'
import os,sys;
import eyed3;

newPath = raw_input("Enter the source directory : ")
word = raw_input("\nEnter the word to be deleted : ")
try:
     os.chdir(newPath)
     print"Directory changed to : ", (os.getcwd())
     z = len(os.walk(newPath).next()[2])
except OSError:
     print "The entered directory is not available"
     sys.exit()
if (word == ".mp3" or word == "mp3" or word=="m" or word == "p" or word =="3"):
    print "Deleting .mp3 or mp3 would delete the source format"
else:

    print "******************************\n\nThe total number of files in folder is : ", z
    dirs = os.listdir(os.getcwd())

    # print "The dir is: %s"%dirs
    filename = []
    filenamech = []
    print"******************************\n\nThe file directory listed\n"
    for file in dirs:
       # if file.endswith('.mp3'):
            print file
            filename.append(file)

    try:
        for i in range(0, z):
            y = filename[i].find(word)
            if (y == -1):
                print "String not found in file %d" % (i + 1)
            if file.endswith('.mp3'):
                editedname = filename[i].replace(word, "")
                finalname = os.renames(filename[i], editedname)
        dirsnew = os.listdir(os.getcwd())
        print"******************************\n\nThe renamed files name's\n"
        for file in dirsnew:
            print file
            filenamech.append(file)
        print"******************************\n\nThe renamed titles of mp3 files\n"
        for i in range(0, z):
            filestring = str(filenamech[i])
            if filestring.endswith('.mp3'):
                path2 = newPath + "\\" + filestring
                print filenamech[i].translate(None,".mp3")
                audiofile = eyed3.load(path2)
                audiofile.tag.title = unicode(filenamech[i].translate(None,".mp3"))
                audiofile.tag.track_num = i+1
                audiofile.tag.save()


    except IndexError ,e:
        print e