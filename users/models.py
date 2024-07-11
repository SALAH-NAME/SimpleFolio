from djongo import models

class Project(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField()
    url = models.URLField()
    details = models.TextField()

    class Meta:
        abstract = True

class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    role = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    job = models.CharField(max_length=100)
    summary = models.TextField()
    projects = models.ArrayField(
        model_container=Project,
    )
    about = models.TextField()
    skills = models.JSONField()

    def __str__(self):
        return self.username
