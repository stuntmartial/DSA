class TrieNode:
    def __init__(self):
        self.CHILDREN= [None]*26; self.CHILD_CHARS= list()
        self.IS_END= False

    def addChild(self, char):
        index_= ord(char)- 97
        childTrieNode= TrieNode()
        self.CHILDREN[index_]= childTrieNode
        self.CHILD_CHARS.append(char)
        return childTrieNode

    def getChild(self, char):
        index_= ord(char)- 97
        return self.CHILDREN[index_]

    def getChildren(self):
        children= list()
        for childTrieNode in self.CHILDREN:
            if childTrieNode is not None: children.append(childTrieNode)

        return children, [char for char in self.CHILD_CHARS]

    def set_IS_END(self): self.IS_END= True

class Trie:
    def __init__(self)-> None:
        self.ROOT= TrieNode()

    def addWord(self, word, wordLength)-> None:
        index= 0
        lastMatchedNode, lastMatchedIndex= Trie.searchUtil(self.ROOT, word, wordLength, index)

        currNode, currIndex= lastMatchedNode, lastMatchedIndex+ 1
        while currIndex< wordLength:
            currChar= word[currIndex]
            currNode= currNode.addChild(currChar); currIndex+= 1
        
        currNode.set_IS_END()

    def get_trieBranches(self):
        trieBranches= list()
        Trie.get_trieBranchesUtil(self.ROOT, trieBranches)
        return trieBranches

    @staticmethod
    def get_trieBranchesUtil(currTrieNode, trieBranches, currString= str()):
        children, characters= currTrieNode.getChildren()
        if len(children)== 0: trieBranches.append(currString); return

        for index, childTrieNode in enumerate(children):
            Trie.get_trieBranchesUtil(childTrieNode, trieBranches, "".join([currString, characters[index]]) )
    
    @staticmethod
    def searchUtil(currTrieNode, word, wordLength, index)-> (TrieNode, int):
        returnFlag= True if index== wordLength-1 else False

        currChar= word[index]
        childTrieNode= currTrieNode.getChild(currChar)

        if childTrieNode is None: return currTrieNode, index-1
        if returnFlag: return childTrieNode, index

        return Trie.searchUtil(childTrieNode,word, wordLength, index+1)

class Solution:
    def minimumLengthEncoding(self, words)-> int:
        trie_ins= Trie()

        for word in words: trie_ins.addWord(Solution.reverse(word), len(word))
        trieBranches= trie_ins.get_trieBranches()

        encodingLength= 0
        for word in trieBranches: encodingLength+= (len(word)+ 1)

        return encodingLength

    @staticmethod
    def reverse(word)-> str:
        reverseWord= str()
        for ch in word: reverseWord= "".join([ch, reverseWord])
        return reverseWord