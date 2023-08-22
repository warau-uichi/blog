from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{str(self.id)}_{self.title}"

class News(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{str(self.id)}_{self.title}"
