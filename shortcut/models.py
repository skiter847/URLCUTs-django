from django.db import models
from string import ascii_letters, digits
import random


def create_url_id() -> str:
    """ Генерирует рандомную строку длинной 6 символов """

    symbols = ascii_letters + digits
    res = ''
    for _ in range(6):
        res += random.choice(symbols)

    return res


class URL(models.Model):
    url_id = models.CharField(max_length=10, default=create_url_id())
    link = models.URLField()
    usage = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.url_id

