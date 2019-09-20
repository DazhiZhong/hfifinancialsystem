from django.contrib import admin
from .models import Post,EnvVaribles,testmodel
# Register your models here.
admin.site.register(Post)
admin.site.register(EnvVaribles)
admin.site.register(testmodel)
