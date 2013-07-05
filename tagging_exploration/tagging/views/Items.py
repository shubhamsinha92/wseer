from tagging_exploration.tagging.models import Items
from django.contrib.restful_model_views.ModelResources import ModelResources, edit, create, dispatch

class Items(ModelResources):
  pass

  class Items_Member (ModelResources.ModelResources_Member):
    pass
