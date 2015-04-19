from django.contrib import admin

# Register your models here.
from .models import Task, Category, Event, FlowModel, CredentialsModel
from oauth2client.django_orm import CredentialsField
admin.site.register(Task)
admin.site.register(Category)
admin.site.register(Event)
admin.site.register(FlowModel)
admin.site.register(CredentialsModel)
