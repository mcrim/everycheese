from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField
from model_utils.models import TimeStampedModel
from django.conf import settings

# Create your models here.
class Library(TimeStampedModel):
    book_name = models.CharField("Book name", max_length=255)
    slug = AutoSlugField("Book address", unique=True, always_update=False, populate_from="book_name")
    description = models.TextField("Description", blank=True)

    class Genre(models.TextChoices):
        UNSPECIFIED = "unspecified","Unspecified"
        FICTION = "fiction","Fiction"
        NONFICTION = "nonfiction","Nonfiction"
        COMDEY = "comdey","Comedy"
        DRAMA = "drama","Drama"
        ROMANCE = "romance","Romance"
        FANTASTY = "fantasy","Fantasy"
        ACTION = "action","Action"
        HORROR = "horror","Horror"
        HISTORICAL = "historical","Historical"

    genre = models.CharField("Genre",max_length=50, choices=Genre.choices, default=Genre.UNSPECIFIED)

    author_firstname = models.CharField( 
        "Author's first name", blank=True,
        max_length=255
    )
    author_lastname = models.CharField( 
        "Author's last name", blank=True,
        max_length=255
    )

    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.book_name
    
    def get_absolute_url(self):
        return reverse("library:detail", kwargs={"slug": self.slug})
    