"""
This family file was auto-generated by generate_family_file.py script.

Configuration parameters:
  url = https://www.4training.net
  name = 4training

Please do not commit this to the Git repository!
"""
from pywikibot import family


class Family(family.Family):  # noqa: D101

    name = '4training'
    langs = {
        'en': 'www.4training.net',
    }

    def scriptpath(self, code):
        return {
            'en': '/mediawiki',
        }[code]

    def protocol(self, code):
        return {
            'en': 'https',
        }[code]
