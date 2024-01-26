from django.shortcuts import render
import markdown2

from . import util


def index(request):
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
    


