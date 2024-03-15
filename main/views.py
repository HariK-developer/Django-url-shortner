from django.shortcuts import render
from django.contrib import messages
import pyshorteners




def short_url(request):
    short_url = ""
    url = ""
    if request.method == "POST":
        shortner = pyshorteners.Shortener()
        url = request.POST.get("url")
        short_url = shortner.tinyurl.short(url)
        messages.success(request, "Generated")
    context = {"short_url": short_url, "url": url}
    return render(request,'index.html',context)