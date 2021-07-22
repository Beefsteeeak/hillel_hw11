from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def change_forbidden(value):
    """
    Custom filter to change certain forbidden words to "***" in a given text
    :param value:
    :return: text with changed words
    """

    forbidden_list = [
        "QuerySet",
        "index",
        "Random",
        "new",
    ]

    for word in forbidden_list:
        value = value.replace(word, "***")

    # forbidden_list_lower = [f.lower() for f in forbidden_list]

    # for word in value.split():
    #     if word.lower().strip(",.;:!?@#$%&^*<>") in forbidden_list_lower:
    #         value = value.replace(word, "***")

    return value
