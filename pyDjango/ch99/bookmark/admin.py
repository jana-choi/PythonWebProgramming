from django.contrib import admin
from bookmark.models import Bookmark

@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "url")

# admin.site.register(Bookmark, BookmarkAdmin) # 데코레이터 대신 작성 가능