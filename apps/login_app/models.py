# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import re

import bcrypt

# Create your models here.

class UserManager(models.Manager):

    def loginVal(self, postData):
        results = {
            'status': False,
            'errors': [],
            'user': None
        }
        email_matches = self.filter(email = postData['email'])
        if len(email_matches) == 0:
            results['errors'].append('Please check your email and password and try again.')
            results['status'] = True
        else:
            results['user'] = email_matches[0]
            if not bcrypt.checkpw(postData['password'].encode(), results['user'].password.encode()):
                results['errors'].append('Please check your email and password and try again.')
                results['status'] = True
        return results
        
    

    def createUser(self, postData):
        new_password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
        self.create(first_name = postData['first_name'], last_name = postData['last_name'], email = postData['email'], password = new_password)

    def registerVal(self, postData):
        results = {
            'status': False,
            'errors': []    
        }
        if len(postData['first_name']) < 2:
            results['status'] = True
            results['errors'].append('First name is too short.')

        if not postData['first_name'].isalnum():
            results['status'] = True 
            results['errors'].append("For First Name, please use alphanumeric characters only")

        if not postData['last_name'].isalnum():
            results['status'] = True 
            results['errors'].append("For Last Name, please use alphanumeric characters only")

        if len(postData['last_name']) < 2:
            results['status'] = True
            results['errors'].append('Last name is too short.')

        if not re.match(r"[^@]+@[^@]+\.[^@]+", postData['email']):
            results['status'] = True
            results['errors'].append('Email is not valid.')
        
        if len(postData['password']) < 8:
            results['status'] = True
            results['errors'].append('Password is too short.')

        if not postData['password'].isalnum():
            results['status'] = True 
            results['errors'].append("Please Enter a valid Password")

        if postData['password'] != postData['c_password']:
            results['status'] = True
            results['errors'].append('Passwords do not match.')

        user = self.filter(email= postData['email'])

        if len(user) > 0:
            results['status'] = True
            results['errors'].append('User already exists in database.')

        return results
        

        
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = UserManager()
    friends = models.ManyToManyField('User', related_name="friended")
