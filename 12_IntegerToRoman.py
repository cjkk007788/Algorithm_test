class Solution1:
    def intToRoman(self, num: int) -> str:

        roman = [
            {1:'I',4:'IV',5:'V',9:'IX'},
            {1:'X',4:'XL',5:'L',9:'XC'},
            {1:'C',4:'CD',5:'D',9:'CM'},
            {1:'M'}
        ]


        result = ""

        for power in range(3,-1,-1):
            digit = num // 10**power %10
            if digit == 0:
                continue
            r = roman[power]
            if digit in (4,9):
                result += r[digit]
            elif digit>=5:
                result = result + r[5] + r[1] * (digit-5)
            else:
                result = result + r[1]*digit
        return result

class Solution2:
    def intToRoman(self,num:int)->str:
        table = [["","M","MM","MMM"],
                ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"],
                ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"],
                ["","I","II","III","IV","V","VI",'VII','VIII','IX'],
                ]

        return table[0][num//1000] + table[1][num//100 %10] + table[2][num//10%10] + table[3][num%10]


class Soultion3:
    def intToRoman(self,num:int) -> str:
        pairs = [
            (1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),
            (100,'C'),(90,'XC'),(50,'L'),
            (40,'XL'),
            (10,"X"),
            (9,'IX'),
            (5,'V'),
            (4,'IV'),
            (1,'I')
        ]

        result = ""
        for number , rn in pairs :

            count, num = divmod(num, number)
            result = result + rn * count
        return result
