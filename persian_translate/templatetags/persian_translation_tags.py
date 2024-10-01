from django import template

# Register File
register = template.Library()


# Translate Number From English To Persian
@register.filter
def translate_number(value):
    value = str(value)
    english_to_persian = value.maketrans('0123456789', '۰۱۲۳۴۵۶۷۸۹')
    return value.translate(english_to_persian)
