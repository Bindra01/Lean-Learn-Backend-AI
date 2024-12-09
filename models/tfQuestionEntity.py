
def tfEntity(item):
    used_value = item.get('used', False)  # Default False if not present
    if isinstance(used_value, str):
        used_value = used_value.lower() == 'true'
    return {
        "id": str(item.get("_id", "")),
        'question': item.get("question", ""),
        'answer': item.get('answer', ""),
        'used': bool(item.get('used', False))  # Added used field
    }

def tfEntitys(items):
    return [tfEntity(item) for item in items]