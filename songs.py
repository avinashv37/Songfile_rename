__author__ = 'avinash'

import os,sys
import eyed3
class songs(object):

    newPath = raw_input("Enter the source directory : ")
    word = raw_input("\nEnter the word to be deleted : ")
    filename=[]
    filenamech=[]

    def changedir(self,newPath):
             os.chdir(self.newPath)
             print"Directory changed to : ", (os.getcwd())
             z = len(os.walk(self.newPath).next()[2])
             return z

    def checkmp3(self,dirs):
        if (self.word == ".mp3" or self.word == "mp3" or self.word == "m" or self.word == "3" or self.word == "p"):
            print "Deleting .mp3 or mp3 would delete the source format"
            self.changedir()
        else:

            print "******************************\n\nThe total number of files in folder is : ", self.z
            dirs = os.listdir(os.getcwd())
            return dirs

    # print "The dir is: %s"%dirs
    def list_directory(self):
            print"******************************\n\nThe file directory listed\n"
            for file in self.dirs:
               # if file.endswith('.mp3'):
                    print file
                    self.filename.append(file)

    def changemp3(self,dirsnew):
        for i in range(0, self.z):
            y = self.filename[i].find(self.word)
            if (y == -1):
                print "String not found in file %d" % (i + 1)
            if file.endswith('.mp3'):
                editedname = self.filename[i].replace(self.word, "")
                self.finalname = os.renames(self.filename[i], editedname)
            else:
                print "file format is not mp3"
        dirsnew = os.listdir(os.getcwd())
        return dirsnew


    def listmp3(self):
            print"******************************\n\nThe renamed files name's\n"
            for file in self.dirsnew:
                print file
                self.filenamech.append(file)
            print"******************************\n\nThe renamed titles of mp3 files\n"
    def changemp3prop(self):
        for i in range(0, self.z):
            filestring = str(self.filenamech[i])
            if filestring.endswith('.mp3'):
                path2 = self.newPath + "\\" + filestring
                print self.filenamech[i].translate(None,".mp3")
                audiofile = eyed3.load(path2)
                audiofile.tag.title = unicode(self.filenamech[i].translate(None,".mp3"))
                audiofile.tag.track_num = i+1
                audiofile.tag.save()