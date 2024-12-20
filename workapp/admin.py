from django.contrib import admin
from .models import Apply,Customer,FuelCharge,FoodAllowance,ItemPurchased,VendorInfo,CurrentStatus,Technicians

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display=('id','u_name','u_address','u_contact_number','u_whatsapp_number','u_reffered_by')
admin.site.register(Customer,CustomerAdmin)
    
class ApplyAdmin(admin.ModelAdmin):
    list_display=('id','name','address','contact_number','whatsapp_number','reffered_by','service_by','work_type',
                  'item_name_or_number','issue','photos_of_item','estimation_document','estimated_price','estimated_date',
                  'any_other_comments')
admin.site.register(Apply,ApplyAdmin)


class FuelChargeAdmin(admin.ModelAdmin):
    list_display=('id','technician_name','date','purpose','kilometers','cost')
admin.site.register(FuelCharge, FuelChargeAdmin)


class FoodAllowanceAdmin(admin.ModelAdmin):
    list_display=('id','technician_name','date','purpose','cost')
admin.site.register(FoodAllowance, FoodAllowanceAdmin)


class ItemPurchasedAdmin(admin.ModelAdmin):
    list_display=('id','date','item_name','price','bill_photo')
admin.site.register(ItemPurchased, ItemPurchasedAdmin)


class VendorInfodAdmin(admin.ModelAdmin):
    list_display=('id','date','vendor_name','vendor_bill_photo','vendor_eta','vendor_cost')
admin.site.register(VendorInfo, VendorInfodAdmin)


class CurrentStatusdAdmin(admin.ModelAdmin):
    list_display=('id','date','technician_name','status')
admin.site.register(CurrentStatus, CurrentStatusdAdmin)






