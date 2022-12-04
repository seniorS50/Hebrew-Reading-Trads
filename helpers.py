from bidi.algorithm import get_display
import json
from xml.dom import minidom

def get_Book_Index():
    # Get info from the index
    doc = minidom.parse("Books/TanachIndex.xml")
    index = doc.getElementsByTagName("book")
    book_info = []
    for book in index:
        name = book.getElementsByTagName("name")[0].firstChild.data
        abbrev = book.getElementsByTagName("abbrev")[0].firstChild.data
        filename = book.getElementsByTagName("filename")[0].firstChild.data
        # Get all the chapter data for each book
        c = book.getElementsByTagName("c")
        chapters = []
        for chapter in c:
            chapters.append({
                "chps": chapter.getAttribute("n"),
                "vss": chapter.getElementsByTagName("vs")[0].firstChild.data
            })
        book_info.append({
            "name": name,
            "abbrev": abbrev,
            "filename": filename,
            "chapters": chapters
        })
        
    # return a list of dicts with the following info:
    # name
    # abbrevfilename
    # chapters - a list of dicts with the attributes:
    #     chp (which chapter)
    #     vss (which vss)
    return book_info

def get_Hebrew_Text(book, chapter, firstvs = 1, lastvs = -1):
    # load the index
    index = get_Book_Index()

    for entry in index:
        if entry["name"] == book or entry["abbrev"] == book:
            filename = entry["filename"]
            chapters = entry["chapters"]
            break
    if not filename:
        print("error: book not found. Searching by abbreviation not supported yet")
        return(1)
    # Check that the book and chapter numbers make sense
    if chapter < 1 or chapter > len(chapters) + 1:
        print("invalid chapter")
        return(2)
    # If there is an invalid or default verse ranger, just go ahead and give the whole chapter back
    if firstvs > lastvs or lastvs > int(chapters[chapter - 1]["vss"]):
        print("invalid verse range")
        firstvs = 1
        lastvs = int(chapters[chapter-1]["vss"])
    
    # load the xml of the specific book
    doc = minidom.parse("Books/" + filename + ".xml")
    # doc.getElementsByTagName returns the NodeList
    chps = doc.getElementsByTagName("c")
    # get verses in a chapter
    vss = chps[chapter - 1].getElementsByTagName("v")
    # Get each verse
    hebrew_text = []
    for firstvs in range(lastvs):
        # Get the list of xml nodes for the verse
        verse = ""
        words = vss[firstvs].getElementsByTagName("w")
        for word in words:
            verse += word.firstChild.data + " "
            # f = open('output.txt', 'a', encoding="utf-8")
            # f.write(word.firstChild.data + " ")
        # f.write(f"\n")
        hebrew_text.append(verse)
    return hebrew_text

def search_entries(term):
    # load all entries
    with open('FileNames.json') as f:
        data = json.load(f)
    results = []
    # See if we get city hits, if so don't search for anything else
    for entry in data:
        if term.lower() in entry["City"].lower():
            results.append(entry)
    if len(results) > 0:
        return results
    # Now search for countries if city had no results
    for entry in data:
        if term.lower() in entry["Country"].lower():
            results.append(entry)
    if len(results) > 0:
        return results
    # If we couldn't find in country, let's find in book!
    for entry in data:
        if term.lower() in entry["Book"].lower():
            results.append(entry)
    if len(results) > 0:
        return results
    # Just in case, add functionality to search by HULTP
    for entry in data:
        if term == str(entry["HULTP"]):
            results.append(entry)
    return results
    
print(search_entries("SDFas"))