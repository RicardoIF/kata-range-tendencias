VALID_SYMBOLS = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "(", ")", "[", "]", " ", ",", "-"}

class Range: 
    raw_endpoints = None
    endpoints = None
    limit_symbols = None
    allpoints = None

    def __init__(self, entered_range: str) -> None:
        entered_range = entered_range.strip()
        if not (all(range_symbol in VALID_SYMBOLS for range_symbol in entered_range)):
            raise SyntaxError("Invalid range")
        
