from fastapi import APIRouter,Depends,HTTPException,status,Request

from fastapi_jwt_auth import AuthJWT

from database import SessionLocal,engine

from auth import db_dependency,get_current_user

from models import User,Order

from schemas import order,Signup

order_router = APIRouter(
    
    prefix="/order",
    tags=["order"]

) 


@order_router.post('/order',status_code=status.HTTP_201_CREATED)
async def place_an_order(db:db_dependency,order:order, current_user:User=Depends(get_current_user)):

    new_order=Order(

        user_id=current_user.get('id'),

        p_name=order.p_name,
    
        quantity=order.quantity
    )

    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order

    

# @order_router.get('/orders/{id}')
# async def get_order_by_id(db:db_dependency, id:int,current_user:User=Depends(get_current_user)):

#     order_by_id=db.query(Order).filter(Order.id==id).first()

#     if order_by_id is None:
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No order with such id")
    
#     return {f"order_by_id": order_by_id}
    


# @order_router.get('/user/orders')
# async def list_all_orders(db:db_dependency,):



#     # user=db.query(User).filter(User.id==current_user.get('id')).first()

#     user_order=db.query(Order).all()

#     return {f"user_order": user_order}


@order_router.get('user/order')
async def get_a_user_order(db:db_dependency,current_user:User=Depends(get_current_user)):


    user=db.query(Order).filter(Order.user_id==current_user.get('id')).first()

    return {f"user": user}



@order_router.get('user/orders')
async def get_all_user_order(db:db_dependency,current_user:User=Depends(get_current_user)):


    user=db.query(Order).filter(Order.user_id==current_user.get('id')).all()

    return {f"user": user}

    
@order_router.put('user/order/update')
async def update_an_order(db:db_dependency,id:int,order:order,current_user:User=Depends(get_current_user)):

    order_to_update=db.query(Order).filter(Order.id==id).first()

    order_to_update.quantity=order.quantity

    db.commit()

    
    return { f" order with id {id} is updated successfully"}


@order_router.delete('/order/delete/{id}')
async def delete_an_order(db:db_dependency,id:int,current_user:User=Depends(get_current_user)):

     
    order_to_delete=db.query(Order).filter(Order.id==id).first()

    db.delete(order_to_delete)
    db.commit()
    return { 'order_to_delete': order_to_delete}


