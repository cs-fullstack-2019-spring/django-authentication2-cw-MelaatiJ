### POINTS: 2
### KEY: Met minimum requirements for points. Should probably use CASCADE delete option so bloggers posts get deleted if blogger deleted, but didn't cost you points.

# Django Authentication CW

### Exercise 1:

Create a blog app that will allows pre-created users to log in and see all posts created/assigned to them. 

A user's post should include a ```username```, ```blog_title```, and ```blog_entry```. 

The index/root localhost page should show a logged in user's personal blog entries. 

If a user is not logged in, it should ask them to log in.

The pre-created user(s) and the blog entries should be created using the Django admin page.

### Challenge:
Use User Groups to have a 'blog user' group and a 'blog_admin' group. Users in admin group should be able to see all blog entries, and optionally edit or delete them (NOTE: The edit and delete links can go to simple placeholder pages and do not have to actually allow entries to get edites/deleted.
