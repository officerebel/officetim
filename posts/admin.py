from django.contrib import admin

from . models import Post, Contact, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ("title", "author", "created_at", "tag_list")
	search_fields = ("title", "body", "author__username")
	list_filter = ("author",)

	def get_queryset(self, request):
		qs = super().get_queryset(request)
		return qs.prefetch_related("tags")

	def tag_list(self, obj):
		return ", ".join(t.name for t in obj.tags.all())


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
	list_display = ("name", "email", "subject", "created_at")
	search_fields = ("name", "email", "subject")


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
	list_display = ("name",)
	search_fields = ("name",)