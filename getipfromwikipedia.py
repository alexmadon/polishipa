#!/usr/bin/python3
import re
import requests
import bs4

text="""
Moja kochana
Moja kochana
Moja kochana wciąż nie umiem z siebie wydrzeć naszych słów
W mej głowie nie wiem skąd
"""

f=open("filter.txt")
lines=f.readlines()
f.close()

text=''.join(lines)


words = re.compile("\s+").split(text)
print(len(words))

words=set(words)
print(len(words))
print(words)


for word in words:
    urls=[
        ("IPA","https://en.wiktionary.org/wiki/"+word),
        # ("ipa","https://pl.wiktionary.org/wiki/"+word),
    ]
    found=False
    for (cname,url) in urls:
        print("#",url)
        r = requests.get(url)
        c = r.content
        if "Polish" in r.content.decode("utf-8"):
            print("found Polish")
            soup = bs4.BeautifulSoup(c,'html.parser')
            ipas = soup.find_all('span', {'class' : cname}) # <span class="IPA">/ˈɕrɔ.da/</span>
            if len(ipas)==1: # restrict o exact one match
                for ipa in ipas:
                    if found:
                        comment="# "
                    else:
                        comment=""
                    print("        ",comment,'("',word,'","',ipa.get_text(),'"),',sep='')
                    found=True
            found=False
            
