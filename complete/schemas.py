from marshmallow import Schema, fields

from core.schemas import GroupBySchema, MetaSchema


class CompleteSchema(Schema):
    id = fields.Str()
    display_name = fields.Str()
    cited_by_count = fields.Int()
    entity_type = fields.Method("get_entity_type", dump_default=None)
    external_id = fields.Method("get_external_id", dump_default=None)

    def get_entity_type(self, obj):
        entities = {
            "authors": "author",
            "concepts": "concept",
            "institutions": "institution",
            "venues": "venue",
            "works": "work",
        }
        for key, value in entities.items():
            if key in obj.meta.index:
                return value

    def get_external_id(self, obj):
        entities = {
            "authors": "orcid",
            "concepts": "wikidata",
            "institutions": "ror",
            "venues": "issn_l",
            "works": "doi",
        }
        for key, value in entities.items():
            if key in obj.meta.index:
                return getattr(obj, value)

    class Meta:
        ordered = True


class MessageSchema(Schema):
    meta = fields.Nested(MetaSchema)
    results = fields.Nested(CompleteSchema, many=True)
    group_by = fields.Nested(GroupBySchema, many=True)

    class Meta:
        ordered = True
