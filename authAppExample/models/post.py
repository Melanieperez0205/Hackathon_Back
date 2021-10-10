from django.db import models
from .user     import User

class Article(models.Model):
    idpost = models.BigAutoField(primary_key=True)
    author = models.ForeignKey(User, related_name='nombreUsuario', on_delete=models.CASCADE)
    title = models.CharField(max_length = 50,verbose_name = "Başlık")
    content = models.TextField(max_length =100)
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    article_image = models.FileField(blank = True,null = True,verbose_name="Makaleye Fotoğraf Ekleyin")
 

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Article, self).save(*args, **kwargs)        

    class Meta:
        ordering = ['-created_date']
class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete = models.CASCADE,verbose_name = "Makale",related_name="comments")
    comment_author = models.CharField(max_length = 50,verbose_name = "İsim")
    comment_content = models.CharField(max_length = 200,verbose_name = "Yorum")
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_content
    class Meta:
        ordering = ['-comment_date']