def intToRoman(num: int) -> str:
    roman = ""
    i = num
    while i > 0:
        print(i)
        if i // 1000 > 0:
            numMs = i // 1000
            i = i % 1000
            roman = roman + (numMs * "M")
        elif i // 900 > 0:
            i = i % 900
            roman += "CM"
        elif i // 500 > 0:
            roman += "D"
            i = i % 500
        elif i // 400 > 0:
            roman +=  "CD"
            i = i % 400
        elif i // 100 > 0:
            numCs = i // 100
            i = i % 100
            roman += ("C" * numCs)
        elif i // 90 > 0:
            i = i % 90
            roman += "XC"
        elif i // 50 > 0:
            i = i % 50
            roman += "L"
        elif i // 40 > 0:
            i = i % 40
            roman += "XL"
        elif i // 10 > 0:
            numX = i // 10
            i = i % 10
            roman += (numX * "X")
        elif i == 9:
            i = 0
            roman += "IX"
        elif i // 5 > 0:
            roman += "V"
            i = i % 5
        elif i == 4:
            i = 0
            roman += "IV"
        else:
            roman += ("I" * i)
            i = 0
    return roman
    
    
print(intToRoman(3)) 