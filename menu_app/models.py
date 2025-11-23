from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError

class Menu(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название меню")

    class Meta:
        verbose_name = "Меню"
        verbose_name_plural = "Меню"

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, related_name='items', on_delete=models.CASCADE, verbose_name="Меню")
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE, verbose_name="Родительский пункт")
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    url = models.CharField(max_length=255, blank=True, null=True, verbose_name="URL или named URL")
    named_url = models.CharField(max_length=100, blank=True, null=True, verbose_name="Named URL (если есть)")

    class Meta:
        verbose_name = "Пункт меню"
        verbose_name_plural = "Пункты меню"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        if self.named_url:
            try:
                return reverse(self.named_url)
            except:
                pass
        return self.url if self.url else '#'
    
    def clean(self):
        # Проверка на то, что пункт не может быть своим собственным родителем
        if self.parent and self.parent.pk == self.pk:
            raise ValidationError("Пункт меню не может быть своим собственным родителем.")
        # Проверка на циклические зависимости (простая рекурсия, можно улучшить для глубоких деревьев)
        parent = self.parent
        while parent:
            if parent.pk == self.pk:
                raise ValidationError("Обнаружена циклическая зависимость в родителях.")
            parent = parent.parent  