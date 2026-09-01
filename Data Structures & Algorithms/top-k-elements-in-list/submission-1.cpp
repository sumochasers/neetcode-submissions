class is_max {
public :
    
    bool operator() (std::pair<int,int> p1, std::pair<int,int> p2){
        if(p1.first > p2.first){
            return true;
        }
        return false;
    }
};

class Solution {

public:
    
    vector<int> topKFrequent(vector<int>& nums, int k) {

        std::unordered_map<int, int> freq;
        for (const int& num : nums){
            freq[num] = 1+freq[num];
        }
        

        std::priority_queue<std::pair<int,int>, vector<std::pair<int,int>>, is_max> pq;
        
        for(auto pair : freq){
            pq.push(std::make_pair(pair.second, pair.first));
            if(pq.size() > k){
                pq.pop();
            }
        }

        std::vector<int> result;
        while(!pq.empty()){
            int number = pq.top().second;
            result.push_back(number);
            pq.pop();
        }
        return result;
        
    }
};
