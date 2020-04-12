from django import template

register = template.Library()

# Function for the filter
def cut(value, arg):
    """
    This cuts out all values of "arg" from the string
    """
    return value.replace("arg", "")

# Register filter
register.filter("cut", cut)
