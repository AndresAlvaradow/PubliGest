from django.contrib import admin
from apps.Publigest.models import DataScrapy, EntidadesNombradas, PalabrasClaves, EntidadesNombradas_texto
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class DataCategoria(resources.ModelResource):
    class Meta:
        model = DataScrapy
        import_id_fields = ('post_id',)

class DataAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['text']
    list_display = ('text',	'likes', 'loves', 'hahas', 'wows', 'sads', 'hates', 'cares', 'link')
    resource_class = DataCategoria
admin.site.register(DataScrapy,DataAdmin)

class DataEntidad(resources.ModelResource):
    class Meta:
        model = EntidadesNombradas
        import_id_fields = ('ent_id',)
        
class DataAdminEntidad(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['etiqueta']
    list_display = ('ent_id', 'entidad', 'etiqueta')
    resource_class = DataEntidad
admin.site.register(EntidadesNombradas, DataAdminEntidad)
# Register your models here.


class DataKW(resources.ModelResource):
    class Meta:
        model = PalabrasClaves
        import_id_fields = ('kw_id',)
        
class DataAdminKW(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['text']
    list_display = ('kw_id', 'keyswords', 'text')
    resource_class = DataKW
admin.site.register(PalabrasClaves, DataAdminKW)

class DataEntidad_texto(resources.ModelResource):
    class Meta:
        model = EntidadesNombradas_texto
        import_id_fields = ('id_ent_text',)
        
class DataAdminEntidad_texto(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['texto']
    list_display = ('id_ent_text', 'entidad', 'texto')
    resource_class = DataEntidad_texto
admin.site.register(EntidadesNombradas_texto, DataAdminEntidad_texto)