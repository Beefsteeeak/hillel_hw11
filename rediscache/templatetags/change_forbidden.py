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

    # correct
    # for word in forbidden_list:
    #     if word in value:
    #         value = value.replace(word, "***")

    # incorrect
    # for word in value:
    #     if word in forbidden_list:
    #         value = value.replace(word, "***")

    return value
