from django.shortcuts import render, redirect
from django.http import HttpResponse
import markdown2
from . import util
import random


# Will display all the list of entries in wiki
def index(request):

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


"""
 This function will get the form with name of q and get the entry(util.get_entry()) based on the q
 This function will render in encyclopedia/entry.html template
"""
def search(request):
    try:
        query = request.GET.get('q')
        if query:
            result = util.get_entry(query)
            html = markdown2.markdown(result)

            return render(request, "encyclopedia/entry.html", {
                "content": html,
                "title": query
            })

# if the search is not accurate it will get the substring of the name="q" and render it in "encyclopedia/searched.html"
    except TypeError:
        query = request.GET.get('q')
        entries = util.list_entries()
        entries = [entry for entry in entries if query.lower() in entry.lower()]

        return render(request, "encyclopedia/searched.html", {
            "entries": entries
        })


"""
The title will be provided in urls.py in path("wiki/<str:title>")
markdown2.markdown() will convert the markdown or md to html file
"""
def entry(request, title):
    text = util.get_entry(title)
    html = markdown2.markdown(text)

    return render(request, "encyclopedia/entry.html", {
        "content": html,
        "title": title
    })




def newpage(request):

    try:
        if request.method == "POST":
            title = request.POST.get('title')
            content = request.POST.get('content')
            util.save_entry(title, content)
            return redirect('entry', title)

    except ValueError:
        return render(request, "encyclopedia/valueError.html", {})

    return render(request, 'encyclopedia/newpage.html', {})




def editEntry(request,title):
    if request.method == "POST":
       content = request.POST.get('content')
       util.save_edit_entry(title, content)
       return redirect("entry", title)
    
    content = util.get_edit_entry(title)
    return render(request, 'encyclopedia/edit.html', {
        "content": content
    })


def randomEntry(request):
    
    entries = util.list_entries()
    random_int = random.randint(0, len(entries)-1)

    entry = entries[random_int]
    text = util.get_entry(entry)
    html = markdown2.markdown(text)
    return render(request, 'encyclopedia/entry.html', {
        "content": html,
        "title": entry
    })
    