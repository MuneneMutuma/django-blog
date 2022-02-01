from django.contrib import admin
from .models import Post

# register the Post model on the admin page
admin.site.register(Post)
