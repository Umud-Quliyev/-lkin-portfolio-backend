from django.db import models

class Lab(models.Model):
    key = models.CharField(max_length=50, unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    detail = models.TextField()
    color = models.CharField(max_length=20)
    background = models.CharField(max_length=20)
    text_color = models.CharField(max_length=20)

class LabImage(models.Model):
    lab = models.ForeignKey(Lab, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='labs/')

class LabExtra(models.Model):
    lab = models.OneToOneField(Lab, related_name='extra', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.JSONField(default=list)        # List of strings
    contents = models.JSONField(default=list)    # List of strings
    system = models.JSONField(default=list)      # List of strings


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"