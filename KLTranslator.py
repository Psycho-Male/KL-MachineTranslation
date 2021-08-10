#to make an executable run this in command line: pyinstaller -F yourprogram.py
#list of supported languages: https://yandex.com/dev/translate/doc/dg/concepts/api-overview.html#api-overview__languages
#Azerbaijani	az	Malayalam	ml
#Albanian	sq	Maltese	mt
#Amharic	am	Macedonian	mk
#English	en	Maori	mi
#Arabic	ar	Marathi	mr
#Armenian	hy	Mari	mhr
#Afrikaans	af	Mongolian	mn
#Basque	eu	German	de
#Bashkir	ba	Nepalese	ne
#Belarusian	be	Norwegian	no
#Bengal	bn	Punjabi	pa
#Burmese	my	Papiamento	pap
#Bulgarian	bg	Persian	fa
#Bosnian	bs	Polish	pl
#Welsh	cy	Portuguese	pt
#Hungarian	hu	Romanian	ro
#Vietnamese	vi	Russian	ru
#Haitian (Creole)	ht	Cebuano	ceb
#Galician	gl	Serbian	sr
#Dutch	nl	Sinhalese	si
#Hill Mari	mrj	Slovak	sk
#Greek	el	Slovenian	sl
#Georgian	ka	Swahili	sw
#Gujarati	gu	Sundanese	su
#Danish	da	Tajik	tg
#Hebrew	he	Thai	th
#Yiddish	yi	Tagalog	tl
#Indonesian	id	Tamil	ta
#Irish	ga	Tartar	tt
#Italian	it	Telugu	te
#Icelandic	is	Turkish	tr
#Spanish	es	Udmurt	udm
#Kazakh	kk	Uzbek	uz
#Kannada	kn	Ukrainian	uk
#Catalan	ca	Urdu	ur
#Kirghiz	ky	Finnish	fi
#Chinese	zh	French	fr
#Korean	ko	Hindi	hi
#Xhosa	xh	Croatian	hr
#Khmer	km	Czech	cs
#Laotian	lo	Swedish	sv
#Latin	la	Scottish	gd
#Latvian	lv	Estonian	et
#Lithuanian	lt	Esperanto	eo
#Luxembourg	lb	Javanese	jv
#Malagasy	mg	Japanese	ja
#Malay	ms	
language_name=[
"Azerbaijani","Malayalam",
"Albanian","Maltese",
"Amharic","Macedonian",
"English","Maori",
"Arabic","Marathi",
"Armenian","Mari",
"Afrikaans","Mongolian",
"Basque","German",
"Bashkir","Nepalese",
"Belarusian","Norwegian",
"Bengal","Punjabi",
"Burmese","Papiamento",
"Bulgarian","Persian",
"Bosnian","Polish",
"Welsh","Portuguese",
"Hungarian","Romanian",
"Vietnamese","Russian",
"Haitian","eole",
"Galician","Serbian",
"Dutch","Sinhalese",
"Hill Mari","Slovak",
"Greek","Slovenian",
"Georgian","Swahili",
"Gujarati","Sundanese",
"Danish","Tajik",
"Hebrew","Thai",
"Yiddish","Tagalog",
"Indonesian","Tamil",
"Irish","Tartar",
"Italian","Telugu",
"Icelandic","Turkish",
"Spanish","Udmurt",
"Kazakh","Uzbek",
"Kannada","Ukrainian",
"Catalan","Urdu",
"Kirghiz","Finnish",
"Chinese","French",
"Korean","Hindi",
"Xhosa","Croatian",
"Khmer","Czech",
"Laotian","Swedish",
"Latin","Scottish",
"Latvian","Estonian",
"Lithuanian","Esperanto",
"Luxembourg","Javanese",
"Malagasy","Japanese",
"Malay"
]
language_code=[
"az","ml",
"sq","mt",
"am","mk",
"en","mi",
"ar","mr",
"hy","mhr",
"af","mn",
"eu","de",
"ba","ne",
"be","no",
"bn","pa",
"my","pap",
"bg","fa",
"bs","pl",
"cy","pt",
"hu","ro",
"vi","ru",
"ht","ceb",
"gl","sr",
"nl","si",
"mrj","sk",
"el","sl",
"ka","sw",
"gu","su",
"da","tg",
"he","th",
"yi","tl",
"id","ta",
"ga","tt",
"it","te",
"is","tr",
"es","udm",
"kk","uz",
"kn","uk",
"ca","ur",
"ky","fi",
"zh","fr",
"ko","hi",
"xh","hr",
"km","cs",
"lo","sv",
"la","gd",
"lv","et",
"lt","eo",
"lb","jv",
"mg","ja",
"ms"]
#coding:utf8
from googletrans import Translator
import json,os
import requests,time
import glob
import sys
#from os import listdir

special_characters="!@#$%^&*()-+?_=<>/[]"
#special_characters="!@#$%^&*()-+?_=<>/"

def yanTrans(text,lang):
    key="trnsl.1.1.20210804T163643Z.4b57461e204c6f41.2b55797a06762b1b5c80826703973d96ef20b934"
    url_yandex="https://translate.yandex.net/api/v1.5/tr.json/translate?key=%s&text=%s&lang=%s" % (key,text,lang)
    #time.sleep(0.3)
    response=requests.get(url_yandex,timeout=None)
    response_data=eval(response.content.decode("utf-8"))
    lb=response_data["text"][0]
    return lb
#Make a function for clear code
translator=Translator()
def trans(text,lang):
    srcLang=translator.detect(text)
    print(srcLang)
    return translator.translate(text,src="en",dest=lang).text

#Choose how many languages we'll be translating into
#folders=["tr","es","it","ja"]
#Files we'll be translating
files=[]
for file in glob.glob("*.json"):
    files.append(file)
    #files.append("Dianna.json")
print("Files %s"%files)
path_prefix="C:/Users/Manko/Documents/GameMakerStudio2/Kingdom Lost/datafiles/Interaction/";
debug=False


i=0
while i<len(language_name):
    print(language_name[i]+": "+language_code[i],end="|")
    if i%2==0:
        print()
    i+=1
lang=input("Input language code(full list can be found here:yandex.com/dev/translate/doc/dg/concepts/api-overview.html#api-overview__languages):")
i=0
codeFound=False;
while i<len(language_name):
    if language_code[i]==lang:
        codeFound=True
        break
    i+=1
if not codeFound:
    input("Wrong language code, aborting...")
    quit()
#MAIN LOOP
print("<<<<<<<<<Translate Language: %s>>>>>>>>>>>"%lang)

#Start translation
n=0
for j in files:
    print("Open file: %s"%(path_prefix+j))
    f=open(path_prefix+j,"r")
    try:
        data_json=json.load(f)
    except:
        print("Json %s might be empty."%path_prefix+j)
        continue
    jsonLen=len(data_json)
    print("Found %d titles."%jsonLen)
    while n<jsonLen:
        #Get the body part of .json
        print("[lang=%s]%s\n..."%(lang,data_json[n]["title"]))
        #This fixes .|
        #data_json[n]["body"]=data_json[n]["body"].replace("./",".|")
        text=data_json[n]["body"]
        split=text.split("\n");
        if debug:
            print(yanTrans(split[0],lang))
            print(yanTrans(translated,lang))
        for sen in split:
            if sen=="":
                continue
            sp=sen.split(":")
            if len(sp)>1:
                if debug:
                    print("Text: ",text)
                    print("sp[1]: ",sp[1])
                translated=sp[1],yanTrans(sp[1],lang)
                if debug:
                    print("Translated: ",translated[1])
                data_json[n]["body"]=data_json[n]["body"].replace(sp[1],translated[1])
                if debug:
                    print("Text: ",data_json[n]["body"])
            else:
                specialFound=False
                for c in special_characters:
                    if c==sen[0]:
                        if debug:
                            print("Special char found: %s."%c)
                        specialFound=True
                        break
                if not specialFound:
                    try:
                        data_json[n]["body"]=data_json[n]["body"].replace(sen,yanTrans(sen,lang))
                    except:
                        print(sys.exc_info()[0])
                        print(yanTrans(sen,lang))
        n+=1
    with open (j,"w") as outfile:
        n=0
        print("Dump into %s/%s"%(path,j))
        json.dump(data_json,outfile)
        #print(data_json[n])
input("Press ENTER to exit")
