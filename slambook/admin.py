from django.contrib import admin
from .models import (CharacterTemplate,CQuestion,
                     RCTemplateCQuestions,Slams,Slam,SlamChart)

# Register your models here.

class CharacterTemplateAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(CharacterTemplate)
admin.site.register(CQuestion)
admin.site.register(RCTemplateCQuestions)
admin.site.register(Slams)
admin.site.register(Slam)
admin.site.register(SlamChart)