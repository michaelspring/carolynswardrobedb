from django.shortcuts import render
import requests
from django.template.defaulttags import register
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import requests
import urllib3



# Create your views here.
def search(request):
    context = locals()
    template = 'search.html'
    return render(request,template,context)

def tidy(request):
    context = locals()
    template = 'tidy.html'
    return render(request,template,context)

def results(request):
    context = locals()
    template = 'results.html'
    return render(request,template,context)

def qthis1(request):
    data = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    print(data.text)
    data = data.text
    return render(request, 'results.html', {'data' : data})

def qthis2(request):
    from google.cloud import firestore
    import firebase_admin
    from firebase_admin import credentials
    from firebase_admin import db
    import requests
    import urllib3
    import os
    from firebase_admin import firestore
    import enum
    import pytz

    if (not len(firebase_admin._apps)):
        cred = credentials.Certificate('weatherwear-a4626-firebase-adminsdk-0nxej-aba5711d50.json')
        firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://weatherwear-a4626.firebaseio.com/'
        })

    data = db.collection('wardrobe').where(u'temperature', u'==', u'23')
    return render(request, 'search.html', {'data' : sorted(data.iteritems())})

def q_weekendBrunch(request):
    import firebase_admin
    from firebase_admin import credentials
    from firebase_admin import db
    import requests
    import urllib3

    if (not len(firebase_admin._apps)):
        cred = credentials.Certificate('weatherwear-a4626-firebase-adminsdk-0nxej-aba5711d50.json')
        firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://weatherwear-a4626.firebaseio.com/'
        })

    ref = db.reference('weather_db')
    data = ref.order_by_child('weekendBrunch').equal_to(1).get()
    return render(request, 'search.html', {'data' : sorted(data.iteritems())})


def q_summerVibes(request):
    import firebase_admin
    from firebase_admin import credentials
    from firebase_admin import db
    import requests
    import urllib3

    if (not len(firebase_admin._apps)):
        cred = credentials.Certificate('weatherwear-a4626-firebase-adminsdk-0nxej-aba5711d50.json') #in pythonanywhere this must be a direct link i.e. /home/michaelspring/myapp/src/file.json
        firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://weatherwear-a4626.firebaseio.com/'
        })

    ref = db.reference('weather_db')
    data = ref.order_by_child('summerVibes').equal_to(1).get()
    return render(request, 'search.html', {'data' : sorted(data.iteritems())})

def q_professional(request):
    import firebase_admin
    from firebase_admin import credentials
    from firebase_admin import db
    import requests
    import urllib3

    if (not len(firebase_admin._apps)):
        cred = credentials.Certificate('weatherwear-a4626-firebase-adminsdk-0nxej-aba5711d50.json')
        firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://weatherwear-a4626.firebaseio.com/'
        })

    ref = db.reference('weather_db')
    data = ref.order_by_child('professional').equal_to(1).get()
    return render(request, 'search.html', {'data' : sorted(data.iteritems())})

def q_partyTime(request):
    import firebase_admin
    from firebase_admin import credentials
    from firebase_admin import db
    import requests
    import urllib3

    if (not len(firebase_admin._apps)):
        cred = credentials.Certificate('weatherwear-a4626-firebase-adminsdk-0nxej-aba5711d50.json')
        firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://weatherwear-a4626.firebaseio.com/'
        })

    ref = db.reference('weather_db')
    data = ref.order_by_child('partyTime').equal_to(1).get()
    return render(request, 'search.html', {'data' : sorted(data.iteritems())})

def q_enVacances(request):
    import firebase_admin
    from firebase_admin import credentials
    from firebase_admin import db
    import requests
    import urllib3

    if (not len(firebase_admin._apps)):
        cred = credentials.Certificate('weatherwear-a4626-firebase-adminsdk-0nxej-aba5711d50.json')
        firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://weatherwear-a4626.firebaseio.com/'
        })

    ref = db.reference('weather_db')
    data = ref.order_by_child('enVacances').equal_to(1).get()
    return render(request, 'search.html', {'data' : sorted(data.iteritems())})

def q_active(request):
    import firebase_admin
    from firebase_admin import credentials
    from firebase_admin import db
    import requests
    import urllib3

    if (not len(firebase_admin._apps)):
        cred = credentials.Certificate('weatherwear-a4626-firebase-adminsdk-0nxej-aba5711d50.json')
        firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://weatherwear-a4626.firebaseio.com/'
        })

    ref = db.reference('weather_db')
    data = ref.order_by_child('active').equal_to(1).get()
    return render(request, 'search.html', {'data' : sorted(data.iteritems())})

def q_feelingFresh(request):
    import firebase_admin
    from firebase_admin import credentials
    from firebase_admin import db
    import requests
    import urllib3

    if (not len(firebase_admin._apps)):
        cred = credentials.Certificate('weatherwear-a4626-firebase-adminsdk-0nxej-aba5711d50.json')
        firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://weatherwear-a4626.firebaseio.com/'
        })

    ref = db.reference('weather_db')
    data = ref.order_by_child('feelingFresh').equal_to(1).get()
    return render(request, 'search.html', {'data' : sorted(data.iteritems())})

def q_inbetween(request):
    import firebase_admin
    from firebase_admin import credentials
    from firebase_admin import db
    import requests
    import urllib3

    if (not len(firebase_admin._apps)):
        cred = credentials.Certificate('weatherwear-a4626-firebase-adminsdk-0nxej-aba5711d50.json')
        firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://weatherwear-a4626.firebaseio.com/'
        })

    ref = db.reference('weather_db')
    data = ref.order_by_child('inbetween').equal_to(1).get()
    return render(request, 'search.html', {'data' : sorted(data.iteritems())})

#all queiry commands
#https://firebase.google.com/docs/database/admin/retrieve-data

#from django.template.defaulttags import register
#...
#@register.filter
#def get_item(dictionary, key):
#    return dictionary.get(key)
