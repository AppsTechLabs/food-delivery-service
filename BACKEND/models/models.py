from database import Base

from sqlalchemy import Column, String, Integer, Boolean,ForeignKey,Float

from sqlalchemy.orm import relationship

from sqlalchemy_utils.types import ChoiceType

class User(Base):

    __tablename__ = 'user'

    id=Column(Integer, primary_key=True,index=True)
    Username=Column(String(25), unique=True)
    email=Column(String(80), unique=True)
    password=Column(String)
    is_staff=Column(Boolean,default=False)
    is_active=Column(Boolean,default=True)
    orders=relationship('Order', back_populates='user')
    
    def __repr__(self):
        return f"<User {self.Username}"
    
class Order(Base):

    ORDER_STATUSES=(

        ('PENDING', 'pending'),
        ('IN-TRANSIT', 'in-transit'),
        ('DELIVERED', 'delivered'),

    )

    
    __tablename__ = 'orders'

    id=Column(Integer, primary_key=True, index=True)
    quantity=Column(Integer,nullable=False)
    order_status=Column(ChoiceType(choices=ORDER_STATUSES), default="PENDING") 
    user_id=Column(Integer,ForeignKey('user.id'))
    p_name=Column(String, ForeignKey('product.name'))
    user=relationship('User', back_populates='orders')

    product=relationship('Product', back_populates='order')

    def __repr__(self):
        return f"<Order {self.id}"
 

class Product(Base):

    __tablename__ = 'product'

    id=Column(Integer, primary_key=True, index=True)
    name=Column(String(25), unique=True)
    price=Column(Float, nullable=False)
    description=Column(String(255), nullable=False)
    category=Column(String(255), nullable=False)
    order=relationship('Order', back_populates='product')


    def __repr__(self):
        return f"<Product {self.id}"
        
