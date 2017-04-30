class BST:

    class Treenode():
        def __init__(self,value):
            self.value = value
            self.rc= None
            self.lc = None
            self.next = self.rc

    def __init__(self):
        self.root = self.Treenode("Oiddle")
        self.levels = 1
        self.format = 2
        self.format_i = "%"
        self.format_ii = "s"
        self.ridigier = 5
        self.ledifier = 2
        self.rightspace = 8
        self.leftspace = 20
    
        
    def __str__(self):
        tree = ""
        runner = self.root
        return str(runner.value)+ "\n" + str(self.walktree(runner))

    def walktree(self,director):
        tree = ""
        if director == None:
            pass
        else:
            if director.lc != None:
                tree += "lc:" + str(director.lc.value) + "   "
            else:
                tree += "lc: " + str(director.lc) + "   "
            if director.rc != None:
                tree += "rc:" + str(director.rc.value)+ "\n"
            else:
                tree += "rc: " + str(director.rc) + "\n"
            
            if director.lc != None: 
                tree += "this is lc of:  " +str(director.lc.value) + "  " + str(self.walktree(director.lc))
            if director.rc != None:
                tree += "this is rc of:  " + str(director.rc.value) + "  " + str(self.walktree(director.rc))

        return tree
    def addBST(self,value,node):
        if node.lc == None and value < node.value:
            node.lc = self.Treenode(value)
            return
        
        elif node.rc == None and value > node.value:
            node.rc =self.Treenode(value)
            return

        elif node.lc != None and value < node.value:
            self.addBST(value,node.lc)

        elif node.rc != None and value > node.value:
            self.addBST(value,node.rc)

        
        
        """if node.lc == None and node.rc == None:
            if value < node.value:
                node.lc = self.TreeNode(value + str(1)) 
                return
            node.rc = self.TreeNode(value + str(1))
            return

        elif node.lc != None and node.rc == None:
            if value > node.value:
                node.rc = self.TreeNode(value + str(2))
                return
        elif node.rc != None and node.lc == None:
            if value < node.value:
                node.lc = self.TreeNode(value + str(2))
                return
            
        if node.lc != None:
            if value < node.lc.value:
                self.addBST(value,node.lc)
            
            
        if node.rc != None:
            if value > node.rc.value:
                self.addBST(value,node.rc)

        """
    def make_tree(self):

        runner = self.root
        left = None
        right=  None
        tree = ""
        cache = []
        
        if runner.lc != None:
            cache.append(runner.lc)
        if runner.rc != None:
            cache.append(runner.rc)
        cache_i = cache[:]
        times =self.format_levels(cache)

        if times > 5:
            self.leftspace = self.leftspace * (2 ** (times -5))
        
        start = self.format_i + str(self.ridigier) + self.format_ii
        tree += start % str(runner.value) + "\n"
        self.levels = self.levels * 2
        
        while self.levels == 2:
            a = 0
            if runner.lc != None:
                led = self.format_i + str(self.ledifier) + self.format_ii
                tree += led % str(runner.lc.value)
            else:
                if runner.rc != None:
                    a =1
                    right = self.format_i + str(self.rightspace) + self.format_ii
                    tree += right % str(runner.rc.value)  
            if runner.rc != None:
                if a == 0:               
                    rig = self.format_i + str(self.ridigier) + self.format_ii
                    tree += rig % str(runner.rc.value)
            
            self.levels = self.levels *2
            tree += "\n"
        tree += self.make_levels(cache_i,times)
        return tree

    def make_levels(self,cache,levels):
        
        tree = ""
        newcache = []
        x = 2
        self.ledifier = self.ledifier//2
        self.ridigier = self.ridigier //2
        self.rightspace = self.rightspace//2
        self.leftspace = self.leftspace//2
        while len(cache) != 0:
            x+=1
            a = 0
            runner = cache[0]
            if runner.lc != None:
                led = self.format_i + str(self.ledifier) + self.format_ii
                tree += led % str(runner.lc.value)
                newcache.append(runner.lc)
            else:
                led = self.format_i + str(self.leftspace) + self.format_ii
                tree += led % str("")
                
                if runner.rc != None:
                    a=1
                    space = self.format_i + str(self.rightspace) + self.format_ii
                    tree += space % str(runner.rc.value)
                else:
                    a=1
                    space = self.format_i + str(self.leftspace) + self.format_ii
                    tree += space % str("")
                    
                    
            if runner.rc != None and a == 0:
                rig = self.format_i + str(self.ridigier) + self.format_ii
                tree += rig % str(runner.rc.value) + "      "
                newcache.append(runner.rc)
            else:
                rig = self.format_i + str(self.leftspace) + self.format_ii
                tree += rig % str("") + "      "

            a=0
            del cache[0]
        print(newcache)
        cache = newcache
        tree += "\n"
        if len(cache) != 0:
            tree += self.make_levels(cache,levels)
        return tree

    def empty_space(self,cache):

        tree = ""
        question = cache[0]
        if question.lc == None and question.rc == None:
            space = self.format_i + str(self.leftspace) + self.format_ii
            tree += space % str("")
            return tree
        return tree
        

    def format_levels(self,cache):
        
        counter = cache
        newcounter = []
        while len(counter) != 0:
            walker = counter[0]
            del counter[0]
            if walker.lc != None:
                newcounter.append(walker.lc)
            if walker.rc != None:
                newcounter.append(walker.rc)
        if len(newcounter) != 0:
            self.format += 1
            self.ridigier = self.ridigier *2
            self.ledifier = self.ledifier *2
            self.rightspace = self.rightspace * 2
            self.format_levels(newcounter)

        return self.format

    def preorder(self):
        line = ""
        walker = self.root
        line += walker.value

        if walker.lc != None:
            line += "(" + str(walker.lc.value)
        else:
            line += "(" + str(walker.lc)

        if walker.lc != None:
            runner = walker.lc

        if walker.rc != None:
            speed = walker.rc

        line += self.preorder_aux(runner)
        if walker.rc != None:
            line += str(walker.rc.value) + "("
        line += self.preorder_aux(speed)

        return line

    def preorder_aux(self, node):

        line = ""
        if node.lc != None:
            that = node.lc
            if that.rc == None and node.rc == None and that.lc != None:
                line += "(" + str(node.lc.value) + "("
                line += self.preorder_aux(node.lc)
            elif that.rc == None and node.rc == None:
                line += "(" + str(node.lc.value) + ")"
                line += self.preorder_aux(node.lc)
            else:
                line += "(" + str(node.lc.value) 
                line += self.preorder_aux(node.lc)
                

        if node.rc != None:
            this = node.rc
            if this.lc != None or this.rc != None:
                line += str(node.rc.value)
                line += self.preorder_aux(node.rc)
            else:
                line += str(node.rc.value) + ")"
                line += self.preorder_aux(node.rc)

        return line

            

        
        
            

        

        
        
            





























        


    
    
                
