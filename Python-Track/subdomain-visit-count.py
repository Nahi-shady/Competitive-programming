class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        c = defaultdict(int)
        for i in cpdomains:
            sep = i.split()
            subdomains = sep[1].split(".")
            # print(sep, subdomains)
            for indx in range(len(subdomains)):
                domain = '.'.join(subdomains[indx:])
                c[domain] += int(sep[0])
    
        return [f'{count} {dom}' for dom, count in c.items()]