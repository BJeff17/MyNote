from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from django.contrib.auth.models import AnonymousUser, User
from django.contrib.auth import login, authenticate, logout
from .models import Note, Categorie
from .serializers import NoteSerializer

# Create your views here.
#-----------------------------------------------------------------------
# with open('main/quote.txt', "r",encoding="utf8") as file:
#     quotes = list(file.read().split('\n'))
#-----------------------------------------------------------------------
# print(quotes[0])
def index(request):
    
    return render(request,"home.html")
def propos(request):
    return render(request,"propos.html")
def vnotes(request):
    print(request.user)
    if request.user == AnonymousUser():
        return redirect("login-page")
    notes = Note.objects.filter(user = request.user)
    have_notes = len(notes) != 0
    context = {
        "vos_notes":notes,
        "have_notes":have_notes,

    }
    return render(request, "notes.html",context)
def log_(request):
    if request.method == "POST":
        name = request.POST.get("username")
        password = request.POST.get("password")
        user =  authenticate(request, username=name, password = password)
        if user != AnonymousUser():
            login(request,user)
            return redirect("unotes")
    return render(request,"login.html" )
def sign_(request):
    if request.method == "POST":
        name = request.POST.get("username")
        mail = request.POST.get("email")
        password = request.POST.get("password")
        password_confirm = request.POST.get("password-confirm")
        if password == password_confirm:
            user = User.objects.create_user(username=name,email=mail,password=password)
            user.save()
            login(request, user)
            return redirect("unotes")
    return render(request, "signin.html")
def log_out(request):
    logout(request)
    return redirect("home")
def add_note(request):
    categories = Categorie.objects.filter()
    if request.method == "POST":
        title = request.POST.get("title")
        body = request.POST.get("content")

        categorie = request.POST.get("category")
        print(categorie)
        print("-------------------")
        if categorie == "autre":
            categorie = request.POST.get("newCategory")
            categorie = Categorie.objects.create(name= categorie)
            categorie.save()
        else:
            categorie = Categorie.objects.filter(name = categorie).first()
        note = Note.objects.create(title=title,body = body, user= request.user, categorie = categorie)
        note.save()
        return redirect("unotes")
    return render(request,"add-note.html", {"categories":categories})
def search(request):
    print(request)
    if request.user != AnonymousUser():
        title = request.POST.get("title")
        notes = Note.objects.filter(user = request.user, title = title)
        # serializer = NoteSerializer(notes, many=True)
        # return JsonResponse(serializer.data, safe=False)
        return render(request,'search.html',{"notes":notes,"have_notes":len(notes) !=0})
    else:
        
        return redirect("login-page")
def update_notes(request, slug):
    categories = Categorie.objects.all()
    note = Note.objects.filter(slug = slug, user=request.user).first()
    print(note)
    if request.method == "POST":
        note.body = request.POST.get("content")
        note.title = request.POST.get("title")
        categorie = request.POST.get("category")
        print(categorie)
        print("-------------------")
        if categorie == "autre":
            categorie = request.POST.get("newCategory")
            categorie = Categorie.objects.create(name= categorie)
            categorie.save()
        else:
            categorie = Categorie.objects.filter(name = categorie).first()
        note.categorie = categorie
        note.save()
        return redirect("unotes")
    return render(request,"update_notes.html",{
        "note":note,
        "categories":categories,
        })
    