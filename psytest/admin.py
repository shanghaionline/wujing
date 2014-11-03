import re
from django.contrib import admin
from .models import Paper, Question, Option, Result
# Register your models here.

class OptionInline(admin.TabularInline):
    model = Option
    fk_name = 'question'
    extra = 1

class ResultInline(admin.TabularInline):
    model = Result
    extra = 1

class PaperAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'id')
    list_display_links = ('__str__',)
    search_fields = ('name',)
    inlines = (ResultInline,)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'paper', 'order')
    inlines = (OptionInline,)
    list_filter = ('paper__name',)
    raw_id_fields = ('paper',)

    def get_changeform_initial_data(self, request):
        params = request.GET
        initial_data = super(QuestionAdmin, self).get_changeform_initial_data(request)
        if '_changelist_filters' in params and 'paper' not in initial_data:
            p = params['_changelist_filters']
            m = re.search(r'paper__id=(\d+)', p)
            if m is not None:
                initial_data['paper'] = m.group(1)
        return initial_data


admin.site.register(Paper, PaperAdmin)
admin.site.register(Question, QuestionAdmin)

