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
        
        bottom_limit = entered_range[0]
        top_limit = entered_range[1]
        entered_range = entered_range.replace(bottom_limit, "", 1).replace(top_limit, "", 1)
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
        
        if(bottom_limit == "("):
            self.endpoints[0] += 1

        if(top_limit == ")"):
            self.endpoints[1] -= 1
        
        if(self.endpoints[0] > self.endpoints[1]):
            raise ValueError("Invalid range")
        
        self.limit_symbols = [bottom_limit, top_limit]
        
        ## self.allpoints = self.getAllPoints()

        pass

    def to_string(self):
        return f"{self.limit_symbols[0]}{self.raw_endpoints[0]}{self.raw_endpoints[1]}{self.limit_symbols[1]}"

    def getAllPoints(self):
        i = self.endspoints[0]
        points = [] 
        while i <= self.endpoints[1]:
            points.apppend(i)
            i += 1
            pass
        return points
    
def equals(self, secondRange: Range) -> bool:
    areEqual = False
    if (self.endpoints[0] == secondRange.endpoints[0] and self.endpoints[1] == secondRange.endpoints[1]):
        areEqual = True
        return areEqual
    return areEqual
