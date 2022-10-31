from saleapp.models import Category, Product


def load_categories():
   return Category.query.all()


def load_products(category_id=None, kw=None, pr=None):
    query = Product.query.filter(Product.active.__eq__(True))

    if category_id:
        query = query.filter(Product.category_id.__eq__(category_id))

    if kw:
        query = query.filter(Product.name.contains(kw))

    #if pr:
    #    query = query.filter(Product.price.contains(pr))

    return query.all()
