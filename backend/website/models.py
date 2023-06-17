from django.db import models
import uuid
# Create your models here.


class FeesStructure(models.Model):
    pdf_file = models.FileField(
        upload_to="Fees-structure/")
    created = models.DateField(auto_now_add=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)


class Gallery(models.Model):
    GALLERY_CHOICES = (
        ('Main Gallery', 'Main Gallery'),
        ('Student Gallery', 'Student Gallery'),
    )
    photo = models.FileField(upload_to="Gallery")
    title = models.CharField(max_length=100)
    gallery_type = models.CharField(max_length=100, choices=GALLERY_CHOICES)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    created = models.DateField(auto_now_add=True, editable=False)

    class Meta:
        verbose_name_plural = "Galleries"

    def __str__(self) -> str:
        return self.title
