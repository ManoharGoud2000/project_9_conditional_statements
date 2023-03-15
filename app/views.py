from django.shortcuts import render

# Create your views here.

def looping_statements(request):
    d={'Name':'Manohar Goud'}
    return render(request,'looping_statements.html',d)
