import wikipedia

def getData(inputval:str)->str:
    try:
        page = wikipedia.page(inputval)
        output_result = page.summary
        searchResults = wikipedia.search(inputval)
        return output_result, searchResults
    except Exception as e:
        return "Error : Please try another keyword or Check your spellings are correct." , e


   

