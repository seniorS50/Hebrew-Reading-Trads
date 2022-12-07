import json
from xml.dom import minidom

def get_jps(book, chapter, firstvs = 0, lastvs = 0):
    # Get info from the index
    doc = minidom.parse("Books\engjps_vpl.xml")
    index = doc.getElementsByTagName("v")
    text = []
    for verse in index:
        if verse.hasAttribute("b") and verse.getAttribute("b") == book \
                and int(verse.getAttribute("c")) == chapter \
                and int(verse.getAttribute("v")) >= firstvs \
                and int(verse.getAttribute("v")) <= lastvs:
            text.append({ "vs": int(verse.getAttribute("v")), "text": verse.firstChild.data})
    return text

def book_to_abbr(book_name):
    match book_name:
        case 'Genesis': return ( 'GEN')
        case 'Exodus': return ( 'EXO')
        case 'Leviticus': return ( 'LEV')
        case 'Numbers': return ( 'NUM')
        case 'Deuteronomy': return ( 'DEU')
        case 'Joshua': return ( 'JOS')
        case 'Judges': return ( 'JDG')
        case 'Ruth': return ( 'RUT')
        case '1 Samuel': return ( '1SA')
        case '2 Samuel': return ( '2SA')
        case '1 Kings': return ( '1KI')
        case '2 Kings': return ( '2KI')
        case '1 Chronicles': return ( '1CH')
        case '2 Chronicles': return ( '2CH')
        case 'Ezra': return ( 'EZR')
        case 'Nehemiah': return ( 'NEH')
        case 'Esther': return ( 'EST')
        case 'Job': return ( 'JOB')
        case 'Psalms': return ( 'PSA')
        case 'Proverbs': return ( 'PRO')
        case 'Ecclesiastes': return ( 'ECC')
        case 'Song of Songs': return ( 'SNG')
        case 'Isaiah': return ( 'ISA')
        case 'Jeremiah': return ( 'JER')
        case 'Lamentations': return ( 'LAM')
        case 'Ezekiel': return ( 'EZK')
        case 'Daniel': return ( 'DAN')
        case 'Hosea': return ( 'HOS')
        case 'Joel': return ( 'JOL')
        case 'Amos': return ( 'AMO')
        case 'Obadiah': return ( 'OBA')
        case 'Jonah': return ( 'JON')
        case 'Micah': return ( 'MIC')
        case 'Nahum': return ( 'NAM')
        case 'Habakkuk': return ( 'HAB')
        case 'Zepheniah': return ( 'ZEP')
        case 'Haggai': return ( 'HAG')
        case 'Zecheriah': return ( 'ZEC')
        case 'Malachi': return ( 'MAL')
    return("Error")

print(book_to_abbr("Malachi"))