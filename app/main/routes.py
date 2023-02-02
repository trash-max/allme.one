from flask import render_template
from flask import redirect, url_for
from flask import request
# from flask import flash
from flask_login import login_required, current_user
from app.main import bp
from app.extensions import db
from app.models.links import Links
from app.models.networks import networks_data
from app.main.collector import collect_links_data, collect_share_data


@bp.route('/<unique_link>/')
def short_list_of_links(unique_link):
    '''
    Generate short list of user links by unique identifer \n
    Avaible groups for filtering: \n
    '''
    # TODO OperationalError
    user_list = Links.query.filter_by(unique_link=unique_link).first_or_404()
    links_data = collect_links_data(user_list)

    user_url = url_for('main.short_list_of_links',
                       unique_link=unique_link,
                       _external=True,
                       )
    share_data = collect_share_data(user_url)

    owner_is_paying = user_list.user.is_paying()

    if current_user.is_authenticated:
        visitor_authenticated = True
    else:
        visitor_authenticated = False

    # I can’t think about that right now. If I do,
    # I’ll go crazy. I’ll think about that tomorrow
    db.session.close()

    return render_template("links/cards/short.html",
                           links_data=links_data,
                           visitor_authenticated=visitor_authenticated,
                           owner_is_paying=owner_is_paying,
                           share_data=share_data,
                           )


@bp.route('/home/')
@login_required
def home():
    ''' Draw control panel for logged user '''
    used_links, free_links = current_user.links[0].get_links()
    # I think need else more list of paid links...
    return render_template('home.html',
                           user=current_user,
                           used_links=used_links,
                           free_links=free_links,
                           networks=networks_data,
                           )


@bp.route('/settings/')
def settings():
    if current_user.is_authenticated:
        return render_template("settings.html", centered_view=True)
    return redirect(url_for('main.index'))


@bp.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    return render_template("index.html",
                           visitor_authenticated=current_user.is_authenticated,
                           )
