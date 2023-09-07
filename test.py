import webbrowser 


def validator(func):
    def wrapper(url):
        print("Это текст до функции")
        func(url)
        print("Текст после функции")
    return wrapper

@validator
def open_url(url):
    webbrowser.open(url)
    
    
    
open_url("https://itproger.com")