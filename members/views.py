#from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Members

def members(request):
  mymembers = Members.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request)) 

  #creer une nouvelle vue de la page detaille 

def details(request, id):
  mymember = Members.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))


#creer une nouvelle vue de la page Main

def main (request):
  template = loader .get_template('main.html')
  return HttpResponse(template.render()) 


  # ajouter une vue de test sur notre projet 
def testing(request):
  template = loader.get_template('template.html')
  context = {
    #'fruits':['Pomme','Banane','cerise','kiwi'],
    #'firstname' : 'Maoulida hafidhou'
    'member' : mymembers,
  }
  return HttpResponse(template.render(context, request))





# return HttpResponse("Bonjour tout le monde ! ")

 #  template = loader.get_template('myfirst.html')
 #  return HttpResponse(template.render())




