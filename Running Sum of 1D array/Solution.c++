class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        if (nums.size() < 1 || nums.size() > 1000) {
            throw invalid_argument("nums length must be between 1 and 1000");
        }
        vector<int> runningSums(nums.size());
        int sum = 0;
        for(int i = 0; i < nums.size(); i++){
            if (nums[i] < -1000000 || nums[i] > 1000000) {
                throw invalid_argument("nums values must be between -10^6 and 10^6");
            }
            sum += nums[i];
            runningSums[i] = sum;
        }
        return runningSums;
    }
};