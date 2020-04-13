from django.contrib import admin
from .models import FeedBack

class FeedbackAdmin(admin.ModelAdmin):
    class Meta:
        model = FeedBack
        fields = ['name', 'phone', 'description', 'call_time', 'email']


admin.site.register(FeedBack, FeedbackAdmin)
# Register your models here.
