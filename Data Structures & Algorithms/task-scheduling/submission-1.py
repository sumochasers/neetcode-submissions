'''
x x y y 
x-2 
y-2
yxy-x

A A A B C
A-3 - 2
B-1
C-1

ABC-A---A
BCA---A---A
'''
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Brute force
        # Maintain pair of tasks and frequencies
        # Maintain window of processed elements
        # Find max until pair is not empty
        #   if window has next element -> add dummy cycle -1
        # Count all the cycles
        
        freq_by_task = Counter(tasks)
        #print(freq_by_task)
        cycles = 0
        window = []
        while freq_by_task :
            
            max_task = -1
            max_freq = -1
            
            # Find max_task
            for task,freq in freq_by_task.items() :
                
                # Ignore if task in  hot_window
                hot_window = False
                
                for i in range( max(0,cycles-n),cycles) :
                    if window[i] == -1 :
                        continue
                    if window[i] == task :
                        hot_window = True
                        break
                
                if hot_window :
                    continue
                
                 # Set Max - If not in window
                if freq > max_freq :
                    max_task = task
                    max_freq = freq
                
            if max_freq != -1 :
                freq_by_task[max_task] -= 1
                if freq_by_task[max_task] == 0 :
                    freq_by_task.pop(max_task)
                
            window.append(max_task)
            cycles += 1
        
        return cycles

            
            



         
        
        
       




        