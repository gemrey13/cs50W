from django.shortcuts import render
from django.http import HttpResponse
import markdown2
from . import util




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
                "content": html
            })
    except TypeError:
        query = request.GET.get('q')
        entries = util.list_entries()
        entries = [entry for entry in entries if query.lower() in entry.lower()]
        return render(request, "encyclopedia/searched.html", {
            "entries": entries
        })




def entry(request, title):
    text = util.get_entry(title)
    html = markdown2.markdown(text)

    return render(request, "encyclopedia/entry.html", {
        "content": html
    })

