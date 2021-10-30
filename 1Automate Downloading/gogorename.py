from os import walk, rename

location = r'D:\\'

input_ = 'we are going to remove (....gogoanime) from every file: '
#remove gogoanime
for root, path, file in walk(location):
    for i in file:
        # print((root+"\\"+i))
        a = (root+"\\"+i)
        new_dir = a
        try:
            new_dir = root+"\\"+(a[a.index('gogoanime')+10:])
            print(i)
            print(new_dir)
        except:
            pass
        rename(a,new_dir)


# os.rename(r'file path\OLD file name.file type',r'file path\NEW file name.file type')