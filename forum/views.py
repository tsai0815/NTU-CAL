from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# def forum(request):
#     template = loader.get_template('index.html')
#     return HttpResponse(template.render())

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def topics_listing(request):
    template = loader.get_template('topics-listing.html')
    return HttpResponse(template.render())

def topics_detail(request):
    template = loader.get_template('topics-detail.html')
    return HttpResponse(template.render())

def buy_coffee(request):
    template = loader.get_template('buy-coffee.html')
    return HttpResponse(template.render())

def aboutus(request):
    template = loader.get_template('aboutus.html')
    return HttpResponse(template.render())