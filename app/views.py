from django.shortcuts import render

# Create your views here.

def condition(request):
    d={'A':40, 'B':50, 'C':80}
    return render(request,'condition.html',d)
