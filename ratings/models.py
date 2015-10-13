from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

from products.models import Product

class Rating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Пользователь')
    product = models.ForeignKey(Product, verbose_name='Товар', related_name='ratings')
    comment = models.TextField(verbose_name='Комментарий')
    rating = models.IntegerField(verbose_name='Рейтинг', validators=[MinValueValidator(1),
                                                                     MaxValueValidator(5)])
    date = models.DateTimeField(verbose_name='Дата', auto_now_add=True)
    image = models.ImageField(verbose_name='Изображение', upload_to='images/rating', blank=True)
    moderated = models.BooleanField(verbose_name='Модерация пройдена', default=False)

    def __str__(self):
        return 'Отзыв №' + str(self.pk)

    class Meta:
        ordering = ['-date']
