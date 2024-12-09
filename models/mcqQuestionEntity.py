def mcqEntity(item):
    # Convert used field to boolean
    used_value = item.get('used', False)  # Default False if not present
    if isinstance(used_value, str):
        used_value = used_value.lower() == 'true'
    
    return {
        "id": str(item.get("_id", "")),
        'question': item.get("question", ""),
        'options': item.get('options', []),
        'answers': item.get('answers', []),
        'used': bool(used_value)# Convert to boolean
    }

def mcqEntitys(items):
    return [mcqEntity(item) for item in items]