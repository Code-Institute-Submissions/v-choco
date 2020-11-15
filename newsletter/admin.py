from django.contrib import admin

from .models import NewsletterUser


class NewsletterAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'email',
        'date_added',
    )


admin.site.register(NewsletterUser, NewsletterAdmin)
