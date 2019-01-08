from django.contrib import admin
from .models import *
import datetime
from datetime import timedelta
from decimal import Decimal


class ItemInlineAdmin(admin.TabularInline):
    model = Item
    extra = 1

    def get_extra(self, request, obj=None, **kwargs):
        if obj:
            return 0
        return self.extra


class TemaAdmin(admin.ModelAdmin):
    inlines = [ItemInlineAdmin]
    list_display = ('nome', 'valor_aluguel', 'cor_toalha')
    list_filter = ('valor_aluguel',)
    search_fields = ('nome',)


class ClienteAdmin(admin.ModelAdmin):
    def antigo(self,obj):
        hoje = datetime.datetime.now()
        return hoje.date() >= obj.data + timedelta(days=360)

    list_display = ('nome', 'telefone','data','antigo')
    ordering = ('nome',)
    search_fields = ('nome',)

    antigo.short_description = 'Cliente Antigo?'
    antigo.boolean=True


class AluguelAdmin(admin.ModelAdmin):
    def valor_com_desconto(self,obj):
        desconto = Decimal(float(0.20))
        if ClienteAdmin.antigo.boolean == True:
            cobrado = obj.valor_cobrado-(obj.valor_cobrado*desconto)
            return '{:.2f}'.format(cobrado)
        else:
            return obj.valor_cobrado

    list_display = ('cliente', 'data_festa', 'endereco', 'valor_cobrado','valor_com_desconto')
    list_filter = ['valor_cobrado']
    search_fields = ['cliente__nome','endereco__logradouro']
    ordering = ('data_festa', 'valor_cobrado')


admin.site.register(Tema, TemaAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Aluguel, AluguelAdmin)
admin.site.register(Endereco)
admin.site.register(Item)


#default:"Administração do Django"
admin.site.site_header = 'Painel de Controle'

#default:"Administração do Site"
admin.site.index_title = ''

#default:"Site de Administração do Django"
admin.site.site_title = 'Questão 03'
