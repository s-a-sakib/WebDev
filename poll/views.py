from django.shortcuts import render

def indexes(request):
    peoples = [
        {'name': 'Sakib' , 'Age' : '18'},
        {'name': 'Ahedul' , 'Age' : '17'},
        {'name': 'Kabya' , 'Age' : '16'},
        {'name': 'Apurbo' , 'Age' : '28'},
        {'name': 'Aziz' , 'Age' : '22'}
    ]
    
    return render(request,'index.html', context = {'peoples' : peoples})
