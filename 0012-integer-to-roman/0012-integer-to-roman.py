class Solution:
    def intToRoman(self, num: int) -> str:
        
        chars = {
                    1        : "I", 
                    4        : "IV",
                    5        : "V",
                    9        :  "IX",
                    10       :  "X",
                    40       :  "XL",
                    50       :  "L",   
                    90       :  "XC",
                    100      :  "C", 
                    400      :  "CD",
                    500      :  "D", 
                    900      :  "CM",
                    1000     :  "M"        
        }
        if num in chars:
            return chars[num]
        
        order = sorted(chars.keys(), reverse = True);
        
        ans = []
        
        for x in order:
            n = num//x
            ans.append(chars[x]*n)
            num = num%x
        
        return "".join(ans)
            