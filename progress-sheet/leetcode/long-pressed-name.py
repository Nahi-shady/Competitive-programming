class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        name_idx = 0
        typed_idx = 0
        while name_idx <= len(name) and typed_idx < len(typed):
            if name_idx < len(name) and typed[typed_idx] == name[name_idx]:
                typed_idx += 1
                name_idx += 1
            elif typed[typed_idx] == name[name_idx-1] and name_idx != 0:
                typed_idx += 1
            else:
                return False
            
        return name_idx == len(name) and typed_idx == len(typed)
        