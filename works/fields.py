from core.fields import (BooleanField, DateField, OpenAlexIDField, PhraseField,
                         RangeField, SearchField, TermField)

fields = [
    BooleanField(
        param=f"authorships.institutions.is_global_south",
        custom_es_field="authorships.institutions.country_code",
        nested=True,
    ),
    BooleanField(
        param=f"institutions.is_global_south",
        custom_es_field="authorships.institutions.country_code",
        nested=True,
    ),
    BooleanField(param="has_abstract", custom_es_field="abstract"),
    BooleanField(param="has_doi", custom_es_field="ids.doi"),
    BooleanField(param="has_fulltext", custom_es_field="fulltext"),
    BooleanField(param="has_pmid", custom_es_field="ids.pmid"),
    BooleanField(param="has_pmcid", custom_es_field="ids.pmcid"),
    BooleanField(param="has_references", custom_es_field="referenced_works"),
    BooleanField(param="has_ngrams", custom_es_field="fulltext"),
    BooleanField(param="has_oa_accepted_or_published_version"),
    BooleanField(param="has_oa_submitted_version"),
    BooleanField(param="is_oa", alias="open_access.is_oa"),
    BooleanField(param="is_paratext"),
    BooleanField(param="is_retracted"),
    BooleanField(param="open_access.is_oa"),
    DateField(
        param="from_created_date",
        custom_es_field="created_date",
    ),
    DateField(
        param="from_publication_date",
        custom_es_field="publication_date",
    ),
    DateField(
        param="from_updated_date",
        custom_es_field="updated_date",
    ),
    DateField(param="publication_date"),
    DateField(
        param="to_publication_date",
        custom_es_field="publication_date",
    ),
    OpenAlexIDField(param="alternate_host_venues.id"),
    OpenAlexIDField(param="author.id", alias="authorships.author.id", nested=True),
    OpenAlexIDField(param="authorships.author.id", nested=True),
    OpenAlexIDField(param="authorships.institutions.id", nested=True),
    OpenAlexIDField(param="cited_by"),
    OpenAlexIDField(param="cites", alias="referenced_works"),
    OpenAlexIDField(param="concept.id", alias="concepts.id"),
    OpenAlexIDField(param="concepts.id"),
    OpenAlexIDField(param="host_venue.id"),
    OpenAlexIDField(param="ids.openalex"),
    OpenAlexIDField(
        param="institution.id", alias="authorships.institutions.id", nested=True
    ),
    OpenAlexIDField(
        param="institutions.id", alias="authorships.institutions.id", nested=True
    ),
    OpenAlexIDField(param="journal.id", alias="host_venue.id"),
    OpenAlexIDField(param="openalex", custom_es_field="ids.openalex.lower"),
    OpenAlexIDField(param="openalex_id", alias="ids.openalex"),
    OpenAlexIDField(param="repository"),
    OpenAlexIDField(param="referenced_works"),
    OpenAlexIDField(param="related_to"),
    PhraseField(param="host_venue.publisher"),
    RangeField(param="cited_by_count"),
    RangeField(param="publication_year"),
    SearchField(param="abstract.search", custom_es_field="abstract"),
    SearchField(param="display_name.search"),
    SearchField(param="fulltext.search", custom_es_field="fulltext"),
    SearchField(
        param="raw_affiliation_string.search",
        custom_es_field="authorships.raw_affiliation_string",
        nested=True,
    ),
    SearchField(param="title.search"),
    TermField(param="alternate_host_venues.license"),
    TermField(param="alternate_host_venues.version"),
    TermField(param="author.orcid", alias="authorships.author.orcid", nested=True),
    TermField(param="authorships.author.orcid", nested=True),
    TermField(param="authorships.institutions.country_code", nested=True),
    TermField(
        param=f"authorships.institutions.continent",
        custom_es_field="authorships.institutions.country_code",
        nested=True,
    ),
    TermField(param="authorships.institutions.ror", nested=True),
    TermField(param="authorships.institutions.type", nested=True),
    TermField(param="concepts.wikidata"),
    TermField(param="display_name", custom_es_field="display_name.lower"),
    TermField(param="doi", alias="ids.doi"),
    TermField(param="doi_starts_with", custom_es_field="ids.doi"),
    TermField(param="ids.mag", custom_es_field="ids.mag"),
    TermField(param="ids.pmid", custom_es_field="ids.pmid"),
    TermField(param="ids.pmcid", custom_es_field="ids.pmcid"),
    TermField(
        param="host_venue.display_name", custom_es_field="host_venue.display_name"
    ),
    TermField(param="host_venue.issn"),
    TermField(param="host_venue.license", custom_es_field="host_venue.license"),
    TermField(param="host_venue.type", custom_es_field="host_venue.type"),
    TermField(
        param="institutions.country_code",
        alias="authorships.institutions.country_code",
        nested=True,
    ),
    TermField(
        param="institutions.continent",
        alias="authorships.institutions.country_code",
        nested=True,
    ),
    TermField(
        param="institutions.ror", alias="authorships.institutions.ror", nested=True
    ),
    TermField(
        param="institutions.type", alias="authorships.institutions.type", nested=True
    ),
    TermField(param="mag", custom_es_field="ids.mag"),
    TermField(param="oa_status", alias="open_access.oa_status"),
    TermField(param="open_access.oa_status"),
    TermField(param="pmid", custom_es_field="ids.pmid"),
    TermField(param="pmcid", custom_es_field="ids.pmcid"),
    TermField(param="type"),
    TermField(param="version", custom_es_field="host_venue.version"),
]

fields_dict = {f.param: f for f in fields}
