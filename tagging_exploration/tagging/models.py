from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tags(models.Model):
  tag_name = models.CharField(maxlength=255)
  
  def __str__(self):
    return self.tag_name
  
  class Admin: 
    list_display = ('tag_name',)
    search_fields = ['tag_name']
  class Meta:
    verbose_name_plural = 'Tags'
  
  
class Items(models.Model):
  item_name = models.CharField(maxlength=255)
  added_on  = models.DateTimeField(core=True, auto_now_add=True)
  
  def __str__(self):
    return self.item_name
  
  class Admin: 
    list_display = ('item_name', 'added_on')
    search_fields = ['item_name']
  class Meta:
    verbose_name_plural = 'Items'
    ordering = ['item_name']
    
    
class Users(models.Model):
  user = models.OneToOneField(User)
    

class Tag_Assignment(models.Model):
  assigned_on  = models.DateTimeField(core=True)
  item = models.ForeignKey(Items)
  tag = models.ForeignKey(Tags)
  user = models.ForeignKey(Users)
  