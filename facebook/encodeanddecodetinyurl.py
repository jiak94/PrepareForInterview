class Codec:
    def __init__(self):
        self.mapping = {}
        self.convert = {}

    def encode(self, longURL):
        hashcode = id(longURL)
        self.mapping[hashcode] = longURL
        shorturl = "http://tinyurl.com/" + str(hashcode)
        self.convert[shorturl] = hashcode
        return shorturl
    
    def decode(self, shorturl):
        hashcode = self.convert[shorturl]
        return self.mapping[hashcode]
    

        