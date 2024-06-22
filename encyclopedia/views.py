from django.shortcuts import render, redirect

from markdown2 import markdown

from . import util

from random import choice


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

def random_entry(request):
    random_title = choice(util.list_entries())
    return redirect('entry', title=random_title)

def format_page(request):
    if request.method == "GET":
        if request.GET["id"] == "new":
            message = "Create a New"
            form = util.EntryForm()
        else:
            message = "Update Existing"
            title = request.GET["id"]
            form = util.EntryForm(title=title, content=util.get_entry(title))
        return render(request, "encyclopedia/format_page.html", {
            "heading": message,
            "form": form
        })

    else:
        form = util.EntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            print(title, content)
            util.save_entry(title, content)
            return redirect('entry', title=form.cleaned_data['title'])
        else:
            return render(request, "encyclopedia/format_page.html", {
            "heading": message,
            "form": form
        })







