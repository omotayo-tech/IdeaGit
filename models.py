from django.db import models
import bcrypt
import re
import datetime


class UserManager(models.Manager):
    def basic_validator(self, postdata):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postdata['first_name']) < 2:
            errors['first_name'] = "First name is too short."

        if len(postdata['last_name']) < 2:
            errors['last_name'] = "Last name is too short."

        if len(postdata['password']) < 8:
            errors['password'] = "Password is too short."

        if not postdata['password'] == postdata['confirm_password']:
            errors['password'] = 'Submitted passwords do not match.'

        if not re.match(r"[^@]+@[^@]+\.[^@]+", postdata['email']):
            errors['email'] = 'E-mail address is not in a valid format.'

        try:
            user = Login.objects.get(email=postdata['email'])
            print("got a user with a matching email address")
            errors['email'] = 'E-mail address already in use.'
        except:
            pass

        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    website = models.URLField(default='')
    phone_number = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

# Create your models here.
class OpinionManager(models.Manager):
    def opinion_validator(self, postdata):
        errors = {}
        if len(postdata['point_of_view']) < 5:
            errors['point_of_view'] = "No empty entries"

        return errors


class Opinion(models.Model):
    point_of_view = models.TextField()
    user = models.ForeignKey(User, related_name="thoughts")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    added= models.BooleanField(default=False)
    added_at = models.DateTimeField(blank= True,null=True)
    likes = models.ManyToManyField(User, related_name="liked_by")
    objects = OpinionManager()


class Comment(models.Model):
    comment = models.TextField()
    my_opinion = models.ForeignKey(Opinion, related_name="comments")
    composer = models.ForeignKey(User, related_name="comments")

    
