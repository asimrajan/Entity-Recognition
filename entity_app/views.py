from django.shortcuts import render
from .forms import InputForm
from entity_app.entity_extractor import enty


def home(request):
    result = None
    #form = InputForm(request.GET or None)
    if request.method=='POST':
    	form = InputForm(request.POST)
    	if form.is_valid():
    		data = form.cleaned_data['sentence']
    		print(data)
    		result = enty(data)
    	return render(request,"results.html",{'result':result})
    else:
    	form = InputForm()
    	return render(request, "home.html", {'form': form})