
# QUIZ - implement the function add_new_link() that both adds a link to the
# "links" list and updates the link_index dictionary.
def add_new_link(link):
    links.append(link)
    link_index[link.id] = link

# python code to include SQL query for one item
def query():
    c = db.execute("SELECT * FROM links WHERE id = 2;")

    link = Link(*c.fetchone())
    return link.votes

#python code to include SQL query with list of items

def query():
    results[]
    c = db.execute("SELECT * FROM links WHERE submitter_id = 62443 ORDER BY submitted_time ASC;")
    for link_tuple in c:
        link = Link(*link_tuple)
        results.append(link.id)
    return results

# same, but only pulling id from db
def query():
    results[]
    c = db.execute("SELECT id FROM links WHERE submitter_id = 62443 ORDER BY submitted_time ASC;")
    results = [t[0] for t in c]
    return results

print query()




#python code to query DB without SQL
def query():
    submissions = []
    for i in links:
        if i.submitter_id == 62443:
            submission = submission(links[i], i.submitted_time)
            submissions += submission
    sorted_subs = submissions.sort(key = lambda x: x.submitted_time)
    sorted_links = sorted_subs[0] for i in sorted_subs
    return sorted_links
