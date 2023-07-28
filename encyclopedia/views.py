import random

from django.shortcuts import render
from markdown2 import Markdown

from . import util

def mdtohtml(title):
    text = util.get_entry(title)
    markdowner = Markdown()
    if text == None:
        return None
    else:      
        return markdowner.convert(text)


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, title):
    html_page = mdtohtml(title)
    if html_page == None:
        return render(request, "encyclopedia/error_sms.html", {
            "display_error_message": "Requested page not found."
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": html_page
        })
    

def search(request):
    if request.method == "POST":
        busquedas = request.POST['q']
        searchs = mdtohtml(busquedas)
        if searchs is not None:
            return render(request, "encyclopedia/entry.html", {
                "title": busquedas,
                "content": searchs
            })
        else: 
            everyEntry = util.list_entries()
            possibilities = []
            for entry in everyEntry:
                if busquedas.lower() in entry.lower():
                    possibilities.append(entry)
            return render(request, "encyclopedia/possibilities.html", {
                "possibilities": possibilities
            })


def newpage(request):
    if request.method == "GET":
        return render(request, "encyclopedia/newpage.html")
    else:
        title = request.POST['title_newpage']
        content = request.POST['content']

        # if title already exists
        title_exists = util.get_entry(title)
        if title_exists is not None:
            return render(request, "encyclopedia/error_sms.html", {
                "display_error_message": "Title already exists. Try another one."
            })
        # if title does not exist
        else:
            util.save_entry(title, content)
            newpage_content = mdtohtml(title)
            return render(request, "encyclopedia/entry.html", {
                "title": title,
                "content": newpage_content
            })


def editpage(request):
    if request.method == "POST":
        title = request.POST['entry_title']
        content = util.get_entry(title)
        return render(request, "encyclopedia/editpage.html", {
            "title": title,
            "content": content
        })
    

def edited(request):
    if request.method == "POST":
        title = request.POST['title_newpage']
        content = request.POST['content']

        # save the new content 
        util.save_entry(title, content)
        newpage_content = mdtohtml(title)
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": newpage_content
        })
    

def random_function(request):
    # get all entries that exist
    everyEntry = util.list_entries()
    # use random function
    chosen_entry = random.choice(everyEntry)
    # convert it to markdown 
    converted_content = mdtohtml(chosen_entry)
    return render(request, "encyclopedia/entry.html", {
        "title": chosen_entry,
        "content": converted_content
    })


            


