class Solution:
    def smallestNumber(self, num: int) -> int:
        
        store = sorted(str(num))
        if num < 0:
            return -int(''.join(store[1:])[::-1])

        if store[0] == '0':
            count = 0
            for i in range(len(store)):
                if store[i] == '0':
                    count += 1
                else:
                    break
            store = [store[i]] + ['0']*count + store[i+1:]
            
        return int(''.join(store))