import pytest

from functions import load_data, get_post_all, get_post_by_user, get_post_by_pk, get_dict_data, get_bookmarks_post
from functions import search_for_posts, get_comments_by_post_id, get_list_dict, search_by_tag


def test_load_data():
    """
    The function contains unit tests to check the correctness of the "load_data" function.
    """
    data = load_data()

    assert data != [], "Data loading error"
    assert type(data) == list, "Data loading error"


def test_get_dict_data():
    """
     The function contains unit tests to check the correctness of the "get_dict_data" function.
    """
    data = get_dict_data(get_post_by_pk(1))
    assert type(data) == dict, "Data dictionary formation error."
    assert data != {}, "Data dictionary formation error."


def test_get_list_dict():
    """
     The function contains unit tests to check the correctness of the "get_list_dict" function.
    """
    data = get_list_dict(get_post_all())
    assert type(data) == list, "Dictionary list generation error."
    assert type(data[0]) == dict, "Dictionary list generation error."


def test_get_post_all():
    """
    The function contains unit tests to check the correctness of the "get_post_all" function.
    """
    data = get_post_all()

    assert data[0].pk == load_data()[0].pk, "Error generating a list of all posts"
    assert data[0].poster_name == load_data()[0].poster_name, "Error generating a list of all posts"
    assert data[0].poster_avatar == load_data()[0].poster_avatar, "Error generating a list of all posts"
    assert data[0].pic == load_data()[0].pic, "Error generating a list of all posts"
    assert data[0].content == load_data()[0].content, "Error generating a list of all posts"
    assert data[0].views_count == load_data()[0].views_count, "Error generating a list of all posts"
    assert data[0].likes_count == load_data()[0].likes_count, "Error generating a list of all posts"


def test_get_post_by_user():
    """
    The function contains unit tests to check the correctness of the "get_post_by_user" function.
    """
    data = get_post_by_user(get_post_all()[0].poster_name)

    assert data != [], "Error searching for posts by author."
    assert type(data) == list, "Error searching for posts by author."
    assert data[0].content == get_post_all()[0].content, "Error searching for posts by author."

    for item in data:
        assert item.poster_name == get_post_all()[0].poster_name, "Error searching for posts by author."


grade_parameters = [(1, get_post_all()[0]), (2, get_post_all()[1]), (3, get_post_all()[2]), (4, get_post_all()[3])]

@pytest.mark.parametrize("grade_int, grade_obj", grade_parameters)
def test_get_post_by_pk(grade_int, grade_obj):
    """
    The function contains unit tests to check the correctness of the "get_post_by_pk" function.
    """
    assert get_post_by_pk(grade_int).pk == grade_obj.pk, "Error searching for a post by ordinal number."
    assert get_post_by_pk(grade_int).poster_name == grade_obj.poster_name, "Error searching for a post by " \
                                                                           "ordinal number."
    assert get_post_by_pk(grade_int).poster_avatar == grade_obj.poster_avatar, "Error searching for a post by " \
                                                                               "ordinal number."
    assert get_post_by_pk(grade_int).pic == grade_obj.pic, "Error searching for a post by ordinal number."
    assert get_post_by_pk(grade_int).content == grade_obj.content, "Error searching for a post by ordinal number."
    assert get_post_by_pk(grade_int).views_count == grade_obj.views_count, "Error searching for a post by " \
                                                                           "ordinal number."
    assert get_post_by_pk(grade_int).likes_count == grade_obj.likes_count, "Error searching for a post by " \
                                                                           "ordinal number."


def test_search_for_posts():
    """
     The function contains unit tests to check the correctness of the "search_for_posts" function.
    """
    data = search_for_posts(get_post_all()[0].content[:4])

    assert data[0].pk == get_post_all()[0].pk, "Error searching for posts by the occurrence of a substring."
    assert data[0].poster_name == get_post_all()[0].poster_name, "Error searching for posts by the occurrence" \
                                                                 " of a substring."
    assert data[0].poster_avatar == get_post_all()[0].poster_avatar, "Error searching for posts by the occurrence " \
                                                                     "of a substring."
    assert data[0].pic == get_post_all()[0].pic, "Error searching for posts by the occurrence of a substring."
    assert data[0].content == get_post_all()[0].content, "Error searching for posts by the occurrence of a substring."
    assert data[0].views_count == get_post_all()[0].views_count, "Error searching for posts by the occurrence " \
                                                                 "of a substring."
    assert data[0].likes_count == get_post_all()[0].likes_count, "Error searching for posts by the occurrence " \
                                                                 "of a substring."
    assert data != [], "Error searching for posts by the occurrence of a substring."


def test_search_by_tag():
    """
    The function contains unit tests to check the correctness of the "search_by_tag" function.
    """
    data = search_by_tag('cat')
    assert type(data) == list, "Error generating a list of objects by tag."


def test_get_comments_by_post_id():
    """
     The function contains unit tests to check the correctness of the "search_for_posts" function.
    """
    data = get_comments_by_post_id(1)
    assert type(data) == list, "Error searching for comments to the post."
    assert type(data[0]) == dict, "Error searching for comments to the post."
    assert data != [], "Error searching for comments to the post."


def test_get_bookmarks_post():
    """
     The function contains unit tests to check the correctness of the "get_bookmarks_post" function.
    """
    data = get_bookmarks_post()
    assert type(data) == list, "Error generating a list of objects contained in bookmarks."

