class PrimaryRouter:
    def db_for_read(self, model, **hints):
        return 'primary_db'

    def db_for_write(self, model, **hints):
        return 'primary_db'

    def allow_relation(self, obj1, obj2, **hints):
        db_set = {'primary_db'}
        print('***********', obj1._state.db, obj2._state.db)
        if obj1._state.db in db_set and obj2._state.db in db_set:
            return True
        return False

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return True
