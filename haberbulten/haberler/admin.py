from django.contrib import admin
from .models import Makale

# Register your models here.


@admin.register(Makale)
class HaberAdmin(admin.ModelAdmin):
    list_display = ('baslik', 'yazar', 'yayinlanma_tarihi',
                    'guncellenme_tarihi')
    list_display_links = ('baslik', 'yazar', 'yayinlanma_tarihi',
                          'guncellenme_tarihi')
