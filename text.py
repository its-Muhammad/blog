# class BlogPost:
#     def __init__(self, id, title, subtitle, body, author, date):
#         self.id = id
#         self.title = title
#         self.subtitle = subtitle
#         self.body = body
#         self.author = author
#         self.date = date


# import requests
#
# data = requests.get(url="https://api.npoint.io/ef7d3aa7f50c686498ba")
# blog_data = data.json()
# blog_obj = [BlogPost(data["id"], data["title"], data["subtitle"], data["body"], data["author"], data["date"]) for data
#             in blog_data]
#
# for post in blog_obj:
#     print(post.id)
#     print(post.date)