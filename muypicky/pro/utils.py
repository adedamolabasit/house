import random
import string
from django.utils.text import slugify
from django.conf import settings

# User=settings.AUTH_USER_MODEL
def random_string_genearator(size=10,chars=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_slug_generator(instance,new_slug=None):
    if new_slug is not None:
        slug=new_slug
    else:
        slug=slugify(instance.title)
    klass=instance.__class__
    qs_exists=klass.objects.filter(slug=slug)
    if qs_exists:
        new_slug="(slug)-(randstr)".format(
            slug=slug,
            randstr=random_string_genearator(size=4)
        )
        return unique_slug_generator(instance,new_slug=new_slug)
    return slug

         