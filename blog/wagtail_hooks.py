from wagtail.core import hooks
from wagtail.core.telepath import register
from wagtail.core.widget_adapters import WidgetAdapter

from django.conf import settings
from django.utils.html import format_html

from wagtailmath.blocks import MathJaxWidget


# Register MathJaxWidget with Wagtail Telepath
register(WidgetAdapter(), MathJaxWidget)


@hooks.register("insert_global_admin_css")
def import_fontawesome_stylesheet():
    return format_html(
        '<link rel="stylesheet" href="{}">',
        settings.STATIC_URL + 'fontawesome-free-5.15.4-web/css/fontawesome.min.css'
    )
