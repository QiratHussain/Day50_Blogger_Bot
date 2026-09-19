from post import PostManager
from quote import Quote

quote_finder= Quote()
quote_finder.goto_site()
quote_content= quote_finder.get_quote()
quote_part= quote_content[0]
author= quote_content[1]

blogger= PostManager()
blogger.goto_site()

# TODO: 1. log in to blogger
# TODO: 2. make a blogger post
# TODO: 3. generate random quote
# TODO: 4. parse quote 
# TODO: 5. send quote to ai
# TODO: 6. prompt ai for content
# TODO: 7. give content to ai
# TODO: 8. prompt ai for an img
# TODO: 9. send img, content and quote to blogger