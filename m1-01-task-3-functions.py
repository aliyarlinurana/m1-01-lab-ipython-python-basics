def to_float(a):
    try:
        return float(a)
    except (ValueError, TypeError):
        return None

def clean(a):
    return str(a).strip().lower()

test= ["IronHACK", " 2006 ", "data", "   ","  20.33  "]

for item in test:
    cleaned_text = clean(item)
    float_value = to_float(cleaned_text)
    
    print("Input: ", item, " Clean: ", cleaned_text, " Float: ", float_value)