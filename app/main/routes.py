from flask import render_template
from flask import redirect, url_for
from flask import send_from_directory
# from flask import flash
from flask_login import login_required, current_user
from app.main import bp
from app.extensions import db
from app.models import Links
from app.models.networks import networks_data
from app.models.gravatar import Gravatar
from app.main.collector import collect_links_data, collect_share_data


@bp.route('/<unique_link>/')
def short_list_of_links(unique_link):
    '''
    Generate short list of user links by unique identifer \n
    Avaible groups for filtering: \n
    '''
    # TODO OperationalError
    # TODO Query syntax changed in ver. 3.0.x
    # Must be:
    # user_list = db.one_or_404(db.select(Links).filter_by(unique_link=unique_link))
    # https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/queries/
    user_list = Links.query.filter_by(unique_link=unique_link).first_or_404()
    gravatar = Gravatar(user_list.user.email)
    links_data = collect_links_data(user_list)
    share_data = collect_share_data(unique_link)
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
                           owner_gravatar=gravatar.get_gravatar(),
                           )


@bp.route('/home/')
@login_required
def home():
    ''' Draw control panel for logged user '''
    used_links, free_links = current_user.links[0].get_links()
    # I think need else more list of paid links...
    share_data = collect_share_data(current_user.links[0].unique_link)
    # current_user.update_geo_data(ip=request.remote_addr)
    return render_template('home.html',
                           user=current_user,
                           used_links=used_links,
                           free_links=free_links,
                           networks=networks_data,
                           share_data=share_data,
                           )


@bp.route('/settings/')
@login_required
def settings():
    if current_user.is_authenticated:  # FIXME Double check not needed
        return render_template("settings.html", centered_view=True)
    return redirect(url_for('main.index'))


@bp.route('/')
def index():
    return render_template("index.html",
                           visitor_authenticated=current_user.is_authenticated,
                           )


@bp.route('/app-ads.txt')
def app_ads_txt():
    # AdMob app_ads.txt
    return send_from_directory("static", "app-ads.txt")


@bp.route('/ads.txt')
def ads_txt():
    # AdMob app_ads.txt
    return send_from_directory("static", "ads.txt")
