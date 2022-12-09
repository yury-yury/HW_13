import json

from class_post import Post


def load_data():
    """
    The function does not accept any arguments, and when called, loads data from an external json file,
    creates objects of the Post class and returns them as a list of objects.
    """
    with open('data/posts.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    list_post = []
    for dict_ in data:
        obj_post = Post(dict_['pk'], dict_['poster_name'], dict_['poster_avatar'], dict_['pic'], dict_['content'],
                        dict_['views_count'], dict_['likes_count'], len(get_comments_by_post_id(dict_['pk'])))
        list_post.append(obj_post)

    return list_post


def get_dict_data(item):
    """
    The function takes as an argument an object of the Post class, forms and returns object data
    in the form of a dictionary.
    """
    dict_ = {
        "poster_name": item.poster_name,
        "poster_avatar": item.poster_avatar,
        "pic": item.pic,
        "content": item.content,
        "views_count": item.views_count,
        "likes_count": item.likes_count,
        "pk": item.pk
    }
    return dict_


def get_list_dict(list_):
    """
    The function takes as an argument a list consisting of objects of the Post class, generates and returns
    object data in the form of a list of dictionaries.
    """
    res = []
    for item in list_:
        res.append(get_dict_data(item))

    return res


def get_post_all():
    """
    The function does not accept any arguments, and when called, it returns all the posts
    available in the database as a list of objects of the Post class.
    """
    return load_data()


def get_post_by_user(user_name: str):
    """
    The function takes as an argument the name of the creator of the post as a string, searches for posts
    in the list and returns the found posts as a list of objects of the Post class.
    If there are no posts by this author, returns an empty list.
    """
    res = []
    data = load_data()
    for item in data:
        if item.poster_name == user_name:
            res.append(item)
    return res


def get_post_by_pk(pk: int):
    """
    The function takes as an argument the ordinal number of the post as an integer, searches for posts
    in the list and returns the found post as an object of the Post class.
    If there is no post with this number, it returns the corresponding message.
    """
    data = load_data()
    for item in data:
        if item.pk == pk:
            return item
    return 'There is no post with this number'


def search_for_posts(query: str):
    """
    The function takes as an argument the desired substring in the form of a string, searches for posts
    in the description of which the desired substring occurs in the list and returns the found posts
    as a list of objects of the Post class.
    If there are no posts including the desired substring, returns an empty list.
    """
    res = []
    query = query.lower()
    data = load_data()
    for item in data:
        search_content = item.content.lower()
        if query in search_content:
            res.append(item)
    return res


def search_by_tag(tag: str):
    """
    The function takes as an argument the desired substring in the form of a string, searches for posts
    in the description of which the desired substring occurs in the list and returns the found posts
    as a list of objects of the Post class.
    If there are no posts including the desired substring, returns an empty list.
    """
    res = []
    tag = tag.lower()
    data = load_data()
    for item in data:
        search_content = item.content.lower()
        if tag in search_content:
            res.append(item)
    return res


def get_comments_by_post_id(post_id: int):
    """
    The function takes as an argument the number of the post as an integer, searches for comments
    on this post in an external database and returns the found comments as a list of dictionaries.
    If there is no such number or there are no comments to this post, it causes a ValueError error.
    """
    with open('data/comments.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    res = []
    for dict_ in data:
        if dict_['post_id'] == post_id:
            res.append(dict_)
    try:
        if res == []:
            raise ValueError
    except:
        return []

    return res


def add_post_bookmarks(id:int):
    """
    The function takes as an argument the ordinal number of the post as an integer, and adds it to the list
    of posts contained in bookmarks in an external file in JSON format.
    """
    with open('data/bookmarks.json', 'r', encoding='utf-8') as file:
        bookmarks = json.load(file)

    bookmarks.append(id)
    bookmarks = list(set(bookmarks))

    with open('data/bookmarks.json', 'w', encoding='utf-8') as file:
        json.dump(bookmarks, file)


def remove_post_bookmarks(id:int):
    """
    The function takes as an argument the ordinal number of the post as an integer, and deletes it from
    the list of posts contained in bookmarks in an external file in JSON format.
    """
    with open('data/bookmarks.json', 'r', encoding='utf-8') as file:
        bookmarks = json.load(file)

    bookmarks.remove(id)

    with open('data/bookmarks.json', 'w', encoding='utf-8') as file:
        json.dump(bookmarks, file)


def get_bookmarks_post():
    """
    The function does not accept any arguments, searches for posts whose numbers are contained in bookmarks
    in an external file in JSON format, and returns them as a list consisting of objects of the Post class.
    """
    with open('data/bookmarks.json', 'r', encoding='utf-8') as file:
        bookmarks = json.load(file)

    res = []
    for id in bookmarks:
        res.append(get_post_by_pk(id))

    return res


if __name__ == '__main__':

# Code for debugging and configuring functions
    print(get_post_all())
    #print(get_post_by_user('gleo'))
    #print(type(get_post_by_pk(1)))
    #print(search_for_posts('тар'))
    #print(get_comments_by_post_id(8))
    #add_post_bookmarks(2)