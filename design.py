#This is a test line

from tkinter import *
import ttkbootstrap as tb
import lang
import wiki

root = tb.Window(themename="darkly")
root.geometry("472x550")
root.resizable(False, False)
root.title("Wikipedia data reader")


def langChanger(i):
    try:
        result = lang.translator2(i, datas)
        textout.delete(1.0, END)
        textout.insert(tb.INSERT, result)
    except Exception as e:
        textout.delete(1.0, END)
        textout.insert(tb.INSERT, f"Error ! {e}")


def translator(textin, searchResults):
    try:
        finalresult, searchResult = lang.translate(textin, searchResults)
        textout.delete(1.0, END)
        textout.insert(tb.INSERT, finalresult)
        textoutOfSearchResult.delete(1.0, END)
        textoutOfSearchResult.insert(tb.INSERT, searchResult)
    except Exception as e:
        textout.delete(1.0, END)
        textout.insert(tb.INSERT, f"Error ! {e}")


def searchWiki(inputval):
    try:
        data, searchResults = wiki.getData(inputval)
        global datas
        datas = data
        translator(data, searchResults)
    except Exception as e:
        textout.delete(1.0, END)
        textout.insert(tb.INSERT, f"Error ! {e}")


title = tb.Label(root, text="Wikipedia Search Engine", font=(
    "calbri 20 bold"), bootstyle="primary inverse")
title.grid(row=0, column=0)

# TODO: This is the first frame so consider that
myframe = tb.Frame(root, padding=4)
myframe.grid(row=2, column=0, sticky=NSEW, pady=10)

textout = tb.Text(myframe, width=60, height=15, font=("Helvetica 10"))
textout.grid(row=0, column=0, columnspan=2, rowspan=6, padx=10, pady=5)

textout.delete(1.0, END)
textout.insert(
    tb.INSERT, f"{'-'*25} The search result will be shown here {'-'*25}")

scrollbar = tb.Scrollbar(myframe, command=textout.yview, bootstyle="success")
textout['yscroll'] = scrollbar.set
scrollbar.grid(row=0, column=2, rowspan=6, sticky=NS)


# TODO
LangFrame = tb.Frame(root, padding=4)
LangFrame.grid(row=3, column=0, sticky=NSEW, pady=5, padx=5)

langLabel = tb.Label(
    LangFrame, text="Select Preffered Language (Defualt -Sinhala) : ", font="arial 10 bold italic")
langLabel.grid(row=0, column=0, padx=16)


my_menu = tb.Menubutton(
    master=LangFrame, bootstyle="info", text="Language", width=10)
my_menu.grid(row=0, column=1, padx=10)

themelist = tb.Menu(my_menu)

item_var = tb.StringVar()
for i in lang.langs:
    themelist.add_radiobutton(
        label=i, variable=item_var, command=lambda i=i: langChanger(i))

my_menu['menu'] = themelist


# TODO: This is the third frame so consider that
searchresultsframe = tb.Frame(root, padding=4)
searchresultsframe.grid(row=4, column=0, sticky=NSEW, pady=5, padx=5)

textoutOfSearchResult = tb.Text(
    searchresultsframe, width=60, height=5, font=("Helvetica 9 italic"))
textoutOfSearchResult.grid(
    row=0, column=0, columnspan=2, rowspan=6, padx=5, pady=5)

textoutOfSearchResult.delete(1.0, END)
textoutOfSearchResult.insert(
    tb.INSERT, "More Suggested Keywords for your search will be appear here.")


# TODO: This is the second frame so consider that
searchframe = tb.Frame(root, padding=4)
searchframe.grid(row=5, column=0, sticky=NSEW, pady=10)

datain = tb.Entry(searchframe, width=50,)
datain.grid(row=0, column=0, padx=5)

searchbtn = tb.Button(searchframe, text="Search...", bootstyle="outlined warning",
                      width=15, command=lambda: searchWiki(datain.get()))
searchbtn.grid(row=0, column=2, padx=4)


root.mainloop()
