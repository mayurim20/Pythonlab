str1="python""\n""is""\n""high""\n""level""\n""programming""\n""language"
fw=open("file.txt","w")
fw.write(str1)
fw.close()

fr=open("file.txt","r")
str2=fr.readlines()
for i in str2:
    print(i)
