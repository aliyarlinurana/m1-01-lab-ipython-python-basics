def to_float(s):
    try:
        return float(s)
    except (ValueError, TypeError):
        return None

def clean(s):
    return str(s).strip().lower()

test_data = ["  42.5  ", "PYTHON", " 100 ", "alma123", "   "]

for item in test_data:
    cleaned_text = clean(item)
    float_value = to_float(cleaned_text)
    
    # Nəticəni "expression" şəklində göstərək
    print(f"Giriş: {repr(item):<10} | Təmiz: {repr(cleaned_text):<10} | Rəqəm: {float_value}")