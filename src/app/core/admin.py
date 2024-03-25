from sqladmin import Admin, ModelView

from app.infra.db.models.theme import Theme
from app.infra.db.models.post import Post


class PostAdmin(ModelView, model=Post):
    column_list = [Post.title]


class ThemeAdmin(ModelView, model=Theme):
    column_list = [Theme.title]


admin_list = [PostAdmin, ThemeAdmin]


def register_admin_panel(admin: Admin) -> None:
    for admin_view in admin_list:
        admin.add_view(admin_view)
