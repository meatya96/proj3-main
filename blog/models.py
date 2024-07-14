from django.db import models

nullable = {"null": True, "blank": True}

class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    slug = models.CharField(max_length=100, **nullable)
    content = models.TextField()
    preview = models.ImageField(upload_to="blog/preview")
    created_at = models.DateTimeField(auto_now_add=True, **nullable)
    published = models.BooleanField(default=False)
    views = models.PositiveIntegerField(default=0, **nullable)

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоговые записи"

    def __str__(self):
        return self.title