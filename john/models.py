from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# HOME SECTION

class Home(models.Model):
    name = models.CharField(max_length=20)
    greetings_1 = models.CharField(max_length=50)
    
    picture = models.ImageField(upload_to='picture/')
    # save time when modified
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# ABOUT SECTION

class About(models.Model):
    heading = models.CharField(max_length=50)
    career = models.CharField(max_length=20)
    description = models.TextField(blank=False)
    profile_img = models.ImageField(upload_to='profile/')
    
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.career


class Profile(models.Model):
    about = models.ForeignKey(About,
                                on_delete=models.CASCADE)
    social_name = models.CharField(max_length=10)
    link = models.URLField(max_length=200)



# SKILLS SECTION

class Category(models.Model):
    name = models.CharField(max_length=20)

    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return self.name

class Skills(models.Model):
    category = models.ForeignKey(Category,
                                on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=20)

    

# PORTFOLIO SECTION

class Portfolio(models.Model):
    title = models.CharField(default="Video Title", max_length=50)
    image = models.ImageField(upload_to='portfolio/')
    link = models.URLField(max_length=200)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Portfolio {self.id}'

# STREAMER SECTION

class Streamers(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='portfolio/')
    link = models.URLField(max_length=200)

    def __str__(self):
        return self.name


# Tournament section

class Tourn(models.Model):
    tp = models.CharField(max_length=100, default='Tournament / Scrim')
    host = models.CharField(max_length=50)
    macth = models.CharField(max_length=20)
    details = models.TextField(blank=False)
    
    room = models.CharField(max_length=500, null=True, blank=True)

    when = models.DateTimeField(null=True)

    updated = models.DateTimeField(auto_now=True)
    

  

    def __str__(self):
        return self.host


class Results(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    gametype = models.CharField(max_length=2, default="MP/BR")
    game = models.ForeignKey(Tourn, on_delete=models.CASCADE)
    result = models.CharField(max_length=100, default="WIN 5-0")
    when = models.DateField(null=True)

    def __str__(self):
        return self.result


class Store(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='store/')
    link = models.URLField(max_length=200)
    price = models.IntegerField(max_length=100)

    def __str__(self):
        return self.name


class Tournament(models.Model):
    tp = models.CharField(max_length=100, default='Tournament / Scrim')
    host = models.CharField(max_length=200)
    when = models.DateTimeField()
    info = models.TextField()
    game_type = models.CharField(max_length=2, default="MP/BR")
    room = models.CharField(max_length=500, null=True, blank=True)
    result = models.CharField(max_length=500, null=True, blank=True)
    
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Participant'
        verbose_name_plural = 'Participants'

    def __str__(self):
        return self.tp

    


class Participants(models.Model):
    tournament = models.ForeignKey(Tournament,
                                   on_delete=models.CASCADE)
    team_name = models.CharField(max_length=20)


class News(models.Model):
    topic = models.CharField(max_length=50)
    content = models.TextField(blank=False)
    img = models.ImageField(upload_to='news/')

    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.topic


# TEAM SECTION

class Team(models.Model):
    player = models.CharField(default="Videos Title", max_length=55)
    image = models.ImageField(upload_to='portfolio/')

    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.player


class Livestream(models.Model):
    title = models.CharField(max_length=300)
    link = models.URLField(max_length=200)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    


