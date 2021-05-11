
from django.core.exceptions import ValidationError
from .models import RestaurantLocation

def  validate_email(value):
    email=value
    if ".edu" in email:
        raise ValidationError('we do not accept edu email')

CATEGORIES=['Mexican','Asian','American','Local']
def validate_category(value):
    cat=value.capitalize()
    if not value in CATEGORIES and not cat in CATEGORIES:
        raise ValidationError(f'{value} this is is not a valid category')

# def validate_name(value):
#     name=value
#     qs=RestaurantLocation.objects.filter(name=name)
#     if name in qs:
#         raise ValidationError(f'{value}: you have an existing restaurant location')



