from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel


class HomePage(Page):
    template = "home/home_page.html"

    banner_title = models.CharField (max_length=100, blank=False, null=True)
    banner_subtitle = models.CharField (max_length=200, blank=False, null=True)
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null = True,
        blank = False,
        on_delete = models.SET_NULL,
        related_name = "+",
    )
    
    banner_text = RichTextField()
    
    
    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
        FieldPanel("banner_subtitle"),
        ImageChooserPanel("banner_image"),
        FieldPanel("banner_text"),
    ]

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"