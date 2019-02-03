### lyric searcher: project 2b by Luis Torres ###
import urllib

print 'Lyric Searcher by Luis Torres'
print "lyrics provided from azlyrics.com"
print "Enter an artist and a song name to search for lyrics."
print "Note that some artist must be entered differently. For example, 'The Black Keys' should be entered 'Black Keys', 'Earth, Wind and Fire' should be entered 'Earth Wind and Fire'."
print "Also to get the lyric, you must not put any special characters in the artist and song. Some examples are ' , < > # % & "
def main():
    artist = raw_input("Who is the Artist?: ")
    song = raw_input("What is the song called?: ")
    f = 'http://www.azlyrics.com/lyrics/%s/%s.html' % (artist.replace(' ', '').lower(), song.replace(' ', '').lower())
    url = urllib.urlopen(f)
    html = url.read()
    url.close()
    def parse(string):
        """
        Takes a string with html code and returns only the lyrics.
        """
        if 'third-party lyrics provider' not in string:
            print 'Could not find the lyric. Please try again.'
            return main()
        string = string.split('<!-- Usage of azlyrics.com content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->')[1]
        string = string .split('<!-- MxM banner -->')[0]
        string = string.replace('<br>', '')
        string = string.replace('</div>', '')
        string = string.replace('<i>', '')
        string = string.replace('</i>', '')
        return string
    return parse(html)
print main()
