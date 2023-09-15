import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite2.settings')
django.setup()
from faker import Faker
from sec_app.models import Topic, Webpage, AccessRecord
fakegen = Faker()
def populate(N=5):
    for i in range(N):
        top = fakegen.word()
        topic = Topic.objects.get_or_create(top_name=top)[0]
        name = fakegen.company()
        url = fakegen.url()
        webpg = Webpage.objects.get_or_create(topic=topic, name=name, url=url)[0]
        date = fakegen.date()
        acrc = AccessRecord.objects.get_or_create(name=webpg, date=date)[0]
if __name__ == '__main__':
    print('populating database...')
    populate(10)
    print('population complete')







