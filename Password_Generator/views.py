from django.shortcuts import render
from django.http import HttpResponse
# from django.template import render
# from . import templates
import random


# Create your views here.
def pass_generate(request):
    # Getting data from form
    length = request.GET.get('Length')
    uppercase = request.GET.get('uppercase')
    lowercase = request.GET.get('lowercase')
    specialcharacters = request.GET.get('specialcharacters')
    numbers = request.GET.get('numbers')
    
    
    #Generating Password
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
            
    # Sending data to sessions

    if 'last_15' in request.session: 
        if len(request.session['last_15']) > 14:
            request.session['last_15'].pop()
        if result:
            request.session['last_15'].insert(0,result)
    else:
        request.session['last_15'] = [result]
    # for i in  
    sessions_result = request.session['last_15']
    request.session.modified = True # We are telling django that every time the page reloads or this sessions code runs you should modify list inside your sessions everytime, django doesn't modify list and dictionnaries inside sessions on every reload that is why we have to tell django to modify lists,dicts inside sessions through this command


    
    # def fun():
    #     return (listtt[random.randint(0,25)] + listtt[random.randint(0,25)] + listt[random.randint(0,7)] + listtt[random.randint(0,25)])
    # print(fun() + str(random.randint(0,99)) + fun() + str(random.randint(1,99)) )
    # varr = fun() + str(random.randint(0,99)) + fun() + str(random.randint(1,99)) 
    
    return render(request, 'pass-generator.html', {'result': result, 'sessions_result': sessions_result})
    # return HttpResponse('<span>Salam</span><span>W.Salam</span>')
