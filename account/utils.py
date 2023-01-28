from string import digits, ascii_lowercase, ascii_letters
from random import choices
import time

def generate_file_prefix():
    timestamp = str(time.time()).split(".")[1][-5:]
    random_string = "".join(choices(ascii_lowercase+digits, k=5))
    return timestamp + '-' + random_string

def get_final_filename(filename):
    suffix = filename.split(".")[-1]
    new_filename = generate_file_prefix() + '.' + suffix
    return new_filename
    
def get_avatar_path(instance, filename):
    return f"{instance.user.id}/avatars/{get_final_filename(filename)}"


def unique_generator(class_, field_name, length=15):
    
    new_code = "".join(choices(ascii_letters+digits, k=length))
    arguments = {field_name:new_code}
    qs_exists = class_.objects.filter(**arguments).exists()
    
    if qs_exists:
        return unique_generator(class_, field_name, length=length)
    
    return new_code