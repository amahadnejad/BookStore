from django import template

register = template.Library()


def translate_number(value):
    value = str(value)
    english_to_persian = value.maketrans('0123456789', '۰۱۲۳۴۵۶۷۸۹')
    return value.translate(english_to_persian)