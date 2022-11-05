class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:

    def __init__(self,total_words):
        self.root = TrieNode()
        self.unfound_words = total_words
        

    def insert(self, word: str) -> None:
        cur = self.root
        
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            
        cur.endOfWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        res = []
        M , N = len(board) , len(board[0])
        d = Trie(len(words))                                    
        
        for w in words:                                         #build Trie
            d.insert(w)
        
        def go(r,c,s,cur_node):   
            if cur_node.endOfWord:
                res.append(s)
                cur_node.endOfWord = False                      # To avoid duplicates in res 
                d.unfound_words -= 1

            if d.unfound_words == 0:
                return

            if r < 0 or c < 0 or r >= M or c >= N:
                return 
            
            cur_chr = board[r][c] 
            if cur_chr not in cur_node.children:
                return                                          # No Such Prefix in WORDS
            
            cur_root = cur_node
            cur_node = cur_node.children[cur_chr]               #prefix exists in trie ... cur node points to this prefix
            
            
            board[r][c] = '69'
            go(r+1,c,s+cur_chr,cur_node) 
            go(r-1,c,s+cur_chr,cur_node) 
            go(r,c-1,s+cur_chr,cur_node) 
            go(r,c+1,s+cur_chr,cur_node) 
            board[r][c] = cur_chr
            
            if not cur_node.children:
                del cur_root.children[cur_chr]                  # Pruning the trie ... TLE's otherwise
																# if current node has no children and this path has been explored...then this child is useless 
																# delete child to never visit again and save time.
            return
            
        
        root = d.root
        for i in range(M):
            for j in range(N):
                if d.unfound_words == 0:
                    return res
                go(i,j,"",root)
                
        return res
    