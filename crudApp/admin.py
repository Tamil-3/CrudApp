from django.contrib import admin
from crudApp.models import UserCrud

class UserCrudAdmin(admin.ModelAdmin):
    crud_det = ['firstname', 'lastname', 'country']

admin.site.register(UserCrud, UserCrudAdmin)
