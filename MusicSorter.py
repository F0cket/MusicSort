import os
import re
import io
import sys
from mutagen.easyid3 import EasyID3
import argparse
import time
import mutagen
import shutil
from mutagen.flac import FLAC
from mutagen.wave import WAVE
from mutagen.easymp4 import EasyMP4
EasyID3.RegisterTextKey('comment', 'COMM')
badsymbols = ['|','*','\"','>','<',':','?']

def direxist(directory):
    if not os.path.exists(directory):
        os.makedirs(str(directory))

def validname(name):
    for i in badsymbols:
        name = name.replace(i, '')
    name = name.replace("\\",'&')
    name = name.replace("/",'&')
    while name[0] == '.':
        name = name[1:]
    while name[-1] == '.':
        name = name[:-1]
    return(name)

filepath = input("Where are the files: ")
outpath = input("Where should the sorted files go: ")

for r, d, f in os.walk(filepath):
    for file in f:
        filedir = os.path.join(r,file)
        try:
            if ".flac" in file:
                fileTags = FLAC(os.path.join(r,file))
            elif ".wav" in file:
                direxist(os.path.join(outpath, r"Wav's"))
                shutil.copy(filedir,os.path.join(outpath, r"Wav's",file))
                continue
            elif ".m4a" in file:
                fileTags = EasyMP4(os.path.join(r,file))
            else:
                fileTags = EasyID3(os.path.join(r,file))

            album = str(fileTags["album"])[2:-2]

            try:
                title = str(fileTags["title"])[2:-2]
            except:
                direxist(os.path.join(outpath,"No Title"))
                shutil.copy(filedir,os.path.join(outpath,"No Title",file))
                continue

            try:
                artist = str(fileTags["artist"])[2:-2]
            except:
                direxist(os.path.join(outpath, "No Artist"))
                shutil.copy(filedir,os.path.join(outpath,"No Artist",file))
                continue

            try:
                album = str(fileTags["album"])[2:-2]
            except:
                artist = validname(artist)
                direxist(os.path.join(outpath,"No album",artist))
                shutil.copy(filedir,os.path.join(outpath,"No album",artist,file))
                continue

            try:
                albumartist = str(fileTags["albumartist"])[2:-2]
            except:
                artist = validname(artist)
                album = validname(album)
                direxist(os.path.join(outpath,"No Album Artist",artist,album))
                shutil.copy(filedir,os.path.join(outpath,"No Album Artist",artist,album,file))
                continue

            try:
                albumartist = validname(albumartist)
                album = validname(album)
                direxist(os.path.join(outpath,albumartist,album))
                shutil.copy(filedir,os.path.join(outpath,albumartist,album,file))
            except Exception as e:
                print(filedir,e)

        except Exception as e:
            continue

