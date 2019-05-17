
#Take input link
print("Enter the link to download")
link = input()

#Find name of the file from the link
rev = link[::-1]
#print(rev)
n = ""
for k in rev:

    if k != '/':
        n += k
    else:
        break
name = n[::-1]
print(name)

#urllib
import urllib.request
url = link
print ("download start!")
filename, headers = urllib.request.urlretrieve(url, filename= name)
print ("download complete!")
print ("download file location: ", filenam)
print ("download headers: ", headers)
