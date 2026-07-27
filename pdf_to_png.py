from importlib import import_module
utils=import_module("0utils")
globals().update({n:getattr(utils,n) for n in dir(utils) if not n.startswith("_")})
if __name__=="__main__":
    print("Loaded 0utils.py")
