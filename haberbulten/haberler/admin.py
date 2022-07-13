from django.contrib import admin
from .models import Makale, Gazeteci

# Register your models here.


@admin.register(Makale)
class HaberAdmin(admin.ModelAdmin):
    list_display = ('baslik', 'yazar', 'yayinlanma_tarihi',
                    'guncellenme_tarihi')
    list_display_links = ('baslik', 'yazar', 'yayinlanma_tarihi',
                          'guncellenme_tarihi')


@admin.register(Gazeteci)
class GazeteciAdmin(admin.ModelAdmin):
    list_display = ('id', 'isim', 'soyisim')
    list_display_links = ('id', 'isim', 'soyisim')
