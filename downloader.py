#Take input link
print("Enter the link to download")
link = input()

y= link[:23]
#print(y)

if y == 'https://www.youtube.com':
    print("To download single video Enter 1")
    print("To download the hole playlist Enter 2")
    i = input()
    print(i)

    if i == "1":
        print("Downloading......")
        from pytube import YouTube
        YouTube(link).streams.first().download()
        print("Download Completed")

    elif i == "2":
        print("Downloading......")
        from pytube import Playlist
        pl = Playlist(link)
        pl.download_all()
        print("Download Completed")

    else:
        print("Your response is Incorrect")



else:
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
    print ("Downloading")
    filename, headers = urllib.request.urlretrieve(url, filename= name)
    print ("download complete!")
    print ("download file location: ", filenam)
    print ("download headers: ", headers)
