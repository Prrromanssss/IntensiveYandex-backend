from django.contrib import admin

from .models import FeedBack


@admin.register(FeedBack)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_text', 'created_on')
    fields = ('name', 'mail', 'text', 'created_on')

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False
