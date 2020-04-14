from django.utils.text import slugify
from django.core.exceptions import ValidationError
from time import time
#from novatlet.models import Post
import datetime 

def gen_slug(s):
    s.lower()
    format_string = slugify(s, allow_unicode=True)
    s_translate = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e',
        'ж': 'j', 'з': 'z', 'и': 'i', 'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm',
        'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
        'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ъ': '',
        'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya', '0': '0', '1': '1', '2': '2',
        '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9'
        }

    s_encode = []

    for i in format_string:
        try:
            if i == '-' or i == '_':
                s_encode.append('')
            s_encode.append(s_translate.get(i, i))
        except:
            raise ValidationError("Slug can't be generated!")
    new_slug = ''.join(map(str, s_encode))
    return new_slug + '-' + str(int(time()))


class GetRandomSidebarPost:
    def __init__(self, model=None):
        self.model = model

    def get_newest_post(self):
        get_newest_posts = self.model.objects.filter(post_date__lte=datetime.datetime.today())[:3]

        return get_newest_posts


class RandomImage:
    pass