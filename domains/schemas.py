from marshmallow import Schema, post_dump
from marshmallow import fields as ma_fields

from core.schemas import (
    GroupBySchema,
    GroupBysSchema,
    MetaSchema,
    NumberIdSchema,
    hide_relevance,
    relevance_score,
)


class DomainsSchema(Schema):
    id = ma_fields.Int()
    display_name = ma_fields.Str()
    fields = ma_fields.Nested(NumberIdSchema, many=True)
    relevance_score = ma_fields.Method("get_relevance_score")
    works_count = ma_fields.Int()
    cited_by_count = ma_fields.Int()
    works_api_url = ma_fields.Str()
    updated_date = ma_fields.Str()
    created_date = ma_fields.Str(dump_default=None)

    @post_dump
    def remove_relevance_score(self, data, many, **kwargs):
        return hide_relevance(data, self.context)

    @staticmethod
    def get_relevance_score(obj):
        return relevance_score(obj)

    class Meta:
        ordered = True


class MessageSchema(Schema):
    meta = ma_fields.Nested(MetaSchema)
    results = ma_fields.Nested(DomainsSchema, many=True)
    group_by = ma_fields.Nested(GroupBySchema, many=True)
    group_bys = ma_fields.Nested(GroupBysSchema, many=True)

    class Meta:
        ordered = True
