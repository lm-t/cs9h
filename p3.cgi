#!/usr/local/bin/python
import cgitb, random, cgi
cgitb.enable()

form = cgi.FieldStorage()

def first_time():
    '''executes the nececessary strings to display a web page'''
    print "Content-Type: text/html"
    print
    print '<!DOCTYPE>'
    print '<html>'
    print '<body>'
    print '<h1>Hello!</h1>'
    print "<p>Welcome to my program! Please give me a verb and a noun...</p>"
    print mad_libs[random.randint(0,4)]
    print '</body>'
    print '</html>'
def second_time():
    '''displays the mad lib from the words the user submitted''' 
    if '1' in form.keys()[0]:
        return 'The %s %s my %s homework.' % (form['noun1'].value, form['verb1'].value, form['adj1'].value)
    elif '2' in form.keys()[0]:
        return '%s ate %s hot dogs while %s running the marathon.' % (form['person2'].value, form['number2'].value, form['adverb2'].value)
    elif '3' in form.keys()[0]:
        return '%s is one of the most %s places in the world where one can walk %s.' % (form['place3'].value, form['adj3'].value, form['adverb3'].value)
    elif '4' in form.keys()[0]:
        return 'The %s %s %s in the cold rain.' % (form['adj4'].value, form['noun4'].value, form['verb4'].value)
    else:
        return 'On a %s bed, there is a %s who %s sleeps.' % (form['adj5'].value, form['noun5'].value, form['adverb5'].value)
mad_lib1 = """<form action='p3.cgi'>
Enter a VERB:
<input type=text name=verb1><br>
Enter an ADJECTIVE:
<input type=text name=adj1><br>
Enter a NOUN:
<input type=text name=noun1><br>
<input type=submit value='ok'>
</form>"""

mad_lib2 = """<form action='p3.cgi'>
Enter an ADVERB:
<input type=text name=adverb2><br>
Enter a NUMBER:
<input type=text name=number2><br>
Enter a PERSON:
<input type=text name=person2><br>
<input type=submit value='ok'>
</form>"""
mad_lib3 = """<form action='p3.cgi'>
Enter an ADVERB:
<input type=text name=adverb3><br>
Enter an ADJECTIVE:
<input type=text name=adj3><br>
Enter a PLACE:
<input type=text name=place3><br>
<input type=submit value='ok'>
</form>"""
mad_lib4 = """<form action='p3.cgi'>
Enter a VERB:
<input type=text name=verb4><br>
Enter an ADJECTIVE:
<input type=text name=adj4><br>
Enter a NOUN:
<input type=text name=noun4><br>
<input type=submit value='ok'>
</form>"""
mad_lib5 = """<form action='p3.cgi'>
Enter an ADJECTIVE:
<input type=text name=adj5><br>
Enter an ADVERB:
<input type=text name=adverb5><br>
Enter a NOUN:
<input type=text name=noun5><br>
<input type=submit value='ok'>
</form>"""

mad_libs = [mad_lib1 , mad_lib2, mad_lib3, mad_lib4, mad_lib5]

if len(form) == 0:
    first_time()
else:
    print 'Content-Type: text/html'
    print
    print '<h1>', second_time(), '</h1>'
    print '<a href=p3.cgi>Try Again</a>'
