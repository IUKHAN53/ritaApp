from django.contrib import admin
from users.models import GoogleCred, FacebookCred, GoogleFile, FacebookFile
# Register your models here.

admin.site.register(GoogleCred)
admin.site.register(FacebookCred)
admin.site.register(GoogleFile)
admin.site.register(FacebookFile)
