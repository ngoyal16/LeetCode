class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        
        domainVisitCount = {}
        
        for domainStr in cpdomains:
            domainStr = domainStr.split(" ")
            domainCount = domainStr[0]
            
            domainNameArr = domainStr[1].split(".")
            
            lenDomain = len(domainNameArr)
            for i in range(lenDomain):
                domainName = ".".join(domainNameArr[i:])
                
                if domainName in domainVisitCount:
                    domainVisitCount[domainName] += int(domainCount)
                else:
                    domainVisitCount[domainName] = int(domainCount)
                
        return map(lambda key: " ".join([str(domainVisitCount[key]), key]), domainVisitCount.keys())
