from django import template

register = template.Library()

@register.filter
def replace_vowel_with_something(value, arg):
    new_value = ""
    for letter in value:
        if letter in 'aeiou':
            new_value += arg
        else:
            new_value += letter
    return new_value