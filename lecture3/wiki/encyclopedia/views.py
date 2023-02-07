from django.shortcuts import render
from django.http import HttpResponse
import markdown2
from . import util


def index(request):

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def search(request):
    query = request.GET.get('q')
    if query:
        result = util.get_entry(query)
        html = markdown2.markdown(result)
        return render(request, "encyclopedia/entry.html", {
            "content": html
        })
    

def entry(request, title):
    text = util.get_entry(title)
    html = markdown2.markdown(text)
    return render(request, "encyclopedia/entry.html", {
        "content": html
    })

