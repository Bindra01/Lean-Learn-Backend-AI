from models.qtyEntity import qtyEntity , qtyEntitys
from schemas.qtySchema import qtySchema
from database.database import qty_collection
from fastapi import status , HTTPException
from bson import ObjectId


def get_all_qty():
    items = qty_collection.find()
    if items is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="quantity not found")
    return qtyEntitys(items) 


def Create_qty(qtySchema: qtySchema):
    quantity = qty_collection.find_one({"qty_name": qtySchema.quantity})
    if quantity:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="quantity already exists")
    
    quantity_dict = qtySchema.model_dump()
    insterted_item = qty_collection.insert_one(quantity_dict)
    quantity_dict["_id"] = insterted_item.inserted_id
    return qtyEntity(quantity_dict)  

