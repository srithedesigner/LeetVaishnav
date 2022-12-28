class Solution {
    fun minStoneSum(piles: IntArray, k: Int): Int {
        
        val pilesOfStones: PriorityQueue<Int> = PriorityQueue<Int>({
            i1: Int, i2 : Int -> i2 - i1
        });
        
        for(item in piles) {
            pilesOfStones.add(item)
        }
        
        for(i in 0..k-1) {
            pilesOfStones.add(pilesOfStones.peek() - pilesOfStones.peek()/2)
            pilesOfStones.remove()
        }
        
        var ans: Int = 0;
        
        while(!pilesOfStones.isEmpty()) {
            
            ans += pilesOfStones.peek();
            
            pilesOfStones.remove();
        }
        
        return ans;
        
    }
}