import copy, Queue
class Solution(object):
    def __init__(self):
        self.c = 'abcdefghijklmnopqrstuvwxyz'

    def ladderLength(self, beginWord, endWord, wordList):
        wordList = set(wordList)
        if endWord not in wordList:
            return 0

        q = Queue.Queue()
        q.put(beginWord)
        step = 0
        while not q.empty():
            step += 1
            size = q.qsize()
            while size > 0:
                node = q.get()
                new_nodes = self.expane(node, wordList)
                if endWord in new_nodes:
                    return step + 1

                for w in new_nodes:
                    q.put(w)
                size -= 1
        return 0

    def expane(self, current, wordList):
        res = list()
        for i in range(len(current)):
            for j in range(len(self.c)):
                new_word = current[:i] + self.c[j] + current[i + 1:]
                if new_word in wordList:
                    wordList.remove(new_word)
                    res.append(new_word)

        return res