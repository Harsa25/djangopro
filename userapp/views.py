from django.shortcuts import render,HttpResponse
from django.template import loder
from .models import UserDetails

# Create your views here.
def sayhello(request):
    return HttpResponse("DJANGO PROJECT IS CREATED AND WEB PAGE IS EXECUTED")

def html_page(request):
    return render(request, 'index.html')

    def members(request):
        myusers=UserDetails.all().values()
        template=loder.get_template('all_user.html')
        context={
            'myusers': myusers,
        }
        return HttpResponse(template.render(context,request))

    def details(request,id):
        myusers=UserDetails.object.get(id=id)
        template=loader.get_template('details.html')
        context={
            'myusers':myusers,
        }
        return HttpResponse(template.render(context,request))
