from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from user.forms import NewUser
# Create your views here.


def home(request):
    return render(request, 'user/index.html')

# def register(request):
#     if request.method == "GET":
#         return render(request, "user/register.html",{"form": NewUser})
#     elif request.method == "POST":
#         form = NewUser(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return render(request,'user/index.html')
#             # return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        form = NewUser(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
        return redirect("/")
    form = NewUser()
    return render(request, "user/register.html", {"form":form})