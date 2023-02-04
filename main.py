from post import Post
from user import User

app_user_1 = User("joeriabbo@hotmail.com", "Joeri Abbo", "1234", "Devops engineer")
app_user_1.get_user_info()

app_user_2 = User("example@gmail.com", "Example User", "1234", "Devops engineer")
app_user_2.get_user_info()

new_post = Post("On a secret mission today", app_user_2.name)
new_post.get_post_info()
