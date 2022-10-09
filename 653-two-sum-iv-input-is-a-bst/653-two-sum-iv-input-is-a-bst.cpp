
class Solution {
public:
    bool findTarget(TreeNode* root, int k) {
        
        stack<TreeNode*> left;
        stack<TreeNode*> right;
        
        
        TreeNode* curr = root;
        
        while (curr)
        {
            left.push(curr);
            curr = curr->left;
        }
        
        curr = root;
        
        while(curr)
        {
            right.push(curr);
            curr = curr->right;
        } 
        
        while(!left.empty() and !right.empty())
        {
            TreeNode* x = left.top();
            TreeNode* y = right.top();
            
            //cout<<x->val << " " << y->val<<endl;
            
            
            
            if(x->val + y->val == k and x!=y)
                return true;
            
            if(x->val + y->val < k)
            {
                left.pop();
                TreeNode* rt = x->right;
                while(rt)
                {
                    left.push(rt);
                    rt = rt->left;
                }
                
            }
            
            else
            {
                right.pop();
                TreeNode* lt = y->left;
                while(lt)
                {
                    right.push(lt);
                    lt = lt->right;
                }
                
            }
            
            //cout<<"*"<<left.size()<<" "<<right.size()<<endl;
            
        }
        
        
        return false;
    }
};