import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(name="render_markdown")
def markdown_format(text):
    return mark_safe(markdown.markdown(text))  # nosec: [B703, B308]
