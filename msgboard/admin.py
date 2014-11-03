from django.contrib import admin
from .models import BoardMsg

# Register your models here.
class BoardMsgAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'user', 'agreeTimes', 'created')

admin.site.register(BoardMsg, BoardMsgAdmin)
