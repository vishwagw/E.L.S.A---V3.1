import subprocess

def launch_appp(path_of_app):
    try:
        subprocess.call([path_of_app])
        return True
    except Exception as e:
        print(e)
        return False
    
