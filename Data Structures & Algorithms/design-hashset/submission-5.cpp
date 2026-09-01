class LinkedList{
public:    
    
    LinkedList(int value):value(value), next(nullptr){}
    int value;
    LinkedList* next;
};

class MyHashSet {
private:
    static const int HASH_RANGE = 10000;
    vector<LinkedList* > set;
   

    int get_hash(int number){
        return number % HASH_RANGE;
    }
public:
    MyHashSet() {
        set.resize(HASH_RANGE);
        for (auto& bucket : set) {
            bucket = new LinkedList(0);
        }
    }
    
    void add(int key) {
        // if(!contains(key)){
        //     set.push_back(key);
        // }
        
        //----------- Optimized
        auto node = set[get_hash(key)];
        while(node->next){
            if(node->next->value == key){
                return;
            }
            node = node->next;
        }
        node->next = new LinkedList(key);
    }
    
    void remove(int key) {
        
        // auto it = find(set.begin(),set.end(),key);
        // if (it != set.end()){
        //     set.erase(it);
        // }
        
        //----------- Optimized
        
        LinkedList* node = set[get_hash(key)];
        
        while(node->next){
            if(node->next->value == key){
                LinkedList* temp = node->next;
                node->next = temp->next;
                delete temp;
                return;
            }
            node = node->next;
        }
    }
    
    bool contains(int key) {
        // auto it = find(set.begin(),set.end(),key);
        // if (it != set.end()){
        //     return true;
        // }
        // return false;

        //----------- Optimized
        LinkedList* node = set[get_hash(key)];
        while( node->next ){
            
            if(node->next->value == key){
                return true;
            }
            node = node->next;
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