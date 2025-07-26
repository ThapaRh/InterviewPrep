class Solution:
    def numberToWords(self, num: int) -> str:
        '''
        
        Input: num = 12345/1000 345
        Output: "Twelve Thousand Three Hundred Forty Five"  
        12345/10000 = 345
        345/100 =45
        345//100 = 
        3 hundred
        if 45 in dict:
        string = dict[45]+string
        else:
        45/
        Five
        
        0*1000
        
        
        1234/10
        4*10
        Fourty
        
        123/10
        3*100
        if >10:
        3=Three 100=Hundred
        
        12/10
        
        222000222
        222
        000
        222
        
        Shit question lol
        TC: O(log10N)
        SC: O(1) cause dict is constant space
        '''
        dict={1:"One",
            2:"Two",
            3:"Three",
            4:"Four",
              5:"Five",
              6:"Six",
              7:"Seven",
              8:"Eight",
              9:"Nine",
              10:"Ten",
              11:"Eleven",
              12:"Twelve",
              13:"Thirteen",
              14:"Fourteen",
              15:"Fifteen",
              16:"Sixteen",
              17:"Seventeen",
              18:"Eighteen",
              19:"Nineteen",
            20:"Twenty",
              30:"Thirty",
              40:"Forty",
              50:"Fifty",
              60:"Sixty",
              70:"Seventy",
              80:"Eighty",
              90:"Ninety",
            100:"Hundred",
            1000:"Thousand",
            1000000:"Million",
            1000000000:"Billion",
            1000000000000:"Trillion"}
        if num == 0:
            return "Zero"
        final = "" # two million two hundred twenty two 
        i = 0
        while(num):
            hundreds = num%1000 #222 000 #222
            num = num//1000 #222000 #222 #0
            if (hundreds):
                power = 1000**i #1000000000
                if power>1 and power in dict:
                    final = dict[power] + " " + final
                tens = hundreds%100 #2
                hund = hundreds//100 #0
                if tens in dict:
                    final = dict[tens] + " " + final
                else:
                    ones = tens%10 #2
                    t = tens-ones #20
                    if ones in dict:
                        final = dict[ones] + " " + final 
                    if t in dict:
                        final = dict[t] + " " + final
                if hund and hund in dict:
                    final = dict[100] + " " + final
                    final = dict[hund] + " " + final
            i+=1
        return final.strip()