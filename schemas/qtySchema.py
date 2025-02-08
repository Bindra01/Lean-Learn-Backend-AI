from pydantic import BaseModel

class qtySchema(BaseModel):
    qty_name: str
    qty_symbol: str
