"""Single Responsibility Principle"""

## Suppose you're working on a simple blogging system.
## You might have a class BlogPost that handles both the creation and the formatting of blog posts:


class BlogPost:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def create_post(self):
        # Code to create a new blog post in the database
        pass

    def format_post(self):
        # Code to format the blog post for display
        pass


# In this example, the BlogPost class has two responsibilities: creating a blog post and formatting a blog post.
# This violates the Single Responsibility Principle because a change in formatting requirements could affect the creation logic, and vice versa.
# To adhere to the SRP, you could split the responsibilities into two separate classes:


class BlogPostCreator:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def create_post(self):
        # Code to create a new blog post in the database
        pass


class BlogPostFormatter:
    def __init__(self, post):
        self.post = post

    def format_post(self):
        # Code to format the blog post for display
        pass


# Now, the BlogPostCreator class is responsible only for creating posts, and the BlogPostFormatter class is responsible for formatting posts.
# This separation makes the code more modular and easier to maintain.
# If there are changes in formatting requirements, they won't affect the creation logic, and vice versa.

# By adhering to the Single Responsibility Principle, you ensure that each class has a single reason to change, making your codebase more maintainable and flexible.
