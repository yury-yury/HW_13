


class Post:
    """

    """
    def __init__(self, pk: int, poster_name: str, poster_avatar: str, pic: str, content: str,
                 views_count=0, likes_count=0, comment_count=0):
        """

        """
        self.pk = pk
        self.poster_name = poster_name
        self.poster_avatar = poster_avatar
        self.pic = pic
        self.content = content
        self.short_content = content[ :48] + '...'
        self.views_count = views_count
        self.likes_count = likes_count
        self.comment_count = comment_count


    def __repr__(self):
        """

        """
        return f'post {self.poster_name} number {self.pk}'
