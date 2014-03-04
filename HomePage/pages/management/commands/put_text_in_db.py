from django.core.management.base import BaseCommand, CommandError
from HomePage.pages.models import Essay, Biopic, Personal
from os import listdir
import datetime

class Command(BaseCommand):
    base_path = 'HomePage/pages/static/'
    #Reads the .txt files in the static folder, creates models from them,
    #and writes them to the db.
    def handle(self):
        self.read_in_essays()
        self.read_in_biopics()
        self.read_in_personal()

    def read_in_essays(self):
        essay_order = [
            'Beckoning',
            'Dislocated Priors',
            'Misguided but Effective Heuristics',
            'Utility Swaps',
            'In Defense of Eating Meat',
            'More on Ethics of Vegetarianism',
            'Virtue Ethics',
            'A Job Well Done',
            'A Life Well Lived',
            'Categorizing Errors of Reasoning',
            'Unpacking',
            'Global Maxima',
            'A Simple Case of Updating'
        ]
        for file in listdir(self.base_path + '/Essays'):
            o = open(file, 'rb')
            date_tokens = o.readline().split('-')
            name = file[1:-4]
            try:
                essay = Essay(
                    name = name,
                    publish_date = datetime.date(date_tokens[0], date_tokens[1], date_tokens[2]),
                    content = o.read(),
                    rank = essay_order.index(name))
            except essay.DoesNotExist:
                raise CommandError('Essay %s could not be made' % essay.name)
            except ValueError:
                raise CommandError('Essay %s not in list' % essay.name)
            essay.save()

    def read_in_biopics(self):
        biopic_order = [
           'Nassim Taleb',
           'Sam Harris',
           'Christopher Hitchens',
           'Ludwig Wittgenstein'
        ]
        for file in listdir(self.base_path + '/Biopics'):
            o = open(file, 'rb')
            date_tokens = o.readline().split('-')
            name = file[1:-4]
            try:
                biopic = Biopic(
                    name = name,
                    publish_date = datetime.date(date_tokens[0], date_tokens[1], date_tokens[2]),
                    content = o.read(),
                    rank = biopic_order.index(name))
            except biopic.DoesNotExist:
                raise CommandError('Biopic %s could not be made' % biopic.name)
            except ValueError:
                raise CommandError('Biopic %s not in list' % biopic.name)
            biopic.save()

    def read_in_personals(self):
        personal_order = [
            'My Grandma Janet',
            'A Difficult Life Transition',
            'Singularity Summit 2012',
            'Lessons from 2010-2011',
            'Nootropics'
        ]
        for file in listdir(self.base_path + '/Personals'):
            o = open(file, 'rb')
            date_tokens = o.readline().split('-')
            name = file[1:-4]
            try:
                personal = Personal(
                    name = name,
                    publish_date = datetime.date(date_tokens[0], date_tokens[1], date_tokens[2]),
                    content = o.read(),
                    rank = personal_order.index(name))
            except personal.DoesNotExist:
                raise CommandError('Personal %s could not be made' % personal.name)
            except ValueError:
                raise CommandError('Personal %s not in list' % personal.name)

            personal.save()