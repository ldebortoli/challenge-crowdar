from marshmallow import Schema, fields, post_load


class SmallCategorySchema(Schema):
    label = fields.Str(required=True)
    permalink = fields.Str(required=True)


class ChildrenCategorySchema(Schema):
    id = fields.Str(required=True)
    name = fields.Str()
    permalink = fields.Str(required=True)


class CategorySchema(Schema):
    id = fields.Str(required=True)
    name = fields.Str(required=True)
    permalink = fields.Str(required=True)
    children_categories = fields.List(fields.Nested(ChildrenCategorySchema, required=True))


class DepartmentSchema(Schema):
    name = fields.Str()
    categories = fields.List(fields.Nested(CategorySchema, required=True))


class MenuDepartmentsResponse:
    def __init__(self, departments, landings, more_categories, high_priority):
        self.departments = departments
        self.landings = landings
        self.more_categories = more_categories
        self.high_priority = high_priority


class MenuDepartmentsResponseSchema(Schema):
    departments = fields.List(fields.Nested(DepartmentSchema, required=True))
    landings = fields.List(fields.Nested(SmallCategorySchema, required=True))
    more_categories = fields.Nested(SmallCategorySchema, required=True)
    high_priority = fields.List(fields.Nested(SmallCategorySchema, required=True))

    @post_load
    def make_object(self, data, **kwargs):
        return MenuDepartmentsResponse(**data)
