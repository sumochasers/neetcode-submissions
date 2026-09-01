class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        
        // Swaping val to the end 
        
        // int left = 0;
        // int right = nums.size()-1;

        // while(left <= right){

        //     while(nums[left] != val && left <= right){
        //         left++;
        //     }
        //     while(nums[right] == val && left <= right ){
        //         right--;
        //     }
            
        //     if(left <= right ){
        //         int temp = nums[left];
        //         nums[left] = nums[right];
        //         nums[right] = temp;
        //         left++;
        //         right--;
        //     }
        // }
        
        // return right+1;
        
        // better way 
        int left = 0;
        for (int right = 0 ; right < nums.size() ; right++){
            if (nums[right] != val){
                nums[left] = nums[right];
                left++;
            }
        }
        return left;
    }
};