class Solution {
public:
    
    void swap(int left, int right, vector<int>& nums){
        int temp = nums[left];
        nums[left] = nums[right];
        nums[right] = temp;
    }
    
    int partition(int start, int end, vector<int>& nums){
        int left = start-1;
        int pivot_value = nums[end];
        for(int right=start ; right < end; right++){
            if(nums[right] < pivot_value){
                left++;
                swap(left, right, nums);
            }
        }
        left++;
        swap(left, end, nums);
        return left;
    }
    
    void quick_sort(int start, int end, vector<int>& nums){
        if (start < end){
            int pivot = partition(start, end, nums);
            quick_sort(start, pivot-1, nums);
            quick_sort(pivot+1, end, nums);
        }        
    } 
    
    void sortColors(vector<int>& nums) {
        // Quick sort can be applied but there are better ways since it has only 3 colors
        quick_sort(0, nums.size()-1, nums);
    }
};