import random

from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def random_record(context):
    """
    Custom tag to get random book and its authors
    :param context:
    :return: name of a book, authors of a book
    """

    values = context["object_list"]
    counter = len(values)
    number = random.randint(1, counter)

    return values[number].name, list(values[number].authors.all())
