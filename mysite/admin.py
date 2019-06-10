from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Data

@admin.register(Data)
class DataAdmin(ImportExportModelAdmin):
    list_display = ('nickname', 'contact', 'location', 'enroll_date')
    list_filter = ('location', 'deal_type','enroll_date')

    fieldsets = (
        (None, {
            'fields' : ('nickname', 'contact')
        }),
        ('Room Info', {
            'fields' : (('location', 'moving_date'),('deal_type','residence_type'),('deposit','monthly_price','manage_price'),
                ('room_type', 'roomfloor', 'room_size'), 'option' 
                )
        }),
        ('More details', {
            'fields' : ('age', 'sex', 'job','detail')
        }),
    )

