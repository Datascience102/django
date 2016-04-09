from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpRequest  # optional import
from .models import Watch
from django.db.models import Count, Max,Avg
from django.contrib import messages
from forms import WatchForm

# created a view for store-index page

def index(request):
    return render(request,"index.html")

# creating a view for dukaan

# create a view for stock and populate the stuff from models.py

def stock(request):
    count = Watch.objects.all().count()
    count_alt = Watch.objects.count()
    total_count = Watch.objects.all()
    count_of_all = Watch.objects.all()
    #fossil_total = Watch.objects.filter(Watch__company="Fossil").count() # total of Fossil only
    # Combining multiple aggregations
    q = Watch.objects.annotate(Count('stock')) # this returned a list full of values like it did for

    context = {
        'count': count,
        'totalcount' : total_count,
        'allwatchcount': total_count,

        'title' : "this is stock views page",
        'description' : "the stock which is available is as follows",
        #'listobject': names
        'Fossil' : total_count[0],
        'second' : total_count[1],
        'third' : total_count[2],
        'fourth' : total_count[3],
        'allcount' : q,
    }
    return render(request, 'stock.html',context)

# View for dukaanam

def dukaanam(request):
    return render(request, "dukaan.html")

def newwatch(request):
    form = WatchForm(request.Post or None,request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request,"Created New Watch Successfully")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {"form":form,}
    return render(request,"watch_post.html",context)	



	
	
# def newwatch(request):
    # form=WatchForm(request.Post or None,request.FILES or None)
	
	# if form.is_valid(): 
	    # instance = form.save(commit=False)
		# instance.save()
		# # write form submission success
		# messages.success(request,"Created New Watch Successfully")
		# return HttpResponseRedirect(instance.get_absolute_url())
	# context = { "form":form,}
	# return render(request,"watch_post.html",context)
	
# def newwatch(request):
    # form=WatchForm(request.Post or None,request.FILES or None)
	# if form.is_valid():instance = form.save(commit=False);
		# instance.save();
		# # write form submission success
		# messages.success(request,"Created New Watch Successfully");
		# return HttpResponseRedirect(instance.get_absolute_url());
	# context = { "form":form,};
	# return render(request,"watch_post.html",context)	
	
	
		


def registration(request): return render(request)



