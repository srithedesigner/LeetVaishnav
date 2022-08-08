class SegmentTree:

    def __init__(self, nums):
        self.nums = nums
        self.tree = defaultdict()
        self.n = len(nums)

        def build(node, left, right):

            if left == right:
                #print(len(self.tree), node)

                self.tree[node] = self.nums[left]

            else:

                mid = left + (right - left) // 2

                build(2 * node, left, mid)
                build(2 * node + 1, mid + 1, right)

                self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

        build(1, 0, self.n - 1)

    def update(self, ind, val):

        diff = self.nums[ind] - val
        self.nums[ind] = val

        def find(node, left, right):

            if left == right and left == ind:
                return node

            if left > ind or right < ind:
                return None

            else:

                mid = left + (right - left) // 2

                X = find(2 * node, left, mid)
                y = find(2 * node + 1, mid + 1, right)

                if X is None:
                    return y
                return X

         
        x = find(1, 0, self.n - 1)

        while x >= 1:
             
            self.tree[x] -= diff
            x = x // 2
         

    def query(self, start, end):

        def recursion(node, left, right):

            if right < start or left > end:
                return 0

            if start <= left and end >= right:
                return self.tree[node]

            mid = left + (right - left) // 2

            return recursion(node * 2, left, mid) + recursion(node * 2 + 1, mid + 1, right)

        return recursion(1, 0, self.n - 1)




class NumArray:

    def __init__(self, nums: List[int]):
        
        self.stree = SegmentTree(nums)
        
        #print(len(self.stree.tree))
        

    def update(self, index: int, val: int) -> None:
        self.stree.update(index, val)
        

    def sumRange(self, left: int, right: int) -> int:
        
        return self.stree.query(left, right)
        

 