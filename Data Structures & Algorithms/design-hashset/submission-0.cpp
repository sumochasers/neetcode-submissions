class MyHashSet {
private:
    vector<int> set;
public:
    MyHashSet() {
        
    }
    
    void add(int key) {
        if(!contains(key)){
            set.push_back(key);
        }
    }
    
    void remove(int key) {
        
        auto it = find(set.begin(),set.end(),key);
        if (it != set.end()){
            set.erase(it);
        }     
    }
    
    bool contains(int key) {
        auto it = find(set.begin(),set.end(),key);
        if (it != set.end()){
            return true;
        }
        return false;
    }
};

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet* obj = new MyHashSet();
 * obj->add(key);
 * obj->remove(key);
 * bool param_3 = obj->contains(key);
 */