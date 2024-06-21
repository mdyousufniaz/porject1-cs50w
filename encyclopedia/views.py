from django.shortcuts import render, redirect

from markdown2 import markdown

from . import util


def index(request):
    if request.method == "POST":
        title = request.POST['q']
        if title in util.list_entries():
            print(title)
            return redirect('entry', title=title)
        else:
            return render(request, "encyclopedia/search.html", {
                "title": title,
                "search_results": util.simillar_entries(title)
            })
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    content = util.get_entry(title)
    if content is not None:
        content = markdown(content)
    print(content)
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": content
    })

