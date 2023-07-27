from pathlib import Path

from encryption_machine.settings import *

BASE_DIR = Path(__file__).resolve().parent.parent
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
