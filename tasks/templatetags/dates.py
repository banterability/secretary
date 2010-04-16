from django import template
from django.template.defaultfilters import date as datefilter

register = template.Library()

@register.inclusion_tag('timeago.html')
def timeago(datetime):
    """
    Inserts <abbr> tag that works with timeago js script.
    """    
    iso_date = datetime.isoformat()
    # cut off nasty milliseconds that confusion timeago
    index = iso_date.find('.')
    if index != -1:
        iso_date = iso_date[:index]
    
    pretty_date = datefilter(datetime, "P")
    return {'iso_date':iso_date, 'pretty_date':pretty_date}