
class Solution:
    def singleNumber(self, nums: List[int]):
        d = {}
        for num in nums:
            d[num] = d.get(num,0) + 1
        for key in d:
            if d[key] == 1:
                return key




int singleNumber(int A[], int n) {  #XOR commutative operative (0 or 0 or 5) = 56
    int result = 0;
    for (int i = 0; i<n; i++)
    {
		result ^=A[i];
    }
	return result;
}
