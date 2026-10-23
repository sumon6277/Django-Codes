from django.shortcuts import render

def home(request):

    d = {'name' : 'Sumon Ahmed', 'age' : 23 ,'lst' : [1,2,3,4,5,6,7,8,9,10], 'courses':
     [
        {
            'id':1,
            'c_name':'Python',
            'fee' : 4000
        },
        {
            'id':1,
            'c_name':'Html',
            'fee' : 1000
        },
        {
            'id':1,
            'c_name':'Django',
            'fee' : 14000
        },
        {
            'id':1,
            'c_name':'DSA',
            'fee' : 1500
        },
        {
            'id':1,
            'c_name':'React',
            'fee' : 10000
        },
      ]
    }
    return render(request,'first_app/home.html',context=d)