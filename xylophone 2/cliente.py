#/usr/bin/env python

from xylophone.client import XyloClient
from xylophone.xylo import XyloNote

def create_xilophone(list_score):
    notes = []
    for line in list_score:
        notes.append(XyloNote(line[1],line[0],90))

    return notes
 
def main(notes):

     client = XyloClient(host="10.42.0.1", port=8080)
     client.load(notes)
     client.play()        