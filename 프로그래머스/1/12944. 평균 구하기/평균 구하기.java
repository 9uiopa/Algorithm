class Solution {
    public double solution(int[] arr) {
        double sum = 0;
        int len = arr.length;
        for (int num : arr){
            sum+= num;
        }
        return sum/len;
    }
}