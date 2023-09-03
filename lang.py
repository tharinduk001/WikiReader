from googletrans import Translator
import googletrans
import wiki
translator = Translator()
langs = googletrans.LANGUAGES

def translate(textin,searchresult):
    text1 = textin
    result = translator.translate(text=text1, dest="si", src="en").text
    return result,searchresult


def translator2(i,Text):
    output = translator.translate(text=Text , src= "en", dest=i).text
    return output
