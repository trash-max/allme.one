from flask import Blueprint

bp = Blueprint('main', __name__)


from app.main import routes
from app.main.links import about
from app.main.links import email
from app.main.links import twitter
from app.main.links import facebook
from app.main.links import instagram
from app.main.links import youtube
from app.main.links import cloudtips
from app.main.links import buymeacoffe
from app.main.links import boosty
from app.main.links import telegram
from app.main.links import github
from app.main.links import playmarket
from app.main.links import vk
from app.main.links import linkedin
from app.main.links import flickr
from app.main.links import gitlab
from app.main.links import stackoverflow
from app.main.links import steampublisher
from app.main.links import steamdeveloper
from app.main.links import patreon
from app.main.links import pinterest
