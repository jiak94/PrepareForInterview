class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        names = ["Billion", "Million", "Thousand", ""]
        neg = False
        if num < 0:
            neg = True
            num *= -1

        if num == 0:
            return "Zero"

        num = str(num)
        if len(num) % 3 != 0:
            num = "0" * (3 - len(num) % 3) + num

        i = len(num)
        j = 3
        res = list()
        while i > 0:
            tmp = num[i - 3:i]
            ret_val = self.num2Word(tmp)
            if len(ret_val) != 0:
                ret_val.append(names[j])
            res = ret_val + res
            i -= 3
            j -= 1

        if neg:
            return "Negative " + res
        ret =  " ".join(res)
        return ret.strip()

    def num2Word(self, num):
        ones = {
            "1": "One",
            "2": "Two",
            "3": "Three",
            "4": "Four",
            "5": "Five",
            "6": "Six",
            "7": "Seven",
            "8": "Eight",
            "9": "Nine"
        }
        tenth = {
            "10": "Ten",
            "11": "Eleven",
            "12": "Twelve",
            "13": "Thirteen",
            "14": "Fourteen",
            "15": "Fifteen",
            "16": "Sixteen",
            "17": "Seventeen",
            "18": "Eighteen",
            "19": "Nineteen",
            "2": "Twenty",
            "3": "Thirty",
            "4": "Forty",
            "5": "Fifty",
            "6": "Sixty",
            "7": "Seventy",
            "8": "Eighty",
            "9": "Ninety",
            "0": ""
        }
        res = list()
        for i in range(3):
            if num[i] == "0":
                continue
            elif i == 0:
                res.append(ones[num[i]])
                res.append("Hundred")
            elif i == 1 and num[i] == "1":
                res.append(tenth[num[i:]])
                return res
            elif i == 1:
                res.append(tenth[num[i]])
            else:
                res.append(ones[num[i]])
        return res