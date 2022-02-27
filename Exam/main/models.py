from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models

from Exam.main.validators import character_validator


class Profile(models.Model):
    MAX_USERNAME_LENGTH = 15
    MIN_AGE = 0
    username = models.CharField(max_length=MAX_USERNAME_LENGTH, validators=[
        MinLengthValidator, character_validator
    ], )
    email = models.EmailField()
    age = models.IntegerField(
        blank=True,
        null=True,
        validators=[
            MinValueValidator(MIN_AGE)
        ]
    )


class Album(models.Model):
    MAX_NAME_LENGTH = 30
    MAX_ARTIST_LENGTH = 30
    MIN_PRICE_VALUE = 0
    MAX_GENRE_LENGTH = 30
    CHOICES = (
        ("Pop Music", "Pop Music"),
        ("Jazz Music", "Jazz Music"),
        ("R&B Music", "R&B Music"),
        ("Rock Music", "Rock Music"),
        ("Country Music", "Country Music"),
        ("Dance Music", "Dance Music"),
        ("Hip Hop Music", "Hip Hop Music"),
        ("Other", "Other"),
    )

    name = models.CharField(max_length=MAX_NAME_LENGTH, unique=True)
    artist = models.CharField(max_length=MAX_ARTIST_LENGTH)
    genre = models.CharField(max_length=MAX_GENRE_LENGTH, choices=CHOICES)

    description = models.TextField(blank=True, null=True)
    image_url = models.URLField()
    price = models.FloatField(validators=[
        MinValueValidator(MIN_PRICE_VALUE)
    ])
