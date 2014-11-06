from django.contrib import admin
from .models import BoardMsg, MsgTag

# Register your models here.
class BoardMsgAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'tag', 'agreeTimes', 'created')
    list_filter = ('tag',)

class TagAdmin(admin.ModelAdmin):
    pass

admin.site.register(BoardMsg, BoardMsgAdmin)
admin.site.register(MsgTag, TagAdmin)
