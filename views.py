from django.shortcuts import render, HttpResponse, redirect
import re
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string
import random, string, math



def index(request):

    return render(request,'amadon/index.html')

def process(request):
    if 'total' not in request.session:
        request.session['total']=0
    if 'count' not in request.session:
        request.session['count'] = 0

    if request.method == 'POST':
        value= int(request.POST['product_id'])

        quantity = int(request.POST['quantity'])
        request.session['cost'] = 0
        total = request.session['total']*1

        request.session['cost'] = value*quantity
        request.session['count'] +=1
        request.session['total'] += request.session['cost']
        print "count",request.session['count']

        # total += cost
        # request.session['cost'] = cost
        # request.session['total'] = total
        # request.session['count'] = count +1

        return render(request, 'amadon/checkout.html')
    print "error, process did not POST"
    return redirect('/')

def checkout(request):
    print "not in process"
    return render(request, 'amadon/checkout.html')
