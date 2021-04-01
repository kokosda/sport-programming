class Codec:    
    def __init__(self):
        self.matches = dict()
        self.hash_attempts = 100
        self.min_count = 5
        self.max_count = 10
        self.base_url = 'http://tinyurl.com/'
        
        self.store = [
            *[chr(i) for i in range(ord('a'), ord('z') + 1)],
            *[chr(i) for i in range(ord('A'), ord('Z') + 1)],
            *[chr(i) for i in range(ord('0'), ord('9') + 1)],
        ]
        self.store.sort(key=lambda x: random.random())
        
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl.find(self.base_url) is 0:
            return self.base_url
        
        if self.matches.get(longUrl) is None:
            hashed_url = self._get_hashed_url()
            self.matches[longUrl] = hashed_url
            self.matches[hashed_url] = longUrl
            
        return self.matches[longUrl]

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        
        if shortUrl.find(self.base_url) is not 0:
            raise ValueError(f'Short URL {shortUrl} does not belong to current domain.')
        
        if self.matches.get(shortUrl) is not None:
            return self.matches[shortUrl]
        
        raise ValueError(f'There is no such short URL {shortUrl} .')
    
    def _get_hashed_url(self) -> str:
        tmp = []
        hash_attempts = self.hash_attempts
        
        while True:
            len_s = random.randint(self.min_count, self.max_count)
            
            while len_s >= 0:
                tmp.append(random.choice(self.store))
                len_s -= 1
                
            res = f'{self.base_url}{"".join(tmp)}'
            
            if self.matches.get(res) is None:
                return res
            
            hash_attempts -= 1
            
            if hash_attempts is -1:
                hash_attempts = self.hash_attempts
                self.min_count += self.min_count
                self.max_counut += self.min_count
                
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))