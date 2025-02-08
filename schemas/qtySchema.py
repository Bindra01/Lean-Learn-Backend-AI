from pydantic import BaseModel

class qtySchema(BaseModel):
    id: str
    qty_name: str
    qty_symbol: str
