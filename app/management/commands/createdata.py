from django.core.management.base import BaseCommand
from faker import Faker
import faker.providers 
from app.models import Post

# make costum provider
DESCRIPTION = [
    "My nickname is Septa, and I'm 28 years old.",
    "I'm a Backend Developer and crazy about my job.",
    "I have bachelor degree of computer engineering.",
    "My interests are listening to the music and watching movie."
]
TITLE = [
    "personal-info",
    "job",
    "education",
    "intrest"
]
# make costum provider
class Provider(faker.providers.BaseProvider):
    def post_title(self):
        return self.random_element(TITLE)
    
    def post_description(self):
        return self.random_element(DESCRIPTION)

# setup faker
class Command(BaseCommand):
    help = "Command Information"

    def handle(self, *args, **kwargs):
        fake = Faker(["fa_IR"]) # use specific language.
        fake.add_provider(Provider) # use costum provider

        # print(fake.name())
        # print(fake.paragraph())
        # print(fake.post_description())

        # use costum fake data and save in DB.
        for _ in range(5):
            discription = fake.post_description()
            title = fake.post_title()
            Post.objects.create(description=discription, title=title)

        # checking for make sure that data inserted into DB.
        check_data = Post.objects.all().count()
        print(check_data)