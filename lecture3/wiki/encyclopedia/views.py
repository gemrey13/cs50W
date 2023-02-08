from django.shortcuts import render, redirect
from django.http import HttpResponse
import markdown2
from . import util



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
                "content": html
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




def editEntry(request, id_title):

    html_content = markdown2.markdown(util.get_edited_entry(id_title))
    if request.method == "POST":
        edited_entry = request.POST.get('edit_content')

        util.save_edited_entry(id_title, edited_entry)
        return redirect('entry', id_title)

    return render(request, "encyclopedia/edit.html", {
       "content": html_content,
    })

