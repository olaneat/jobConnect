GMAIL_SOCIALACCOUNT_PROVIDERS =  { 'facebook':
                               {'METHOD': 'oauth2',
                                'SCOPE': ['email'],
                                'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
                                'LOCALE_FUNC': lambda request: 'en_US',
                                'VERSION': 'v2.4'
                               }
                           }
    
FACEBOOK_SOCIALACCOUNT_PROVIDERS = { 'google': 
                             { 'SCOPE': ['email'],
                               'AUTH_PARAMS': { 'access_type': 'online' }
                             }
                          }