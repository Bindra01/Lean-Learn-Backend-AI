from fastapi import APIRouter, status
from services.qtyService import get_all_qty,Create_qty
from schemas.qtySchema import qtySchema as qtySchema

router = APIRouter(
    prefix="/qty",
    tags=["qty"]
)

@router.get("/" ,status_code=status.HTTP_200_OK, response_model=list[qtySchema])
def get_all():
    return get_all_qty()

@router.post("/" ,status_code=status.HTTP_200_OK)
def create_qty(qtySchema: qtySchema):
    return Create_qty(qtySchema)
