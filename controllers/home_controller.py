# An example of what a controller might look like
def index(request):
    # Views are not yet implemented, but might look something like
    # return view('something')
    return 'This is a response from the controller index method'

def details(request, some_var=None):
    if (some_var == None):
        return 'This is a response from other page with no request vars.'

    return 'This is a response from the other page with some_var='+some_var

def test(request, required, optional=False):
    return 'test complete with required: '+required+', optional: '+optional