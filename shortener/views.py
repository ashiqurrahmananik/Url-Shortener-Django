from django.shortcuts import render, redirect
from .models import url
from django.http import HttpResponse
from hashlib import md5
# Create your views here.
def index(request):
    return render (request,'index.html')

def create(request):
    if request.method == 'POST':
        print(request)
        url1 = request.POST.get('link1','')
        uid = md5(url1.encode()).hexdigest()[:5]
        u=str(uid)
        print(url1, uid, u)
        new_url = url(link=url1, uuid=u)
        new_url.save()
        params={'shorturl':u,'longurl':url1}
        return render(request, 'index.html', params)
def go(request, pk):
    url_details=url.objects.get(uuid=pk)
    return redirect(url_details.link)
