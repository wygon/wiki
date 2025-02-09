from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

from . import util
from .forms import NewPageForm#, SearchBarForm
import random

def index(request):
    entries = util.list_entries()
    if request.method == "POST":
        entriesToDelete = request.POST.getlist('entriesToDelete')

        for entry in entriesToDelete:
            util.delete_entry(entry)
        
        return redirect('index')
    return render(request, "encyclopedia/index.html", {
        "entries": entries
    })
def search(request):
    query = request.GET.get('query', '').strip()
    results = util.simmilarList(query.capitalize())
    if results == query.capitalize():
        return render(request,"encyclopedia/page.html", {
        "title" : query,
        "content" : util.get_entry(query)
    })
    else:
        return render(request, "encyclopedia/search.html",{        
            "query" : query,
            "results" : results
        })
def page(request, title):
    return render(request,"encyclopedia/page.html", {
        "title" : title,
        "content" : util.markItDown(util.get_entry(title))
    })

def newPage(request):
    if request.method == "POST":
        form = NewPageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            util.ifExist(title)
            util.save_entry(title.capitalize(), content)
            return redirect(f"/{title}", title=title)
    else:
        form = NewPageForm()
        
    return render(request, "encyclopedia/newPage.html",{
        "form" : form
    })

def editPage(request, title):
    content = util.get_entry(title)

    if request.method == "POST":
        editForm = NewPageForm(request.POST)
        if editForm.is_valid():
            new_title = editForm.cleaned_data["title"]
            new_content = editForm.cleaned_data["content"]
            util.save_entry(new_title.capitalize(), new_content)
            return redirect(f"/{new_title}")
    else:
        editForm = NewPageForm(initial={"title": title, "content": content})

    return render(request, "encyclopedia/editPage.html", {
        "editForm": editForm
    })

def randomPage(request):
    randomPage = random.choice(util.list_entries())
    print(randomPage)
    return page(request, randomPage)