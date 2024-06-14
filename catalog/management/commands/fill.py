from django.core.management import BaseCommand

from catalog.function.work_with_file import open_fixture
from catalog.models import Category, Product
from blog.models import Blog
from users.models import User


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        file = open_fixture('catalog.json')
        list_categories = [item.get("fields") for item in file if item.get("model") == "catalog.category"]
        return list_categories

    @staticmethod
    def json_read_products():
        file = open_fixture('catalog.json')
        list_products = [item.get("fields") for item in file if item.get("model") == "catalog.product"]
        return list_products

    @staticmethod
    def json_read_blog():
        file = open_fixture('blog.json')
        list_blogs = [item.get("fields") for item in file]
        return list_blogs

    @staticmethod
    def json_read_users():
        file = open_fixture('users.json')
        list_users = [item.get("fields") for item in file]
        return list_users

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()
        User.objects.all().delete()
        Blog.objects.all().delete()
        print(self.json_read_users())

        category_for_create = [Category(**item) for item in self.json_read_categories()]
        users_for_create = [User(**item) for item in self.json_read_users()]
        blog_for_create = [Blog(**item) for item in self.json_read_blog()]
        product_for_create = []

        Category.objects.bulk_create(category_for_create)
        User.objects.bulk_create(users_for_create)
        Blog.objects.bulk_create(blog_for_create)

        for product in Command.json_read_products():
            product_for_create.append(
                Product(name=product.get("name"),
                        description=product.get("description"),
                        category=Category.objects.get(pk=product.get("category") + 3),
                        photo=product.get("photo"),
                        price=product.get("price"),
                        created_at=product.get("created_at"),
                        updated_at=product.get("updated_at"),
                        owner=product.get("owner"),
                        is_published=product.get("is_published"))
            )

        Product.objects.bulk_create(product_for_create)
