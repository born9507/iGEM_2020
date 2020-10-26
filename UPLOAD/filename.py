# Capitalize
import os.path
import os

def capitalize():
    path = os.getcwd()

    for filename in os.listdir(path):
        if filename.split('.')[-1] == 'html':
            print(filename.capitalize())
            os.rename(path+'\\'+filename, path+'\\'+str(filename.capitalize()))

if __name__ == '__main__':
    print("hello")