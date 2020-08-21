from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'base.html')
def new(request):
	search=request.POST.get('search')
	context={'search':search}
	return render (request,'new/new_search.html',context)