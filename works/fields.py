from core.fields import (
    BooleanField,
    DateField,
    DateTimeField,
    OpenAlexIDField,
    RangeField,
    SearchField,
    TermField,
)
from core.alternate_names import ALTERNATE_NAMES

# shared docstrings for when multiple fields share the same docstring (such as aliases)
DOCSTRINGS = {
    "is_global_south": "The work has affiliated institutions located in the Global South. The Global South is a term used to identify regions within Latin America, Asia, Africa, and Oceania.",
    "corresponding_authors": "The work's corresponding author(s)",
    "is_corresponding": "The work has corresponding author information available",
    "is_oa": "The work is Open Access, meaning that you can read the full text without needing to pay money or log in",
    "source.is_oa": "The work is in a source that is Open Access. This is different than whether the work itself is Open Access, because the OA status of a source can change",
    "source.is_in_doaj": "The work is published in a journal that is in DOAJ, the Directory of Open Access Journals",
    "is_accepted": "The work has {location_type} that has been accepted for publication",
    "is_published": "The work has {location_type} that has been published",
    "has_abstract": "Abstract is available for the work",
    "has_doi": "The work has a DOI (Digital Object Identifier). Usually, this means that a work has been indexed by Crossref.",
    "has_fulltext": "The work has full text available to search",
    "has_orcid": "The work has at least one author with an ORCID",
    "has_pmid": "The work is in PubMed",
    "has_pmcid": "The work is in PubMed Central",
    "has_references": "The work has references, also known as outgoing citations",
    "is_paratext": 'We have marked the work as "paratext". Paratext means things like front/back cover, table of contents, and issue information.',
    "is_retracted": "The work has been retracted",
    "source.issn": "The work's journal, by ISSN",
    "source.type": "The type of source for the work. For example, you can filter for only works in journals, or in repositories.",
    "sustainable_development_goals": "The work's relevance to one or more of the United Nations' Sustainable Development Goals",
    "type": 'Most works are type "Article". You can also filter for books, editorials, and more.',
    "any_repository_has_fulltext": "The work’s full text is free in an Open Access repository",
    "publication_date": "The date the work was published",
    "author": "The authors of a work",
    "institution": "The institutional affiliations claimed by the authors of a work",
    "corresponding_institutions": "The institutions to which the corresponding author(s) of a work claim affiliation",
    "source": "Sources are where works are hosted, such as journals, conferences, and repositories",
    "publisher": "Publishers are companies or organizations behind the source where a work is available (such as a journal).",
    "repository": "The repositories that the work is available in",
    "license": "A work or version of a work may have an Open Access license, such as a Creative Commons license, or a publisher-specific license",
    "language": "The primary language the work is written in (as detected from titles and abstracts)",
    "cited_by": "The work's outgoing citations, or references",
    "cites": "The work's incoming citations",
    "country": "The countries represented among the work's authors' affiliations",
    "continent": "The continents represented among the work's institutions",
}

# shared documentation_links for when multiple fields share the same link (such as aliases)
DOCUMENTATION_LINKS = {
    "is_global_south": "https://docs.openalex.org/api-entities/geo/regions",
    "corresponding_authors": "https://docs.openalex.org/api-entities/works/work-object/authorship-object#is_corresponding",
    "is_corresponding": "https://docs.openalex.org/api-entities/works/work-object/authorship-object#is_corresponding",
    "is_oa": "https://docs.openalex.org/api-entities/works/work-object#is_oa-1",
    "source.is_oa": "https://docs.openalex.org/api-entities/sources/source-object#is_oa",
    "source.is_in_doaj": "https://docs.openalex.org/api-entities/sources/source-object#is_in_doaj",
    "is_accepted": "https://docs.openalex.org/api-entities/works/work-object/location-object#is_accepted",
    "is_published": "https://docs.openalex.org/api-entities/works/work-object/location-object#is_published",
    "has_abstract": "https://docs.openalex.org/api-entities/works/filter-works#has_abstract",
    "has_doi": "https://docs.openalex.org/api-entities/works/work-object#doi",
    "has_fulltext": "https://docs.openalex.org/api-entities/works/work-object#has_fulltext",
    "has_orcid": "https://docs.openalex.org/api-entities/authors/author-object#orcid",
    "has_pmid": "https://docs.openalex.org/api-entities/works/filter-works#has_pmid",
    "has_pmcid": "https://docs.openalex.org/api-entities/works/filter-works#has_pmcid",
    "has_references": "https://docs.openalex.org/api-entities/works/filter-works#has_references",
    "is_paratext": "https://docs.openalex.org/api-entities/works/work-object#is_paratext",
    "is_retracted": "https://docs.openalex.org/api-entities/works/work-object#is_retracted",
    "source.issn": "https://docs.openalex.org/api-entities/sources/source-object#issn_l",
    "source.type": "https://docs.openalex.org/api-entities/sources/source-object#type",
    "sustainable_development_goals": "https://docs.openalex.org/api-entities/works/work-object#sustainable_development_goals",
    "type": "https://docs.openalex.org/api-entities/works/work-object#type",
    "any_repository_has_fulltext": "https://docs.openalex.org/api-entities/works/work-object#any_repository_has_fulltext",
    "publication_date": "https://docs.openalex.org/api-entities/works/work-object#publication_date",
    "author": "https://docs.openalex.org/api-entities/authors",
    "institution": "https://docs.openalex.org/api-entities/institutions",
    "corresponding_institutions": "https://docs.openalex.org/api-entities/works/work-object#corresponding_institution_ids",
    "source": "https://docs.openalex.org/api-entities/sources",
    "publisher": "https://docs.openalex.org/api-entities/publishers",
    "repository": "https://docs.openalex.org/api-entities/works/filter-works#repository",
    "license": "https://docs.openalex.org/api-entities/works/work-object/location-object#license",
    "language": "https://docs.openalex.org/api-entities/works/work-object#language",
    "cited_by": "https://docs.openalex.org/api-entities/works/filter-works#cited_by",
    "cites": "https://docs.openalex.org/api-entities/works/filter-works#cites",
    "country": "https://docs.openalex.org/api-entities/institutions/institution-object#country_code",
    "continent": "https://docs.openalex.org/api-entities/geo/continents",
}

fields = [
    BooleanField(
        param=f"authorships.institutions.is_global_south",
        custom_es_field="authorships.institutions.country_code",
        docstring=DOCSTRINGS["is_global_south"],
        documentation_link=DOCUMENTATION_LINKS["is_global_south"],
        alternate_names=ALTERNATE_NAMES.get("is_global_south", None),
    ),
    BooleanField(
        param="authorships.is_corresponding",
        docstring=DOCSTRINGS["corresponding_authors"],
        documentation_link=DOCUMENTATION_LINKS["corresponding_authors"],
        alternate_names=ALTERNATE_NAMES.get("corresponding_authors", None),
    ),
    BooleanField(
        param="best_oa_location.is_oa",
        docstring=DOCSTRINGS["is_oa"],
        documentation_link=DOCUMENTATION_LINKS["is_oa"],
        alternate_names=ALTERNATE_NAMES.get("is_oa", None),
    ),
    BooleanField(
        param="best_oa_location.source.is_oa",
        docstring=DOCSTRINGS["source.is_oa"],
        documentation_link=DOCUMENTATION_LINKS["source.is_oa"],
        alternate_names=ALTERNATE_NAMES.get("source.is_oa", None),
    ),
    BooleanField(
        param="best_oa_location.source.is_in_doaj",
        docstring=DOCSTRINGS["source.is_in_doaj"],
        documentation_link=DOCUMENTATION_LINKS["source.is_in_doaj"],
        alternate_names=ALTERNATE_NAMES.get("source.is_in_doaj", None),
    ),
    BooleanField(
        param="best_oa_location.is_accepted",
        docstring=DOCSTRINGS["is_accepted"].format(
            location_type="an Open Access version"
        ),
        documentation_link=DOCUMENTATION_LINKS["is_accepted"],
        alternate_names=ALTERNATE_NAMES.get("is_accepted", None),
    ),
    BooleanField(
        param="best_oa_location.is_published",
        docstring=DOCSTRINGS["is_published"].format(
            location_type="an Open Access Version"
        ),
        documentation_link=DOCUMENTATION_LINKS["is_published"],
        alternate_names=ALTERNATE_NAMES.get("is_published", None),
    ),
    BooleanField(
        param="has_abstract",
        custom_es_field="abstract",
        docstring=DOCSTRINGS["has_abstract"],
        documentation_link=DOCUMENTATION_LINKS["has_abstract"],
        alternate_names=ALTERNATE_NAMES.get("has_abstract", None),
    ),
    BooleanField(
        param="has_doi",
        custom_es_field="ids.doi",
        docstring=DOCSTRINGS["has_doi"],
        documentation_link=DOCUMENTATION_LINKS["has_doi"],
        alternate_names=ALTERNATE_NAMES.get("has_doi", None),
    ),
    BooleanField(
        param="has_fulltext",
        docstring=DOCSTRINGS["has_fulltext"],
        documentation_link=DOCUMENTATION_LINKS["has_fulltext"],
        alternate_names=ALTERNATE_NAMES.get("has_fulltext", None),
    ),
    BooleanField(
        param="has_orcid",
        custom_es_field="authorships.author.orcid",
        docstring=DOCSTRINGS["has_orcid"],
        documentation_link=DOCUMENTATION_LINKS["has_orcid"],
        alternate_names=ALTERNATE_NAMES.get("has_orcid", None),
    ),
    BooleanField(
        param="has_pmid",
        custom_es_field="ids.pmid",
        docstring=DOCSTRINGS["has_pmid"],
        documentation_link=DOCUMENTATION_LINKS["has_pmid"],
        alternate_names=ALTERNATE_NAMES.get("has_pmid", None),
    ),
    BooleanField(
        param="has_pmcid",
        custom_es_field="ids.pmcid",
        docstring=DOCSTRINGS["has_pmcid"],
        documentation_link=DOCUMENTATION_LINKS["has_pmcid"],
        alternate_names=ALTERNATE_NAMES.get("has_pmcid", None),
    ),
    BooleanField(
        param="has_references",
        custom_es_field="referenced_works",
        docstring=DOCSTRINGS["has_references"],
        documentation_link=DOCUMENTATION_LINKS["has_references"],
        alternate_names=ALTERNATE_NAMES.get("has_references", None),
    ),
    BooleanField(
        param="has_ngrams",
        custom_es_field="fulltext",
        docstring=DOCSTRINGS["has_fulltext"],
        documentation_link=DOCUMENTATION_LINKS["has_fulltext"],
        alternate_names=ALTERNATE_NAMES.get("has_fulltext", None),
    ),
    BooleanField(param="has_oa_accepted_or_published_version"),
    BooleanField(param="has_oa_submitted_version"),
    BooleanField(
        param="has_old_authors",
        custom_es_field="authorships.uthor.id",
    ),
    BooleanField(param="has_pdf_url", custom_es_field="locations.pdf_url"),
    BooleanField(
        param="has_raw_affiliation_string",
        custom_es_field="authorships.raw_affiliation_strings",
    ),
    BooleanField(
        param="institutions.is_global_south",
        custom_es_field="authorships.institutions.country_code",
        docstring=DOCSTRINGS["is_global_south"],
        documentation_link=DOCUMENTATION_LINKS["is_global_south"],
        alternate_names=ALTERNATE_NAMES.get("is_global_south", None),
    ),
    BooleanField(
        param="is_corresponding",
        custom_es_field="authorships.is_corresponding",
        docstring=DOCSTRINGS["is_corresponding"],
        documentation_link=DOCUMENTATION_LINKS["is_corresponding"],
        alternate_names=ALTERNATE_NAMES.get("is_corresponding", None),
    ),
    BooleanField(
        param="is_oa",
        alias="open_access.is_oa",
        docstring=DOCSTRINGS["is_oa"],
        documentation_link=DOCUMENTATION_LINKS["is_oa"],
        alternate_names=ALTERNATE_NAMES.get("is_oa", None),
    ),
    BooleanField(
        param="is_paratext",
        docstring=DOCSTRINGS["is_paratext"],
        documentation_link=DOCUMENTATION_LINKS["is_paratext"],
        alternate_names=ALTERNATE_NAMES.get("is_paratext", None),
    ),
    BooleanField(
        param="is_retracted",
        docstring=DOCSTRINGS["is_retracted"],
        documentation_link=DOCUMENTATION_LINKS["is_retracted"],
        alternate_names=ALTERNATE_NAMES.get("is_retracted", None),
    ),
    BooleanField(
        param="locations.is_oa",
        docstring=DOCSTRINGS["is_oa"],
        documentation_link=DOCUMENTATION_LINKS["is_oa"],
        alternate_names=ALTERNATE_NAMES.get("is_oa", None),
    ),
    BooleanField(
        param="locations.source.is_oa",
        docstring=DOCSTRINGS["source.is_oa"],
        documentation_link=DOCUMENTATION_LINKS["source.is_oa"],
        alternate_names=ALTERNATE_NAMES.get("source.is_oa", None),
    ),
    BooleanField(
        param="locations.source.has_issn", custom_es_field="locations.source.issn"
    ),
    BooleanField(
        param="locations.source.is_in_doaj",
        docstring=DOCSTRINGS["source.is_in_doaj"],
        documentation_link=DOCUMENTATION_LINKS["source.is_in_doaj"],
        alternate_names=ALTERNATE_NAMES.get("source.is_in_doaj", None),
    ),
    BooleanField(
        param="locations.is_accepted",
        docstring=DOCSTRINGS["is_accepted"].format(
            location_type="at least one version"
        ),
        documentation_link=DOCUMENTATION_LINKS["is_accepted"],
        alternate_names=ALTERNATE_NAMES.get("is_accepted", None),
    ),
    BooleanField(
        param="locations.is_published",
        docstring=DOCSTRINGS["is_published"].format(
            location_type="at least one version"
        ),
        documentation_link=DOCUMENTATION_LINKS["is_published"],
        alternate_names=ALTERNATE_NAMES.get("is_published", None),
    ),
    BooleanField(
        param="open_access.is_oa",
        docstring=DOCSTRINGS["is_oa"],
        documentation_link=DOCUMENTATION_LINKS["is_oa"],
        alternate_names=ALTERNATE_NAMES.get("is_oa", None),
    ),
    BooleanField(
        param="open_access.any_repository_has_fulltext",
        docstring=DOCSTRINGS["any_repository_has_fulltext"],
        documentation_link=DOCUMENTATION_LINKS["any_repository_has_fulltext"],
        alternate_names=ALTERNATE_NAMES.get("any_repository_has_fulltext", None),
    ),
    BooleanField(
        param="primary_location.is_oa",
        docstring=DOCSTRINGS["is_oa"],
        documentation_link=DOCUMENTATION_LINKS["is_oa"],
        alternate_names=ALTERNATE_NAMES.get("is_oa", None),
    ),
    BooleanField(
        param="primary_location.source.is_oa",
        docstring=DOCSTRINGS["source.is_oa"],
        documentation_link=DOCUMENTATION_LINKS["source.is_oa"],
        alternate_names=ALTERNATE_NAMES.get("source.is_oa", None),
    ),
    BooleanField(
        param="primary_location.source.is_in_doaj",
        docstring=DOCSTRINGS["source.is_in_doaj"],
        documentation_link=DOCUMENTATION_LINKS["source.is_in_doaj"],
        alternate_names=ALTERNATE_NAMES.get("source.is_in_doaj", None),
    ),
    BooleanField(
        param="primary_location.is_accepted",
        docstring=DOCSTRINGS["is_accepted"].format(location_type="a version"),
        documentation_link=DOCUMENTATION_LINKS["is_accepted"],
        alternate_names=ALTERNATE_NAMES.get("is_accepted", None),
    ),
    BooleanField(
        param="primary_location.is_published",
        docstring=DOCSTRINGS["is_published"].format(location_type="a version"),
        documentation_link=DOCUMENTATION_LINKS["is_published"],
        alternate_names=ALTERNATE_NAMES.get("is_published", None),
    ),
    BooleanField(
        param="primary_location.source.has_issn",
        custom_es_field="primary_location.source.issn",
    ),
    DateField(
        param="from_created_date",
        custom_es_field="created_date",
    ),
    DateField(
        param="from_publication_date",
        custom_es_field="publication_date",
        docstring=DOCSTRINGS["publication_date"],
        documentation_link=DOCUMENTATION_LINKS["publication_date"],
        alternate_names=ALTERNATE_NAMES.get("publication_date", None),
    ),
    DateTimeField(
        param="from_updated_date",
        custom_es_field="updated_date",
    ),
    DateTimeField(
        param="to_updated_date",
        custom_es_field="updated_date",
    ),
    DateField(
        param="publication_date",
        docstring=DOCSTRINGS["publication_date"],
        documentation_link=DOCUMENTATION_LINKS["publication_date"],
        alternate_names=ALTERNATE_NAMES.get("publication_date", None),
    ),
    DateField(
        param="to_publication_date",
        custom_es_field="publication_date",
        docstring=DOCSTRINGS["publication_date"],
        documentation_link=DOCUMENTATION_LINKS["publication_date"],
        alternate_names=ALTERNATE_NAMES.get("publication_date", None),
    ),
    OpenAlexIDField(
        param="author.id",
        alias="authorships.author.id",
        docstring=DOCSTRINGS["author"],
        documentation_link=DOCUMENTATION_LINKS["author"],
        alternate_names=ALTERNATE_NAMES.get("author", None),
    ),
    OpenAlexIDField(
        param="authorships.author.id",
        docstring=DOCSTRINGS["author"],
        documentation_link=DOCUMENTATION_LINKS["author"],
        alternate_names=ALTERNATE_NAMES.get("author", None),
    ),
    OpenAlexIDField(
        param="authorships.institutions.id",
        docstring=DOCSTRINGS["institution"],
        documentation_link=DOCUMENTATION_LINKS["institution"],
        alternate_names=ALTERNATE_NAMES.get("institution", None),
    ),
    OpenAlexIDField(
        param="authorships.institutions.lineage",
        custom_es_field="authorships.institutions.lineage",
    ),
    OpenAlexIDField(
        param="corresponding_author_ids",
        docstring=DOCSTRINGS["corresponding_authors"],
        documentation_link=DOCUMENTATION_LINKS["corresponding_authors"],
        alternate_names=ALTERNATE_NAMES.get("corresponding_authors", None),
    ),
    OpenAlexIDField(
        param="corresponding_institution_ids",
        docstring=DOCSTRINGS["corresponding_institutions"],
        documentation_link=DOCUMENTATION_LINKS["corresponding_institutions"],
        alternate_names=ALTERNATE_NAMES.get("corresponding_institutions", None),
    ),
    OpenAlexIDField(param="best_oa_location.source.id"),
    OpenAlexIDField(param="best_oa_location.source.host_organization"),
    OpenAlexIDField(param="best_oa_location.source.host_organization_lineage"),
    OpenAlexIDField(
        param="cited_by",
        docstring=DOCSTRINGS["cited_by"],
        documentation_link=DOCUMENTATION_LINKS["cited_by"],
        alternate_names=ALTERNATE_NAMES.get("cited_by", None),
    ),
    OpenAlexIDField(
        param="cites",
        alias="referenced_works",
        docstring=DOCSTRINGS["cites"],
        documentation_link=DOCUMENTATION_LINKS["cites"],
        alternate_names=ALTERNATE_NAMES.get("cites", None),
    ),
    OpenAlexIDField(param="concept.id", alias="concepts.id"),
    OpenAlexIDField(
        param="concepts.id",
        docstring="Concepts are abstract ideas that the work is about",
        documentation_link="https://docs.openalex.org/api-entities/concepts",
    ),
    OpenAlexIDField(
        param="grants.funder",
        docstring="The funders listed in the work's grants",
        documentation_link="https://docs.openalex.org/api-entities/funders",
    ),
    OpenAlexIDField(param="host_venue.id"),
    OpenAlexIDField(
        param="ids.openalex",
        docstring="The OpenAlex ID for a work",
        documentation_link="https://docs.openalex.org/how-to-use-the-api/get-single-entities#the-openalex-id",
    ),
    OpenAlexIDField(param="institution.id", alias="authorships.institutions.id"),
    OpenAlexIDField(param="institutions.id", alias="authorships.institutions.id"),
    OpenAlexIDField(param="journal", custom_es_field="primary_location.source.id"),
    OpenAlexIDField(
        param="locations.source.id",
        docstring=DOCSTRINGS["source"],
        documentation_link=DOCUMENTATION_LINKS["source"],
        alternate_names=ALTERNATE_NAMES.get("source", None),
    ),
    OpenAlexIDField(
        param="locations.source.host_institution_lineage",
        custom_es_field="locations.source.host_organization_lineage",
    ),
    OpenAlexIDField(param="locations.source.host_organization"),
    OpenAlexIDField(param="locations.source.host_organization_lineage"),
    OpenAlexIDField(
        param="locations.source.publisher_lineage",
        custom_es_field="locations.source.host_organization_lineage",
    ),
    OpenAlexIDField(
        param="primary_location.source.host_institution_lineage",
        custom_es_field="primary_location.source.host_organization_lineage",
    ),
    OpenAlexIDField(
        param="primary_location.source.id",
        docstring=DOCSTRINGS["source"],
        documentation_link=DOCUMENTATION_LINKS["source"],
        alternate_names=ALTERNATE_NAMES.get("source", None),
    ),
    OpenAlexIDField(param="primary_location.source.host_organization"),
    OpenAlexIDField(param="primary_location.source.host_organization_lineage"),
    OpenAlexIDField(
        param="primary_location.source.publisher_lineage",
        custom_es_field="primary_location.source.host_organization_lineage",
        docstring=DOCSTRINGS["publisher"],
        documentation_link=DOCUMENTATION_LINKS["publisher"],
        alternate_names=ALTERNATE_NAMES.get("publisher", None),
    ),
    OpenAlexIDField(param="openalex", custom_es_field="ids.openalex.lower"),
    OpenAlexIDField(param="openalex_id", alias="ids.openalex"),
    OpenAlexIDField(
        param="repository",
        custom_es_field="locations.source.id",
        docstring=DOCSTRINGS["repository"],
        documentation_link=DOCUMENTATION_LINKS["repository"],
        alternate_names=ALTERNATE_NAMES.get("repository", None),
    ),
    OpenAlexIDField(
        param="referenced_works",
        docstring=DOCSTRINGS["cites"],
        documentation_link=DOCUMENTATION_LINKS["cites"],
        alternate_names=ALTERNATE_NAMES.get("cites", None),
    ),
    OpenAlexIDField(
        param="related_to",
        docstring="Related works, based on common concepts the works have.",
        documentation_link="https://docs.openalex.org/api-entities/works/work-object#related_works",
    ),
    RangeField(
        param="apc_list.value",
        documentation_link="https://docs.openalex.org/api-entities/works/work-object#apc_list",
        alternate_names=ALTERNATE_NAMES.get("apc", None),
    ),
    RangeField(
        param="apc_list.value_usd",
        docstring="The work's APC (article processing charge) <em>list</em> price (in USD). This is the price listed by the journal's publisher, which may be different than the paid price",
        documentation_link="https://docs.openalex.org/api-entities/works/work-object#apc_list",
        alternate_names=ALTERNATE_NAMES.get("apc", None),
    ),
    RangeField(
        param="apc_paid.value",
        documentation_link="https://docs.openalex.org/api-entities/works/work-object#apc_paid",
        alternate_names=ALTERNATE_NAMES.get("apc", None),
    ),
    RangeField(
        param="apc_paid.value_usd",
        docstring="The work's APC (article processing charge) <em>paid</em> price (in USD). In some cases, this is different from the journal's list price, and this difference is made public. Otherwise, we assume the paid price is the list price",
        documentation_link="https://docs.openalex.org/api-entities/works/work-object#apc_paid",
        alternate_names=ALTERNATE_NAMES.get("apc", None),
    ),
    RangeField(
        param="authors_count",
        docstring="The number of authors for the work",
        documentation_link="https://docs.openalex.org/api-entities/works/filter-works#authors_count",
        alternate_names=ALTERNATE_NAMES.get("author", None),
    ),
    RangeField(
        param="cited_by_count",
        docstring="The number of times the work has been cited by another work",
        documentation_link="https://docs.openalex.org/api-entities/works/work-object#cited_by_count",
        alternate_names=ALTERNATE_NAMES.get("cites", None),
    ),
    RangeField(
        param="cited_by_percentile_year.min",
        docstring="The minimum percentile rank for this work's citation count, compared to other works published in the same year",
    ),
    RangeField(
        param="cited_by_percentile_year.max",
        docstring="The maximum percentile rank for this work's citation count, compared to other works published in the same year",
    ),
    RangeField(param="concepts_count"),
    RangeField(
        param="countries_distinct_count",
        docstring="The number of distinct countries represented among the work's authors",
        documentation_link="https://docs.openalex.org/api-entities/works/work-object#countries_distinct_count",
    ),
    RangeField(param="institutions_distinct_count"),
    RangeField(
        param="locations_count",
        docstring="The number of distinct online locations we have found for the work",
        documentation_link="https://docs.openalex.org/api-entities/works/work-object/location-object",
    ),
    RangeField(
        param="publication_year",
        docstring=DOCSTRINGS["publication_date"],
        documentation_link=DOCUMENTATION_LINKS["publication_date"],
        alternate_names=ALTERNATE_NAMES.get("publication_date", None),
    ),
    RangeField(param="referenced_works_count"),
    RangeField(param="sustainable_development_goals.score"),
    SearchField(
        param="abstract.search",
        custom_es_field="abstract",
        docstring="Free text search within the work's abstract only",
        documentation_link="https://docs.openalex.org/api-entities/works/search-works#search-a-specific-field",
    ),
    SearchField(
        param="default.search",
        index="works",
        docstring="Free text search among the work's title, abstract (when available) and full text (when available)",
        documentation_link="https://docs.openalex.org/how-to-use-the-api/get-lists-of-entities/search-entities",
    ),
    SearchField(param="display_name.search"),
    SearchField(
        param="fulltext.search",
        custom_es_field="fulltext",
        docstring="Free text search within the work's full text (body) only",
        documentation_link="https://docs.openalex.org/api-entities/works/search-works#search-a-specific-field",
        alternate_names=["body", "full", "text"],
    ),
    SearchField(
        param="keyword.search",
        custom_es_field="keywords.keyword",
        docstring="Free text search within the work's keywords only",
        documentation_link="https://docs.openalex.org/api-entities/works/search-works#search-a-specific-field",
    ),
    SearchField(
        param="raw_affiliation_string.search",
        custom_es_field="authorships.raw_affiliation_string",
    ),
    SearchField(
        param="title.search",
        custom_es_field="display_name",
        docstring="Free text search within the work's title only",
        documentation_link="https://docs.openalex.org/api-entities/works/search-works#search-a-specific-field",
    ),
    SearchField(
        param="title_and_abstract.search",
        docstring="Free text search within the work's title and abstract",
        documentation_link="https://docs.openalex.org/api-entities/works/search-works#search-a-specific-field",
    ),
    TermField(param="apc_list.currency"),
    TermField(param="apc_list.provenance"),
    TermField(param="apc_paid.currency"),
    TermField(
        param="apc_paid.provenance",
        docstring="The source of our information about the work's APC. Works with OpenAPC data might have more accurate prices for APC paid.",
        documentation_link="https://docs.openalex.org/api-entities/works/work-object#apc_paid",
    ),
    TermField(param="author.orcid", alias="authorships.author.orcid"),
    TermField(
        param="authorships.author.orcid",
        docstring="The work's authors, by ORCID",
        documentation_link="https://docs.openalex.org/api-entities/authors/author-object#orcid",
    ),
    TermField(
        param="authorships.countries",
        docstring=DOCSTRINGS["country"],
        documentation_link=DOCUMENTATION_LINKS["country"],
        alternate_names=ALTERNATE_NAMES.get("country", None),
    ),
    TermField(
        param="authorships.institutions.country_code",
        docstring=DOCSTRINGS["country"],
        documentation_link=DOCUMENTATION_LINKS["country"],
        alternate_names=ALTERNATE_NAMES.get("country", None),
    ),
    TermField(
        param=f"authorships.institutions.continent",
        custom_es_field="authorships.institutions.country_code",
        docstring=DOCSTRINGS["continent"],
        documentation_link=DOCUMENTATION_LINKS["continent"],
        alternate_names=ALTERNATE_NAMES.get("continent", None),
    ),
    TermField(
        param="authorships.institutions.ror",
        docstring="The work's authors' institutional affiliations, using ROR ID",
        documentation_link="https://docs.openalex.org/api-entities/institutions/institution-object#ror",
    ),
    TermField(
        param="authorships.institutions.type",
        docstring='The type of institutions affiliated with the work. For example, universities are type "Education," and hospitals are type "Healthcare".',
        documentation_link="https://docs.openalex.org/api-entities/institutions/institution-object#type",
    ),
    TermField(
        param="best_oa_location.landing_page_url",
        custom_es_field="best_oa_location.landing_page_url",
    ),
    TermField(
        param="best_oa_location.source.issn",
    ),
    TermField(
        param="best_oa_location.license",
        docstring=DOCSTRINGS["license"],
        documentation_link=DOCUMENTATION_LINKS["license"],
        alternate_names=ALTERNATE_NAMES.get("license", None),
    ),
    TermField(param="best_oa_location.source.type"),
    TermField(
        param="best_oa_location.version",
        docstring="The version of the work that is available Open Access",
        documentation_link="https://docs.openalex.org/api-entities/works/work-object/location-object#version",
    ),
    TermField(param="best_open_version", custom_es_field="locations.version"),
    TermField(param="concepts.wikidata"),
    TermField(param="display_name", custom_es_field="display_name.lower"),
    TermField(
        param="doi",
        alias="ids.doi",
        docstring="The DOI (Digital Object Identifier) for a work",
        documentation_link="https://docs.openalex.org/api-entities/works/work-object#doi",
    ),
    TermField(param="doi_starts_with", custom_es_field="ids.doi"),
    TermField(param="fulltext_origin"),
    TermField(param="ids.mag", custom_es_field="ids.mag"),
    TermField(param="ids.pmid", custom_es_field="ids.pmid"),
    TermField(param="ids.pmcid", custom_es_field="ids.pmcid"),
    TermField(
        param="indexed_in",
    ),
    TermField(
        param="institutions.country_code",
        alias="authorships.institutions.country_code",
        docstring=DOCSTRINGS["country"],
        documentation_link=DOCUMENTATION_LINKS["country"],
        alternate_names=ALTERNATE_NAMES.get("country", None),
    ),
    TermField(
        param="institutions.continent",
        alias="authorships.institutions.country_code",
        docstring=DOCSTRINGS["continent"],
        documentation_link=DOCUMENTATION_LINKS["continent"],
        alternate_names=ALTERNATE_NAMES.get("continent", None),
    ),
    TermField(param="institutions.ror", alias="authorships.institutions.ror"),
    TermField(param="institutions.type", alias="authorships.institutions.type"),
    TermField(param="keywords.keyword", custom_es_field="keywords.keyword.lower"),
    TermField(
        param="grants.award_id",
        docstring="The award IDs listed in the work's grants",
        documentation_link="https://docs.openalex.org/api-entities/works/work-object#grants",
    ),
    TermField(
        param="language",
        docstring=DOCSTRINGS["language"],
        documentation_link=DOCUMENTATION_LINKS["language"],
        alternate_names=ALTERNATE_NAMES.get("language", None),
    ),
    TermField(
        param="locations.landing_page_url", custom_es_field="locations.landing_page_url"
    ),
    TermField(param="locations.source.issn"),
    TermField(
        param="locations.license",
        docstring=DOCSTRINGS["license"],
        documentation_link=DOCUMENTATION_LINKS["license"],
        alternate_names=ALTERNATE_NAMES.get("license", None),
    ),
    TermField(param="locations.source.type"),
    TermField(param="locations.version"),
    TermField(param="mag", custom_es_field="ids.mag"),
    TermField(param="oa_status", alias="open_access.oa_status"),
    TermField(
        param="open_access.oa_status",
        docstring="""The work's Open Access (OA) status, such as "gold," "green," or "hybrid".""",
        documentation_link="https://docs.openalex.org/api-entities/works/work-object#oa_status",
    ),
    TermField(param="pmid", custom_es_field="ids.pmid"),
    TermField(param="pmcid", custom_es_field="ids.pmcid"),
    TermField(
        param="primary_location.landing_page_url",
        custom_es_field="primary_location.landing_page_url",
    ),
    TermField(
        param="primary_location.license",
        docstring=DOCSTRINGS["license"],
        documentation_link=DOCUMENTATION_LINKS["license"],
        alternate_names=ALTERNATE_NAMES.get("license", None),
    ),
    TermField(
        param="primary_location.source.issn",
        docstring="The work's journal, by ISSN",
        documentation_link="https://docs.openalex.org/api-entities/sources/source-object#issn_l",
    ),
    TermField(
        param="primary_location.source.type",
        docstring=DOCSTRINGS["source.type"],
        documentation_link=DOCUMENTATION_LINKS["source.type"],
        alternate_names=ALTERNATE_NAMES.get("source.type", None),
    ),
    TermField(param="primary_location.version"),
    TermField(
        param="sustainable_development_goals.id",
        docstring=DOCSTRINGS["sustainable_development_goals"],
        documentation_link=DOCUMENTATION_LINKS["sustainable_development_goals"],
        alternate_names=ALTERNATE_NAMES.get("sustainable_development_goals"),
    ),
    TermField(
        param="type",
        docstring=DOCSTRINGS["type"],
        documentation_link=DOCUMENTATION_LINKS["type"],
        alternate_names=ALTERNATE_NAMES.get("work.type", None),
    ),
    TermField(param="type_crossref"),
    TermField(param="version", custom_es_field="locations.version"),
]

fields_dict = {f.param: f for f in fields}
