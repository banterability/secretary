from django import template
from django.conf import settings

register = template.Library()

@register.simple_tag
def media(path=''):
    """
    Returns an absolute URL pointing to the given media URL.

    The optional first argument is the path to the file starting from
    ``settings.MEDIA_URL``.

    For example, if your ``MEDIA_URL`` is ``'http://media.example.com'``
    then in your template you can get the URL for ``css/mystyle.css``
    like this:

        {% media 'css/mystyle.css' %}

    The URL returned would be ``http://media.example.com/css/style.css``.

    If no argument is given, the tag will just output the ``MEDIA_URL``
    (appending a trailing slash if it does not end in one). For example,
    ``{% media %}`` would return ``http://media.example.com/``.
    """
    import urlparse
    url = settings.MEDIA_URL or ''
    if path:
        return urlparse.urljoin(url, path)
    elif not url.endswith('/'):
        return '%s/' % url
    return url