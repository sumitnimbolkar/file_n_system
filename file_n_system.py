# file_n_folder_crud.py


from pathlib import Path
import os


def readfileandfolder():
    path = Path('')
    dirs = list(path.rglob("*"))
    for i,v in enumerate(dirs):
        print(f"{i}.{v}")

# while(True):
    # try
print("what do you want to do :- ")
print("press 1 to create a folder")
print("press 2 to read a folder")
print("press 3 to update a folder")
print("press 4 to delete a folder")
print("press 5 to creation of a file")
print("press 6 to updating the file")
print("press 7 to deletion of file")
print("Press 0 to exit the application")

check = int(input("please tell me what you want to do : "))

if check == 1:
    dirpath = input("Tell the name you want your directory to be : ")
    path = Path(dirpath)
    path.mkdir()
    print("Sucessfully created ")

if check == 2:
    readfileandfolder()

if check == 3 :
    readfileandfolder()
    hello = input("which file name you want to change")
    path = Path(hello)
    path.rename =input("Type your new name : ")
    print ("Sucessfully created")

elif check == 4:
    readfileandfolder()
    dirname = input("enter directory name you wank to remove :")
    path = Path(dirname)
    path.rmdir() 
    print("sucessfully deleted")

elif check == 5:
    readfileandfolder()
    dirpath = input("Please input your file name with extension : ")
    path = Path(dir)
    if path.exists():
        print("sorry file already exist")

    else :
        with open(dirpath,"W") as fs:
            data = input("Just write what you want in your file ")
            fs.write(data)
            print("sucessfully done")

elif check == 6:
    readfileandfolder()
    dirpath = input("which file you want : ")
    path = Path(dirpath)
    print("Press 1 if you want to rename your file")
    print("Press 2 if you want to update your file ")
    print("Press 3 if you want to rewrite your file")
    op = input("Tell your input : ")
    if op == "1":
        newfilename = input("Please tell your new file name : ")
        p = path(newfilename)
        if not p.exists():
            os.rename(path,p)
            print("sucessfully done")
        else :
            print("choose another path coz file already exists")

    elif op == 2:
        with open(dirpath,"a") as fs:
            data = input("what do you want to add ")
            fs.write("" + data)
        print("sucessfully done")


elif check == 7 :
    readfileandfolder()
    dirpath = input("choose the file you want to delete : ")
    path = Path(dirpath)
    if path.exists():
        os.remove(path)
    else:
        print("sorry no such file exists")

elif check == 0 :
    print("exitting the application")
    exit(0)
else :
    print("Bhai shi input please ")