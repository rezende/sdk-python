from starkcore.utils.api import from_api_json
from starkcore.utils.resource import Resource
from starkcore.utils.checks import check_datetime, check_date
from ...utils import rest
from ..__corporateholder import _resource as _corporate_holder_resource


class Log(Resource):
    """# corporateholder.Log object
    Every time a CorporateHolder entity is updated, a corresponding corporateholder.Log
    is generated for the entity. This log is never generated by the
    user, but it can be retrieved to check additional information
    on the CorporateHolder.
    ## Attributes (return-only):
    - id [string]: unique id returned when the log is created. ex: "5656565656565656"
    - holder [CorporateHolder]: CorporateHolder entity to which the log refers to.
    - type [string]: type of the CorporateHolder event which triggered the log creation. ex: "blocked", "canceled", "created", "unblocked", "updated"
    - created [datetime.datetime]: creation datetime for the log. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)
    """

    def __init__(self, id, holder, type, created):
        Resource.__init__(self, id=id)

        self.holder = from_api_json(_corporate_holder_resource, holder)
        self.type = type
        self.created = check_datetime(created)


_resource = {"class": Log, "name": "CorporateHolderLog"}


def get(id, user=None):
    """# Retrieve a specific corporateholder.Log
    Receive a single corporateholder.Log object previously created by the Stark Bank API by its id
    ## Parameters (required):
    - id [string]: object unique id. ex: "5656565656565656"
    ## Parameters (optional):
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call.
    ## Return:
    - corporateholder.Log object with updated attributes
    """
    return rest.get_id(resource=_resource, id=id, user=user)


def query(limit=None, after=None, before=None, types=None, holder_ids=None, ids=None, user=None):
    """# Retrieve corporateholder.Log
    Receive a generator of corporateholder.Log objects previously created in the Stark Bank API
    ## Parameters (optional):
    - limit [integer, default None]: maximum number of objects to be retrieved. Unlimited if None. ex: 35
    - after [datetime.date or string, default None] date filter for objects created only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None] date filter for objects created only before specified date. ex: datetime.date(2020, 3, 10)
    - types [list of strings, default None]: filter for log event types. ex: ["created", "blocked"]
    - holder_ids [list of strings, default None]: list of CorporateHolder ids to filter logs. ex: ["5656565656565656", "4545454545454545"]
    - ids [list of strings, default None]: list of ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call.
    ## Return:
    - generator of corporateholder.Log objects with updated attributes
    """
    return rest.get_stream(
        resource=_resource,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        types=types,
        holder_ids=holder_ids,
        ids=ids,
        user=user,
    )


def page(cursor=None, limit=None, after=None, before=None, types=None, holder_ids=None, ids=None, user=None):
    """# Retrieve paged corporateholder.Log
    Receive a list of up to 100 corporateholder.Log objects previously created in the Stark Bank API and the cursor to the next page.
    Use this function instead of query if you want to manually page your requests.
    ## Parameters (optional):
    - cursor [string, default None]: cursor returned on the previous page function call
    - limit [integer, default 100]: maximum number of objects to be retrieved. It must be an integer between 1 and 100. ex: 50
    - after [datetime.date or string, default None] date filter for objects created only after specified date. ex: datetime.date(2020, 3, 10)
    - before [datetime.date or string, default None] date filter for objects created only before specified date. ex: datetime.date(2020, 3, 10)
    - types [list of strings, default None]: filter for log event types. ex: ["created", "blocked"]
    - holder_ids [list of strings, default None]: list of CorporateHolder ids to filter logs. ex: ["5656565656565656", "4545454545454545"]
    - ids [list of strings, default None]: list of ids to filter retrieved objects. ex: ["5656565656565656", "4545454545454545"]
    - user [Organization/Project object, default None]: Organization or Project object. Not necessary if starkbank.user was set before function call.
    ## Return:
    - list of corporateholder.Log objects with updated attributes
    - cursor to retrieve the next page of corporateholder.Log objects
    """
    return rest.get_page(
        resource=_resource,
        cursor=cursor,
        ids=ids,
        limit=limit,
        after=check_date(after),
        before=check_date(before),
        types=types,
        holder_ids=holder_ids,
        user=user,
    )