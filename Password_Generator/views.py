from django.shortcuts import render
from django.http import HttpResponse
# from django.template import render
# from . import templates
import random


# Create your views here.
def pass_generate(request):
    length = request.GET.get('Length')
    uppercase = request.GET.get('uppercase')
    lowercase = request.GET.get('lowercase')
    specialcharacters = request.GET.get('specialcharacters')
    numbers = request.GET.get('numbers')
    
    listt = ['-','_','*','$','@','!','#','%']
    listtt = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    def upperCase():
        return (listtt[random.randint(0,25)].upper())
    def lowerCase():
        return (listtt[random.randint(0,25)])
    def numbeR():
        return (random.randint(0,9))
    def specialCharacters():
        return listt[random.randint(0,7)]
    
    result = ''
    add = 1
    if length:
        for i in range(int(length)):
            if uppercase and add <= int(length):
                result += upperCase()
                add = add + 1
            if lowercase and add <= int(length):
                result += lowerCase()
                add = add + 1
            if specialcharacters and add <= int(length):
                result += specialCharacters()  
                add = add + 1
            if numbers and add <= int(length):
                result += str(numbeR())
                add = add + 1

    
    # def fun():
    #     return (listtt[random.randint(0,25)] + listtt[random.randint(0,25)] + listt[random.randint(0,7)] + listtt[random.randint(0,25)])
    
    
    # print(fun() + str(random.randint(0,99)) + fun() + str(random.randint(1,99)) )
    # varr = fun() + str(random.randint(0,99)) + fun() + str(random.randint(1,99)) 
    
    return render(request, 'pass-generator.html', {'result': result})
    # return HttpResponse('<span>Salam</span><span>W.Salam</span>')
