from faker import Faker
from django.utils import timezone
from tasks.models import Task, SubTask, Note, Priority, Category
import random

fake = Faker()

# ---- 1. Ensure Priorities exist ----
priority_names = ["High", "Medium", "Low", "Critical", "Optional"]
for name in priority_names:
    Priority.objects.get_or_create(name=name)

# ---- 2. Ensure Categories exist ----
category_names = ["Work", "School", "Personal", "Finance", "Projects"]
for name in category_names:
    Category.objects.get_or_create(name=name)

# ---- 3. Load existing priorities and categories ----
priorities = list(Priority.objects.all())
categories = list(Category.objects.all())

# ---- 4. Generate 100 tasks ----
for _ in range(100):
    task = Task.objects.create(
        title=fake.sentence(nb_words=5),
        description=fake.paragraph(nb_sentences=3),
        status=random.choice(["Pending", "In Progress", "Completed"]),
        deadline=timezone.make_aware(fake.date_time_this_month()),
        priority=random.choice(priorities),
        category=random.choice(categories)
    )

    # ---- 5. Generate 1–5 subtasks per task ----
    for _ in range(random.randint(1, 5)):
        SubTask.objects.create(
            task=task,
            title=fake.sentence(nb_words=3),
            status=random.choice(["Pending", "In Progress", "Completed"])
        )

    # ---- 6. Generate 1–3 notes per task ----
    for _ in range(random.randint(1, 3)):
        Note.objects.create(
            task=task,
            content=fake.paragraph(nb_sentences=2)
        )

print("Seeding complete!")