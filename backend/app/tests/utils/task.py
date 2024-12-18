import datetime as datetime
import random
import uuid

from sqlmodel import Session

from app import crud
from app.models import Task, TaskCreate
from app.tests.utils.user import create_random_user
from app.tests.utils.utils import (
    random_lower_string,  # Code from david imports own method, not sure if necessary ?
)


def create_random_task(db: Session) -> Task:
    title = random_lower_string()
    description = random_lower_string()
    priority_id = random.randint(
        1, 10
    )  # Debated making a function for this, used as a one off though
    duration = random.randint(1, 100)  # This is just an int, no sure how large it gets
    year = random.randint(2024, 9999)
    month = random.randint(1, 12)
    day = random.randint(
        1, 29
    )  # not going higher as random chance of tests failing due to days in months, ie 30th of Feb errors
    due = datetime.datetime(year, month, day)
    task_id = uuid.uuid4()
    owner_id = create_random_user(db).id
    item_in = TaskCreate(
        title=title,
        description=description,
        priority_id=priority_id,
        duration=duration,
        due=due,
    )
    return crud.create_task(session=db, task_in=item_in, owner_id=owner_id)
