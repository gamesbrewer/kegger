from google.appengine.ext import ndb

class Users(ndb.Model):
    password = ndb.StringProperty(required=True)
    full_name = ndb.StringProperty(required=True)
    phone_no = ndb.StringProperty(required=False)
    timestamp = ndb.DateTimeProperty(auto_now_add=True)

    @classmethod
    def query_user(cls, ancestor_key):
       return cls.query(ancestor=ancestor_key).order(cls.full_name)

    @classmethod
    def user_key(cls, user_email):
       return ndb.Key('pyramidmyappname_User', user_email)