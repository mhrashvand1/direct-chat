from urllib import parse

def get_reverse_dict(dictionary):
    keys = dictionary.keys()
    values = dictionary.values()
    
    if not len(values) == len(set(values)):
        raise ValueError('Dictionary must has unique values for get reverse.')
    
    return dict(zip(values, keys))
    

def querystring_to_dict(querystring):
    return parse.parse_qs(querystring)