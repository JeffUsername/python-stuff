#! python3

import requests, os, bs4
tag = input('enter search term: ')
number = int(input('enter number of image to add (an int): '))
url = 'https://imgur.com/search?q='+tag         # starting url
os.makedirs('imgur', exist_ok=True)    # store comics in ./xkcd

    # Download the page.

res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
# Find the URL of the comic image.
comicElem = soup.select('img')
numOpen = min(number, len(comicElem))
i=0
while i in range(numOpen):
    print('Downloading page %s...' % url)
    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicUrl = 'https:' + comicElem[i].get('src')
        # Download the image.
        print('Downloading image %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()
        # Save the image to ./xkcd.
        imageFile = open(os.path.join('imgur', os.path.basename(comicUrl)),'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
    i+=1
    # Get the Prev button's url.
    # prevLink = soup.select('a[rel="prev"]')[0]
    # url = 'https://xkcd.com' + prevLink.get('href')

print('Done.')
print('Done.')