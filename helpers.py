from bidi.algorithm import get_display
import csv
from xml.dom import minidom

file = open("books.csv", "r")
books = list(csv.reader(file, delimiter=","))
file.close
print(books)
        # books2 = ['TanachIndex.xml', 'Zechariah.xml','Zephaniah.xml','Amos.xml','Chronicles_1.xml','Chronicles_2.xml','Daniel.xml','Deuteronomy.xml','Ecclesiastes.xml','Esther.xml','Exodus.DH.xml',
        #     'Exodus.xml','Ezekiel.xml','Ezra.xml','Genesis.xml','Habakkuk.xml','Haggai.xml','Hosea.xml','Isaiah.xml','Jeremiah.xml','Job.xml','Joel.xml','Jonah.xml','Joshua.xml',
        #     'Judges.xml','Kings_1.xml','Kings_2.xml','Lamentations.xml','Leviticus.DH.xml','Leviticus.xml','Malachi.xml','Micah.xml','Nahum.xml','Nehemiah.xml','Numbers.xml','Obadiah.xml',
        #     'Proverbs.xml','Psalms.xml','Ruth.xml','Samuel_1.xml','Samuel_2.xml','Song_of_Songs.xml']
def get_Hebrew_Text(book, chapter, firstvs, lastvs):
    
    doc = minidom.parse("Amos.xml")
    # doc.getElementsByTagName returns the NodeList
    chps = doc.getElementsByTagName("c")
    # get verses in a chapter
    vss = chps[0].getElementsByTagName("v")
    for vs in vss:
        words = vs.getElementsByTagName("w")
        for word in words:
            #     verse_text = ""
            #     verse_text += word.firstChild.data + " "
            # verse_text += "\n" 
            f = open('output.txt', 'a', encoding="utf-8")
            f.write(word.firstChild.data + " ")
        f.write(f"\n")
