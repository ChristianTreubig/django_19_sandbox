from django.shortcuts import render, redirect, get_object_or_404
from my_sandbox_app.models import TriStatePlace, Resident
from my_sandbox_app.forms import ResidentForm
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy

def home(request):
    places = TriStatePlace.objects.all()
    old_guys = Resident.objects.filter(age__gt = 30)
    
    return render(request,
                  "my_sandbox_app/home.html",
                  {"places": places,
                   "old_guys": old_guys})

class PlaceCreate(CreateView):
    model = TriStatePlace
    template_name = "my_sandbox_app/place_create.html"
    fields = ["city", "state", "zip",]
    success_url = reverse_lazy("place_create_done")
    
def place_create_done(request):
    return render(request,
                  "my_sandbox_app/place_create_done.html")
    
def resident_create(request):
    if request.method == "POST":
        form = ResidentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("resident_create_done")
        return render(request,
                  "my_sandbox_app/resident_create.html",
                  {"form": form})
    form = ResidentForm()
    return render(request,
                  "my_sandbox_app/resident_create.html",
                  {"form": form})

def resident_create_done(request):
    return render(request,
                  "my_sandbox_app/resident_create_done.html")
    
def resident_update(request, resident_id):
    resident = get_object_or_404(Resident, id = resident_id)
    if request.method == "POST":
        form = ResidentForm(request.POST, instance = resident)
        if form.is_valid():
            form.save()
            return redirect("resident_create_done")
        return render(request,
                  "my_sandbox_app/resident_create.html",
                  {"form": form})
    form = ResidentForm(instance = resident)
    return render(request,
                  "my_sandbox_app/resident_create.html",
                  {"form": form})