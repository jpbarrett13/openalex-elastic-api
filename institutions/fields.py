from core.fields import (BooleanField, DateField, OpenAlexIDField, RangeField,
                         SearchField, TermField)

fields = [
    BooleanField(
        param=f"country.is_global_south",
        custom_es_field="country_code",
    ),
    BooleanField(param="has_ror", custom_es_field="ids.ror.keyword"),
    DateField(
        param="from_created_date",
        custom_es_field="created_date",
    ),
    DateField(
        param="from_updated_date",
        custom_es_field="updated_date",
    ),
    OpenAlexIDField(param="concepts.id", custom_es_field="x_concepts.id"),
    OpenAlexIDField(param="openalex", custom_es_field="ids.openalex.lower"),
    OpenAlexIDField(param="openalex_id", alias="ids.openalex"),
    OpenAlexIDField(param="x_concepts.id"),
    RangeField(param="cited_by_count"),
    RangeField(param="works_count"),
    SearchField(param="display_name.search"),
    TermField(param="country_code"),
    TermField(
        param=f"country.continent",
        custom_es_field="country_code",
    ),
    TermField(param="display_name", custom_es_field="display_name.keyword"),
    TermField(param="ror", alias="ror"),
    TermField(param="type"),
]

fields_dict = {f.param: f for f in fields}
