from flask import Flask, render_template, request, jsonify, redirect
import logging

from functions import get_post_all, get_post_by_pk, get_comments_by_post_id, search_for_posts, get_post_by_user
from functions import get_list_dict, get_dict_data, search_by_tag, get_bookmarks_post, add_post_bookmarks
from functions import remove_post_bookmarks


logging.basicConfig(filename="log.log", level=logging.INFO)

logger_one = logging.getLogger("one")
console_handler = logging.StreamHandler()
formatter_one = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
console_handler.setFormatter(formatter_one)
logger_one.addHandler(console_handler)

app = Flask(__name__)

@app.route('/')
def main_page():
    data = get_post_all()
    return render_template('main.html', data = data)


@app.route('/post/<int:postid>')
def post_page(postid):
    post = get_post_by_pk(postid)
    data_comment = get_comments_by_post_id(postid)
    return render_template('post.html', data=post, comments=data_comment)


@app.route('/search')
def search_form_page():
    return render_template('search_form.html')


@app.route('/search', methods=['POST'])
def search_res_page():
    sub_str = request.form['sub_str']
    data = search_for_posts(sub_str)
    return render_template('search.html', data=data, count=len(data))


@app.route('/search/<autor>')
def search_autor_page(autor):
    data = get_post_by_user(autor)
    return render_template('search.html', data=data, count=len(data))


@app.route('/tag/<tag>')
def search_tag_page(tag):
    data = search_by_tag(tag)
    return render_template('search.html', data=data, count=len(data))


@app.route('/bookmarks')
def bookmarks_page():
    data = get_bookmarks_post()
    return render_template('bookmarks.html', data=data, count=len(data))


@app.route('/bookmarks/add/<int:postid>')
def bookmarks_add_page(postid):
    add_post_bookmarks(postid)
    return redirect("/", code = 302)


@app.route('/bookmarks/remove/<int:postid>')
def bookmarks_remove_page(postid):
    remove_post_bookmarks(postid)
    return redirect("/", code = 302)


@app.route('/api/posts')
def api_posts():
    logger_one.info("Запрс страницы '/api/posts'")
    data = get_post_all()
    res = get_list_dict(data)
    return jsonify(res)


@app.route('/api/posts/<int:post_id>')
def api_posts_id(post_id):
    logger_one.info("Запрс страницы '/api/posts/<id>'")
    data = get_post_by_pk(post_id)
    return jsonify(get_dict_data(data))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500


if __name__ == '__main__':

    app.run(debug=True)