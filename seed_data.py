import os
import django
import random
from faker import Faker
from django.utils import timezone

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hangarin.settings")
django.setup()

from tasks.models import Task, Note, SubTask, Priority, Category

fake = Faker()

priorities = list(Priority.objects.all())
categories = list(Category.objects.all())

for _ in range(5):
    task = Task.objects.create(
        title=fake.sentence(nb_words=5),
        description=fake.paragraph(nb_sentences=3),
        status=random.choice(["Pending", "In Progress", "Completed"]),
        priority=random.choice(priorities),
        category=random.choice(categories),
        deadline=timezone.make_aware(fake.date_time_this_month())
    )

    for _ in range(random.randint(1, 2)):
        Note.objects.create(
            task=task,
            content=fake.paragraph(nb_sentences=2)
        )

    for _ in range(random.randint(1, 3)):
        SubTask.objects.create(
            task=task,
            title=fake.sentence(nb_words=4),
            status=random.choice(["Pending", "In Progress", "Completed"])
        )
