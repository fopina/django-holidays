from django.contrib import admin
from .models import (
    Group,
    Rule,
)

admin.site.register(Group)
admin.site.register(Rule)
