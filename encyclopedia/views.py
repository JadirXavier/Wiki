from django.shortcuts import render
from django.shortcuts import redirect
from markdown2 import Markdown
import random

from . import util


def markdown_to_html(entry):
    content = util.get_entry(entry)
    markdowner = Markdown()
    if content == None:
        return None
    else:
        return markdowner.convert(content)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry_page(request, page):
    html = markdown_to_html(page)
    if html == None:
        return render(request, "encyclopedia/error.html",{
            "title": "Error",
            "msg":"This page does not exist."
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "title": page,
            "content": html
        })
    
def search_page(request):
    query = request.GET.get('q', '').lower()
    search_results = []
    for entry in util.list_entries():
        if  query in entry.lower():
            search_results.append(entry)

    match = None
    for entry in search_results:
        if entry.lower() == query:
            match = entry
            break

    if match:
        return redirect("page", page=match)
        
    else:
        return render(request, "encyclopedia/search.html", {
            "entries" : search_results
        })
    
def new_page(request):
    if request.method == "POST":
        title = request.POST.get("new_page_title")
        description = request.POST.get("new_page_description")
        content = f"#{title}\n\n{description}"
        entries = util.list_entries()
        if title in entries:
            return render(request, "encyclopedia/error.html",{
                "title": "Error",
                "msg":"This page already exists"
            })
        else:
            util.save_entry(title, content)
            return redirect("page", page=title)
    return render(request, 'encyclopedia/new_page.html')

def edit_page(request, page):
    description = '\n'.join(util.get_entry(page).split('\n')[2:])
    print(description)
    if request.method == "POST":
        description = request.POST.get("edit_page_description")
        content = f"#{page}\n\n{description}"
        util.save_entry(page, content)
        return redirect("page", page=page)
    return render(request, "encyclopedia/edit_page.html",{
        "edit_page_description" : description,
        "edit_page_title": page
    })

def random_page(request):
    entries = util.list_entries()
    random_page = random.choice(entries)
    return redirect("page", page=random_page)