class Config:
    
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance= super().__new__(cls)
        return cls.instance

c = Config()
print(c)
s = Config()
print(s)