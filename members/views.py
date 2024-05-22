from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

'''
views is where we define data y to be displayed on page x
'''
def members(request):
	mymembers = Member.objects.all().values()
	template = loader.get_template('all_members.html')
    #this is how we pull data from a model to display 
	context = {
		'mymembers': mymembers,
	}
	return HttpResponse(template.render(context, request))


def details(request, id):
	mymember = Member.objects.get(id=id)
	template = loader.get_template('details.html')
	context = {
		'mymember': mymember,
	}
	return HttpResponse(template.render(context, request))


def main(request):
	template = loader.get_template('main.html')
	return HttpResponse(template.render())


#for testing
def testing(request):
    '''
    This return specific columns
    mydata = Member.objects.values_list('firstname')
    
    This return specific rows
    mydata = Member.objects.filter(firstname='Bianca').values()

    This Return records where lastname is "Refsnes" and id is 2
    mydata = Member.objects.filter(lastname='Refsnes', id=2).values()

    This Return records where firstname is either "Emil" or Tobias"
    mydata = Member.objects.filter(firstname='Emil').values() | Member.objects.filter(firstname='Tobias').values()
    '''
    mydata = Member.objects.all()
    template = loader.get_template('template.html')
    context = {'mymembers': mydata,}
    return HttpResponse(template.render(context, request))
