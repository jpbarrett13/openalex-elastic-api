from core.fields import (BooleanField, DateField, OpenAlexIDField, PhraseField,
                         RangeField, SearchField, TermField)

fields = [
    BooleanField(param="is_oa", alias="open_access.is_oa"),
    BooleanField(param="is_paratext"),
    BooleanField(param="is_retracted"),
    BooleanField(param="open_access.is_oa"),
    DateField(
        param="from_publication_date",
        custom_es_field="publication_date",
    ),
    DateField(param="publication_date"),
    DateField(
        param="to_publication_date",
        custom_es_field="publication_date",
    ),
    OpenAlexIDField(param="alternate_host_venues.id"),
    OpenAlexIDField(param="author.id", alias="authorships.author.id"),
    OpenAlexIDField(param="authorships.author.id"),
    OpenAlexIDField(param="authorships.institutions.id"),
    OpenAlexIDField(param="cites", alias="referenced_works"),
    OpenAlexIDField(param="concept.id", alias="concepts.id"),
    OpenAlexIDField(param="concepts.id"),
    OpenAlexIDField(param="host_venue.id"),
    OpenAlexIDField(param="institution.id", alias="authorships.institutions.id"),
    OpenAlexIDField(param="institutions.id", alias="authorships.institutions.id"),
    OpenAlexIDField(param="journal.id", alias="host_venue.id"),
    OpenAlexIDField(param="referenced_works"),
    PhraseField(param="host_venue.publisher"),
    RangeField(param="cited_by_count"),
    RangeField(param="publication_year"),
    SearchField(param="display_name.search"),
    SearchField(param="title.search"),
    TermField(param="alternate_host_venues.license"),
    TermField(param="alternate_host_venues.version"),
    TermField(param="author.orcid", alias="authorships.author.orcid"),
    TermField(param="authorships.author.orcid"),
    TermField(param="authorships.institutions.country_code"),
    TermField(param="authorships.institutions.ror"),
    TermField(param="authorships.institutions.type"),
    TermField(param="concepts.wikidata"),
    TermField(param="display_name"),
    TermField(param="host_venue.issn"),
    TermField(
        param="institutions.country_code", alias="authorships.institutions.country_code"
    ),
    TermField(param="institutions.ror", alias="authorships.institutions.ror"),
    TermField(param="institutions.type", alias="authorships.institutions.type"),
    TermField(param="oa_status", alias="open_access.oa_status"),
    TermField(param="open_access.oa_status"),
    TermField(param="type"),
]

fields_dict = {f.param: f for f in fields}
