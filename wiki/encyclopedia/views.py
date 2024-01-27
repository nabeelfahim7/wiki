from django.shortcuts import render
import markdown2
from django import forms
from django.http import HttpResponse


from . import util



def index(request):
    if request.method == "POST":
        sub_list = []
        query = request.POST.get('q')
        for entry in util.list_entries():
            if query.upper() in entry.upper():
                sub_list.append(entry)
            if entry.upper() == str(query).upper():
                return page_render(request, entry)
        # create a new list that includes substrings 
        return render(request, "encyclopedia/search.html", {
        "entries": sub_list, "query" : query
    })
        
        
            
        




    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def page_render(request, TITLE):
    md_content = util.get_entry(TITLE)
    if md_content is None:
        return render(request, "encyclopedia/error.html")
    html_content = markdown2.markdown(md_content)
    return render(request, "encyclopedia/content.html" , {
        "html_content" : html_content, "TITLE" : TITLE
    })
    


