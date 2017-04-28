class Codec:

    def __init__(self):
        self.map = {}
        self.i = 0
    
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        :type longUrl: str
        :rtype: str
        """
        self.i += 1
        self.map[self.i] = longUrl
        return "http://tinyurl.com/" + str(self.i)


    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        :type shortUrl: str
        :rtype: str
        """
        return self.map[int(shortUrl.split('/')[-1])]

# Your Codes object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

url = "https://leetcode.com/problems/design-tinyurl";
codec = Codec()
assert codec.decode(codec.encode(url)) == url