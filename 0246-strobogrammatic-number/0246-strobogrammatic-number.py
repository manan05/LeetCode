
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        new_num = []
        for i in num:
            if i in ['2', '3', '4', '5','7']:
                return False
            elif(i in ['0', '1', '8']):
                new_num.append(i)
            else:
                if(i == '6'):
                    new_num.append('9')
                else:
                    new_num.append('6')
        number = ''.join(new_num[::-1])
        print(number)
        return number == num