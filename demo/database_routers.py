class CMSRouter:
    """
    Router to control all database operations on models in the cms application.
    """
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'cms_app':
            return 'cms_db'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'cms_app':
            return 'cms_db'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        return True  # Allow relations between the two databases

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'cms_app':
            return db == 'cms_db'
        return db == 'default'