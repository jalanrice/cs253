
def build_link_index():
    links_dict = {}
    for l in links:
        links_dict[l.id] = l
    return links_dict


def link_by_id(link_id):
    reqLink = []
    for i in links:
        if i.id == link_id:
            return l



def query():
    c = db.execute("SELECT * FROM links WHERE id = 2;")

    link = Link(*c.fetchone())
    return link.votes




def query():
    for l in links:
        if l.id == 15
            return l.votes

print query

def query():
    submissions = []
    for i in links:
        if i.submitter_id == 62443:
            submission = submission(links[i], i.submitted_time)
            submissions += submission
    sorted_subs = submissions.sort(key = lambda x: x.submitted_time)
    sorted_links = sorted_subs[0] for i in sorted_subs
    return sorted_links

# User Instructions
#
# Implement the function escape_html(s), which replaces
# all instances of:
# > with &gt;
# < with &lt;
# " with &quot;
# & with &amp;
# and returns the escaped string
# Note that your browser will probably automatically
# render your escaped text as the corresponding symbols,
# but the grading script will still correctly evaluate it.
#

def escape_html(s):
    s = s.replace('"', '&quot;')
    s = s.replace('>', '&gt;')
    s = s.replace('<', '&lt;')
    s = s.replace('&', '&amp;')

    return s

print(escape_html('>'))
print(escape_html('<'))
print(escape_html('"'))
print(escape_html('&'))



# User Instructions
#
# Write a function 'sub_m' that takes a
# name and a nickname, and returns a
# string of the following format:
# "I'm NICKNAME. My real name is NAME, but my friends call me NICKNAME."
#

#given_string2 = "I'm %(nickname)s. My real name is %(name)s, but my friends call me %(nickname)s."
#def sub_m(name, nickname):
#        return given_string2 % {'name': name, 'nickname': nickname}


#print sub_m("Mike", "Goose")
# => "I'm Goose. My real name is Mike, but my friends call me Goose."



# User Instructions
#
# Write a function 'sub2' that, given two
# strings, embeds those strings in the string:
# "I think X and Y are perfectly normal things to do in public."
# where X and Y are replaced by the given
# strings.
# The function should return the new string.

#given_string2 = "I think %s and %s are perfectly normal things to do in public."
#def sub2(s1, s2):
#    subbed = given_string2 %(s1, s2)
#    return subbed

#print sub2("running", "sleeping")
# => "I think running and sleeping are perfectly normal things to do in public."
#print sub2("sleeping", "running")
# => "I think sleeping and running are perfectly normal things to do in public."







#def valid_day(day):
#    if day.isdigit():
#        int_day = int(day)
#        if int_day in list(range(1,32)):
#            return int_day
#        else:
#            return None
#    else:
#        return None

#print valid_day('0')
# => None
#print valid_day('1')
# => 1
#print valid_day('15')
# => 15
#print valid_day('500')
# => None
#print valid_day('foo')


# -----------
# User Instructions
#
# Modify the valid_year() function to verify
# whether the string a user enters is a valid
# year. If the passed in parameter 'year'
# is not a valid year, return None.
# If 'year' is a valid year, then return
# the year as a number. Assume a year
# is valid if it is a number between 1900 and
# 2020.
#

#def valid_year(year):
#    if year.isdigit():
#        year = int(year)
#        if year in list(range(1900, 2021)):
#            return year
#        else:
#            return None
#    else:
#        return None


#print valid_year('0')
#=> None
#print valid_year('-11')
#=> None
#print valid_year('1950')
#=> 1950
#print valid_year('2000')
#=> 2000
