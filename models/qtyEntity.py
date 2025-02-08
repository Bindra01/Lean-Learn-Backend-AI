
def qtyEntity(item):
    return {
        "id": str(item.get("_id", "")),
        "qty_name":str(item.get("qty_name","")),
        "qty_symbol":str(item.get("qty_symbol",""))
    }

def qtyEntitys(items):
    return [qtyEntity(item) for item in items]