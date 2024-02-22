class Solution:
    def simplifyPath(self, path: str) -> str:
        split = path.split('/')
        stack = []
        for s in split:
            if s == '..' and stack:
                stack.pop()
            elif s not in ['', '.', '..']:
                stack.append(s)

        return '/' + '/'.join(stack)