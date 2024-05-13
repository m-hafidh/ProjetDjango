#from django.shortcuts import render
from django.http import HttpResponse #,HttpResponseRedirect
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
    'fruits':['Pomme','Banane','cerise','kiwi'],
    
    #'firstname' : 'Maoulida hafidhou'
    #'members' : mymembers,
  }
  return HttpResponse(template.render(context, request))

#creer une nouvelle vue de la page Ytest

def mytest (request):
  mymembers = Members.objects.all().values()
  template = loader .get_template('mytest.html')
  context = {
    'members': mymembers,
  }
  return HttpResponse(template.render(context, request)) 
    # 'fruits': ['Apple', 'Banana', 'Cherry'], 
    #'greeting' == 1,
   # 'x': ['Apple', 'Banana', 'Cherry'],   
   # 'y': ['Apple', 'Banana', 'Cherry'],

  
  
  
 

  
  # ajouter une vue de test sur notre page bouclee 

def voiture(request):
  template = loader.get_template('voiture.html')
  context = {
    'cars': [
      {
        'brand': 'Ford',
        'model': 'Mustang',
        'year': '1964',
      },
      {
        'brand': 'Ford',
        'model': 'Bronco',
        'year': '1970',
      },
      {
        'brand': 'Volvo',
        'model': 'P1800',
        'year': '1964',
      }]
    }
  return HttpResponse(template.render(context, request))  
 
# ajouter une vue de test sur notre page accueil 

def Home(request):
  template = loader.get_template('Home.html')
  return HttpResponse(template.render())


# return HttpResponse("Bonjour tout le monde ! ")

 #  template = loader.get_template('myfirst.html')
 #  return HttpResponse(template.render())

 # ajouter une vue de test sur notre page Test 

def Montest(request):
 # mydata = Members.objects.all() # la methode All() renvoie tous les Enregistrements 
  #mydata = Members.objects.values_list('firstname') # la methode values.list() renvoie des colones specifique 
 # mydata = Members.objects.filter(firstname='Maoulida').values() # la methode filter() renvoie uniquement de ligne ou enregistremnt specifique
 #mydata = Member.objects.filter(lastname='Bezos', id=8).values()
 #onpeut aussi utiliser le ou "|" pour renvoyer plusieurs enregitrement 
 #mydata = Member.objects.filter(firstname='Hadjara').values() | Member.objects.filter(firstname='Taslima').values()
 #Renvoyez les enregistrements où firstnamecommence par la lettre « L » : en utilisant le mot clé __startswithmot:
 #mydata = Member.objects.filter(firstname__startswith='M').values()

 #Classez le résultat par ordre alphabétique du prénom  en utilisant  la méthode "order_by()":
  mydata = Members.objects.all().order_by('firstname').values() # Croissant
  #mydata = Members.objects.all().order_by('-firstname').values() #Decroissant
 
  template = loader.get_template("Test.html")
  context = {
    'mymembers' : mydata,
  }
  return HttpResponse(template.render(context, request))


  


 



