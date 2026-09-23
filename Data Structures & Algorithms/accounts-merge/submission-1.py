class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        parent : dict [str, str] = {}
        def find(node : str) -> str :
            
            parent.setdefault(node, node)
            if parent[node] != node :
                parent[node] = find(parent[node])
            
            return parent[node]
        
        def union(node1 : str, node2 : str) -> None :
            root_a = find(node1)
            root_b = find(node2)

            if root_a != root_b :
                parent[root_b] = root_a
              
        
        # each email create node to name mapping and union with the other components
        name_by_email : dict[str, str] = {}
        
        for account in accounts :
            name = account[0]
            parent_email = account[1]
            for email in account[1:] :
                name_by_email[email] = name
                union(parent_email, email)
       
        # for each email group component
        components : dict[str, list[int]] = defaultdict(list)
        for email in name_by_email :
            parent_email = find(email)
            components[parent_email].append(email)
        
        # for each component draft response
        result = []
        for root, emails in components.items() :
            name = name_by_email[root]
            result.append([name] + sorted(emails))

        return result        


        

        
