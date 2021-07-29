from django.contrib import admin
from .models import Home, About, Participants, Profile, Category, Results, Skills, Portfolio, Store, Streamers, Tourn, Tournament, Team, News, Livestream


# Home
admin.site.register(Home)

# About
class ProfileInline(admin.TabularInline):
    model = Profile
    extra = 1

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
     inlines = [
        ProfileInline,
    ]
# Tournements
admin.site.register(Tourn)
# Skills
class SkillsInline(admin.TabularInline):
    model = Skills
    extra = 2

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
     inlines = [
        SkillsInline,
    ]


class ParticipantsInline(admin.TabularInline):
    model = Participants
    extra = 2


@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):
    inlines = [
        ParticipantsInline,
    ]


# Portfolio
admin.site.register(Portfolio)
admin.site.register(Streamers)
admin.site.register(Results)
admin.site.register(Store)
admin.site.register(Team)
admin.site.register(News)
admin.site.register(Livestream)
