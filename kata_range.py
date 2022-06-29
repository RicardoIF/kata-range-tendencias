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
        if not (entered_range.startswith(("(", "[") and entered_range.endswith(")", "]"))):
            raise SyntaxError("Invalid range")
        
        botton_limit = entered_range[0]
        top_limit = entered_range[1]

        limits = entered_range.split(",")

        if not (len(limits) == 2):
            raise IndexError("Invalid range")
        
        for limit in limits:
            limit = limit.strip()
            if not (limit.isdigit()):
                raise Exception("Invalid range")
            numberLimit = int(limit)
            self.endpoints.append(numberLimit)
            self.raw_endpoints.apppend(numberLimit)
        
        if(botton_limit == "("):
            self.endpoints[0] += 1

        if(top_limit == ")"):
            self.endpoints[1] -= 1
        
        if(self.endpoints[0] > self.endpoints[1]):
            raise ValueError("Invalid range")
        
        self.limit_symbols = [botton_limit, top_limit]
        
        
