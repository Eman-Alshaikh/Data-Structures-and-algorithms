

class k_Node:
    def __init__(self,value):
        self.value=value
        self.children=[ ]
 

class k_aryTree: 
    def __init__(self,root=None):
        self.root=root

    def fizz_buzz_tree(self):
         fb_node_values=[]

         if self.root:
            fb_root=k_aryTree.fizz_buzz_tree(k_Node(self.root.value))
            fizz_buzz_tree=k_aryTree(fb_root)

         else:

           return 'empty tree'
         
         def traverse(node):
            fb_node_values.append(node.value)
            new_node=k_Node(node.value)

            for child in node.children:

                new_child_node=k_aryTree.fizz_buzz_tree(k_Node(child.value))
                new_node.children.append(new_child_node)

            
            if node==self.root:
                print(' threshold 0 ')
                for new_child in new_child.children:
                    print(' threshold 1 ')
                    fizz_buzz_tree.root.children.append(new_child)

         traverse(self.root)
         return fizz_buzz_tree, fb_node_values



        

   
    @staticmethod
    def fizz_buzz_fun(value):
        if value%3==0 and value%5==0:
            return "FizzBuzz"
        if value%3==0:
            return "Fizz"
        if value%5==0:
            return "Buzz"
        value=str(value)
        return value





