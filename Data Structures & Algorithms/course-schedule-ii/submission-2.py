class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        indegree_dict = {i :[] for i in range(numCourses)}
        
        for req in prerequisites :
            indegree_dict[req[0]].append(req[1])
        
        course_order = list()

        def dfs( course, dependencies_set):

            if  len(indegree_dict[course]) == 0  :
                if course not in course_order :
                    course_order.append(course)
                return True
            
            if course in dependencies_set :
                return False
            
            for each_c in indegree_dict[course] :
                dependencies_set.add(course)
                if dfs(each_c,dependencies_set) == False :
                    return False
            
            if course not in course_order :
                course_order.append(course)
            
            indegree_dict[course] = []
            return True

        for i in range(0,numCourses):
            dependencies_set = set();
            status = dfs(i,dependencies_set)
            if status == False :
                return []
        
        return course_order