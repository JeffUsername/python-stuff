#! python3

import requests, os, bs4
url = input('Enter url: ')
number = int(input('enter number of image to add (an int): '))
os.makedirs('link', exist_ok=True)    # store comics in ./xkcd

res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
# Find the URL of the comic image.
comicElem = soup.select('a')
numOpen = min(number, len(comicElem))
i=1
while i in range(numOpen):
    comicUrl = comicElem[i].get('href')
    # Download the image.
    print('Downloading page %s...' % (comicUrl))
    res = requests.get(comicUrl)
    try:
        res.raise_for_status()
    except:
        print('Link not good')
        i+=1
        continue
    if comicElem == []:
        print('Could not find page.')
    else:
        comicUrl = comicElem[i].get('href')
        # Download the image.
        print('Downloading page %s...' % (comicUrl))
        res = requests.get(comicUrl)
        try:
            res.raise_for_status()
        except:
           print('Link not good')
           i+=1
           continue
        # Save the image to ./xkcd.
        imageFile = open(os.path.join('link', 'time'+os.path.basename(comicUrl)),'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
    i+=1

print('Done.')
print('Done.')