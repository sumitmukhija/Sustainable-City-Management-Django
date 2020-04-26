def singleton(_class):
    """[summary]
    
    Arguments:
        _class class -- Class to be made singleton
    
    Application:
        Use as a decorator 

        example: 

        @singleton
        class TheClass(object):
            pass
    """
    instances = {}
    def get_instance(*args, **kwargs):
        """Inner function that returns the instance of the given class
        
        Returns:
            instance -- instance of the singleton class. If not present, creates & return
        """
        if _class not in instances:
            instances[_class] = _class(*args, **kwargs)
        return instances[_class]
    return get_instance
