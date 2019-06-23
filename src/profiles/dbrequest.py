# -*- coding: utf-8 -*-
'''
all queiry commands
https://firebase.google.com/docs/database/admin/retrieve-data
'''

def qthis():
    import firebase_admin
    from firebase_admin import credentials
    from firebase_admin import db
    import requests

    # Fetch the service account key JSON file contents
    cred = credentials.Certificate('weatherwear-a4626-firebase-adminsdk-0nxej-aba5711d50.json')
    # Initialize the app with a service account, granting admin privileges
    firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://weatherwear-a4626.firebaseio.com/'
    })

    dinos = db.reference('test_hot')
    jef = dinos.order_by_child('Temperature').limit_to_last(5).get()

    print(jef)

#qthis()
