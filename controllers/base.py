from utils.orm_utils import session

class BaseController():
    def __init__(self, model, schema):
        self.model = model
        self.schema = schema

    def create(self, data: dict):
        model_obj = self.schema().load(data=data, session=session)
        session.add(model_obj)
        session.commit()
        session.close()
        return model_obj
    
    def create_many(self, data: list[dict]):
        model_objs = self.schema(many=True).load(data=data, session=session)
        session.add_all(model_objs)
        session.commit()
        session.close()
        return model_objs
    
    def get_one(self, id: int):
        model_obj = session.query(self.model).get(id)
        return model_obj
    
    def get_one_with_filter(self, **kwargs):
        model_obj = session.query(self.model).filter_by(**kwargs).first()
        return model_obj