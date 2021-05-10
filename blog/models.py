from django.db import models

class Post(models.Model):
    title = models.CharField(name="Название", max_length=255)
    slug = models.SlugField()
    intro = models.TextField(name="Вступление")
    body = models.TextField(name="Текст")
    date_abbed = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_abbed']

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(name='Имя', max_length=255)
    email = models.EmailField(name='E-mail', max_length=255)
    body = models.TextField(name='Текст')
    date_abbed = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_abbed']