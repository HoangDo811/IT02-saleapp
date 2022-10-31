from sqlalchemy import Column, Integer, String, Float, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from saleapp import db, app

class BaseModel(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)

class Category(BaseModel):
    __tablename__ = 'category'

    name = Column(String(50), nullable=False)
    products = relationship('Product', backref='category', lazy=True)

class Product(BaseModel):
    name = Column(String(50), nullable=False)
    description = Column(String(50))
    price = Column(Float, default=0)
    image = Column(String(500))
    active = Column(Boolean,default=True)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)


if __name__ == '__main__':
    with app.app_context():
        #c1 = Category(name='Điện thoại')
        #c2 = Category(name='Máy tính bảng')
        #c3 = Category(name='Phụ kiện')

        #db.session.add_all([c1,c2,c3])
        #db.session.commit()
        p1 = Product(name='iPhone 7 Plus', description='Apple, 32GB, RAM: 3GB, iOS13', price=17000000,
                     image="https://cdn.tgdd.vn/Products/Images/42/78124/iphone-7-plus-gold.png", category_id=1)
        p2 = Product(name='iPad Pro 2020', description='Apple, 128GB, RAM: 6GB', price=37000000,
                     image="https://cdn.tgdd.vn/Products/Images/522/221775/ipad-pro-12-9-inch-wifi-128gb-2020-xam-400x460-1-400x460.png", category_id=2)
        p3 = Product(name='Galaxy Note 10 Plus', description='Samsung, 64GB, RAML: 6GB', price=24000000,
                     image='https://cdn.tgdd.vn/Products/Images/522/221775/ipad-pro-12-9-inch-wifi-128gb-2020-xam-400x460-1-400x460.png', category_id=1)
        p4 = Product(name='AirPod Pro 2', description='Apple, Inear, Superbass', price=5000000,
                     image='https://didongviet.vn/pub/media/catalog/product//a/i/airpods-pro-2-2022-didongviet.jpg', category_id=3)

        db.session.add_all([p1, p2, p3, p4])
        db.session.commit()
        #db.create_all();

