class TrieNode:
    def __init__(self)-> None:
        self.__CHILDREN= [None]* 26; self.__IS_END= False
        self.__WORDS= list()

    def addChild(self, char):
        index_ = ord(char)- 97; childTrieNode= TrieNode()
        self.__CHILDREN[index_]= childTrieNode
        return childTrieNode

    def getChild(self, char):
        index_= ord(char)- 97
        return self.__CHILDREN[index_]

    def getChildren(self):
        childTrieNodes= list()
        for childTrieNode in self.__CHILDREN:
            if childTrieNode is not None: childTrieNodes.append(childTrieNode)
        return childTrieNodes

    def get_IS_END(self)-> bool: return self.__IS_END
    def set_IS_END(self)-> None: self.__IS_END= True

    def addWord(self, word)-> None: self.__WORDS.append(word)
    def get_WORDS(self)-> [str]: return [word for word in self.__WORDS]

class Trie:
    def __init__(self)-> None:
        self.ROOT= TrieNode()

    def addWord(self, word, wordLength)-> None:
        index= 0
        lastMatchedNode, lastMatchedIndex= Trie.searchUtil(self.ROOT, word, index, wordLength)

        currNode= lastMatchedNode; currIndex= lastMatchedIndex+ 1
        while currIndex< wordLength:
            currChar= word[currIndex]
            currNode= currNode.addChild(currChar); currIndex+= 1

        currNode.set_IS_END(); currNode.addWord(word)

    @staticmethod
    def setWords(trieNode):
        currWordList= list()
        if trieNode.get_IS_END(): currWordList= [word for word in trieNode.get_WORDS()]
        
        children= trieNode.getChildren()
        if len(children)== 0: return currWordList 

        for childTrieNode in children:
            childWordList= Trie.setWords(childTrieNode)

            for word in childWordList: currWordList.append(word); trieNode.addWord(word)
        
        #print(currWordList)
        return currWordList
        
    def search(self, word, wordLength)-> [[str]]:
        suggestionsList= list(); index= 0
        Trie.searchUtil(self.ROOT, word, index, wordLength, suggestionsList)
        return suggestionsList

    @staticmethod
    def searchUtil(currTrieNode, word, index, wordLength, suggestionsList= list())-> tuple:
        returnFlag= True if index== wordLength- 1 else False

        currChar= word[index]
        childTrieNode= currTrieNode.getChild(currChar)

        if childTrieNode is None: 
            for _ in range(wordLength- index): suggestionsList.append(list())
            return currTrieNode, index- 1
        
        currSuggestionList= Trie.get_currSuggestionList(childTrieNode)
        suggestionsList.append(currSuggestionList)

        if returnFlag:
            return childTrieNode, index

        return Trie.searchUtil(childTrieNode, word, index+1, wordLength, suggestionsList)

    @staticmethod
    def get_currSuggestionList(trieNode)-> [str]:
        currSuggestionList= trieNode.get_WORDS()
        return currSuggestionList[: min( len(currSuggestionList), 3 )]

class Solution:
    def suggestedProducts(self, products, searchWord)-> [[str]]:
        trie_ins= Trie()
        for product in products: wordLength= len(product); trie_ins.addWord(product, wordLength)

        Trie.setWords(trie_ins.ROOT)
        suggestionsList= trie_ins.search(searchWord, len(searchWord))
        return suggestionsList

products= ["mobile","mouse","moneypot","monitor","mousepad"]; searchWord= "mouse"
print(Solution().suggestedProducts(products, searchWord))

