from django.contrib import admin
from .models import Party, Vote

@admin.register(Party)
class PartyAdmin(admin.ModelAdmin):
    list_display = ('name', 'total_votes', 'reveal_date')
    search_fields = ('name', 'description')
    list_filter = ('reveal_date',)

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ('voter_id', 'party', 'voted_at')
    search_fields = ('voter_id', 'party__name')
    list_filter = ('voted_at', 'party')