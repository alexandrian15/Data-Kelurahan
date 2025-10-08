from django.contrib import admin
from .models import Warga  # Pastikan import model Warga

# Mendaftarkan model ke admin
@admin.register(Warga)
class WargaAdmin(admin.ModelAdmin):
    list_display = ('nik', 'nama_lengkap', 'alamat', 'no_telepon')
    list_filter = ('alamat',)
    search_fields = ('nik', 'nama_lengkap')
    ordering = ('nama_lengkap',)
    list_per_page = 20
    fieldsets = (
        ('Data Pribadi', {
            'fields': ('nik', 'nama_lengkap')
        }),
        ('Kontak', {
            'fields': ('alamat', 'no_telepon')
        }),
    )