from django.contrib import admin

# Register your models here.

from . models import Media, Rating
from .models import Hanekawa #Kuro
from .models import * #all functions are imported

admin.site.register(Media)
admin.site.register(Rating)

@admin.register(Hanekawa)
class HanekawaAdmin(admin.ModelAdmin):
    list_display = ('user', 'rating', 'vote_type')
#Abrar
@admin.register(CommentReport)
class CommentReportAdmin(admin.ModelAdmin):
    list_display = ('user', 'comment', 'reason', 'description')