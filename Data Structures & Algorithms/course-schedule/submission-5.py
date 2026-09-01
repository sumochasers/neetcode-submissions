class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        
        '''
        [0,1],[1,2][2,3]

        0 1
        1 2
        2 3

        0 -> 1 ->2 ->3 no cycle

        0 1
        1 0

        0 -> 1 -> 0 cycle -

        maintain visited nodes(here it is course num) in set

        construct dict for in-degree mapping
        for each course do dfs to check if there are any cycles

        '''

        indegree_dict = {i :[] for i in range(numCourses)}
        
        for req in prerequisites :
            indegree_dict[req[0]].append(req[1])
        
        print(indegree_dict)

        def dfs( course, dependencies_set):

            if  len(indegree_dict[course]) == 0  :
                return True
            
            if course in dependencies_set :
                return False
            
            for each_c in indegree_dict[course] :
                dependencies_set.add(course)
                if dfs(each_c,dependencies_set) == False :
                    return False
            
            indegree_dict[course] = []
            return True

        for i in range(0,numCourses):
            dependencies_set = set();
            status = dfs(i,dependencies_set)
            print(status)
            if status == False :
                return False

        return True   


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        '''
        preMap = { i : [] for i in range(numCourses)} 

        for crs,prereq in prerequisites :
            preMap[crs].append(prereq)
            
        print(preMap)

        visiting = set()
        def dfs(crs):

            if  crs in visiting :
                return False

            if preMap[crs] == [] :
                return True
            
            visiting.add(crs)
            for pre in  preMap[crs]:
                if not dfs(pre):
                    return False      
            visiting.remove(crs)
            #performance
            preMap[crs] = []
            
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True  '''              




        
        