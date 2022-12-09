from flask import Blueprint
from . import products, reviews, session, orders

bp = Blueprint("api", __name__, url_prefix="/api")

bp.register_blueprint(session.bp)
bp.register_blueprint(products.bp)
bp.register_blueprint(reviews.bp)
bp.register_blueprint(orders.bp)


@bp.route("docs")
def api_help():
    """
    Returns all API routes and their doc strings
    """
    acceptable_methods = ['GET', 'POST', 'PATCH', 'DELETE']
    route_list = {rule.rule: [[method for method in rule.methods if method in acceptable_methods],
                              bp.view_functions[rule.endpoint].__doc__]
                  for rule in bp.url_map.iter_rules() if rule.endpoint != 'static'}
    return route_list
