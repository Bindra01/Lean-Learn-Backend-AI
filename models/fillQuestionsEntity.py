def fillquestionEntity(item):
    used_value = item.get('used', False)  # Default False if not present
    if isinstance(used_value, str):
        used_value = used_value.lower() == 'true'
    return {
        "id": str(item.get("_id", "")),
        'question': item.get("question", ""),
        "choices": item.get("choices", []),
        'answer': item.get('answer', ""),
        'used': bool(used_value)  # Added used field
    }

def fillquestionEntitys(items):
    return [fillquestionEntity(item) for item in items]