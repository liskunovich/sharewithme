from fastapi import FastAPI
from sqladmin import Admin

from app.core.admin import register_admin_panel
from app.core.db import engine


def start_application():
    app = FastAPI()
    admin = Admin(app, engine)
    return app, admin


app, admin = start_application()
register_admin_panel(admin)
