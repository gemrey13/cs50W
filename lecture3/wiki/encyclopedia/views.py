from django.shortcuts import render
import markdown2
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, title):
    text = util.get_entry(title)
    html = markdown2.markdown(text)


    return render(request, "encyclopedia/entry.html", {
        "content": html
    })


def search(request):
    query = request.GET.get('q')
    
    result = util.get_entry(query)
    html = markdown2.markdown(result)

    return render(request, "encyclopedia/entry.html", {
        "content": html
    })