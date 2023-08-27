import random

from elasticsearch_dsl import Q, Search
from flask import Blueprint, abort, redirect, request, url_for

from authors.schemas import AuthorsSchema
from concepts.schemas import ConceptsSchema
from funders.schemas import FundersSchema
from ids.utils import (get_merged_id, is_author_openalex_id,
                       is_concept_openalex_id, is_funder_openalex_id,
                       is_institution_openalex_id, is_openalex_id,
                       is_publisher_openalex_id, is_source_openalex_id,
                       is_venue_openalex_id, is_work_openalex_id,
                       normalize_doi, normalize_issn, normalize_openalex_id,
                       normalize_orcid, normalize_pmid, normalize_ror,
                       normalize_wikidata, process_id_only_fields)
from institutions.schemas import InstitutionsSchema
from publishers.schemas import PublishersSchema
from settings import (AUTHORS_INDEX, AUTHORS_INDEX_OLD, CONCEPTS_INDEX,
                      FUNDERS_INDEX, INSTITUTIONS_INDEX, PUBLISHERS_INDEX,
                      SOURCES_INDEX, WORKS_INDEX)
from sources.schemas import SourcesSchema
from works.schemas import WorksSchema

blueprint = Blueprint("ids", __name__)


# works


@blueprint.route("/works/RANDOM")
@blueprint.route("/works/random")
def works_random_get():
    s = Search(index=WORKS_INDEX)
    only_fields = process_id_only_fields(request, WorksSchema)

    # divide queries into year groups to limit how much work the random function_score has to do
    year_groups = [
        Q("range", publication_year={"lt": 1965}),
        Q("range", publication_year={"gte": 1965, "lte": 1985}),
        Q("range", publication_year={"gte": 1986, "lte": 1990}),
        Q("range", publication_year={"gte": 1991, "lte": 1995}),
        Q("range", publication_year={"gte": 1996, "lte": 2000}),
        Q("range", publication_year={"gte": 2001, "lte": 2004}),
        Q("range", publication_year={"gte": 2005, "lte": 2006}),
        Q("range", publication_year={"gte": 2007, "lte": 2010}),
        Q("range", publication_year={"gte": 2011, "lte": 2014}),
        Q("range", publication_year={"gte": 2015, "lte": 2018}),
        Q("range", publication_year={"gte": 2019, "lte": 2020}),
        Q("range", publication_year={"gt": 2020}),
    ]
    random_query = Q(
        "function_score",
        functions={"random_score": {}},
        query=random.choice(year_groups),
    )
    s = s.query(random_query).extra(size=1)
    response = s.execute()
    works_schema = WorksSchema(context={"display_relevance": False}, only=only_fields)
    return works_schema.dump(response[0])


@blueprint.route("/works/<path:id>")
def works_id_get(id):
    s = Search(index=WORKS_INDEX)
    only_fields = process_id_only_fields(request, WorksSchema)

    if is_openalex_id(id):
        clean_id = normalize_openalex_id(id)
        if clean_id != id:
            return redirect(url_for("ids.works_id_get", id=clean_id, **request.args))
        clean_id = int(clean_id[1:])
        full_openalex_id = f"https://openalex.org/W{clean_id}"
        query = Q("term", ids__openalex=full_openalex_id)
        s = s.filter(query)
        if s.count() == 0:
            # check if document is merged
            merged_id = get_merged_id("merge-works", full_openalex_id)
            if merged_id:
                return redirect(
                    url_for("ids.works_id_get", id=merged_id, **request.args), code=301
                )
    elif id.startswith("mag:"):
        clean_id = id.replace("mag:", "")
        clean_id = f"W{clean_id}"
        return redirect(url_for("ids.works_id_get", id=clean_id, **request.args))
    elif id.startswith("pmid:"):
        id = id.replace("pmid:", "")
        clean_pmid = normalize_pmid(id)
        full_pmid = f"https://pubmed.ncbi.nlm.nih.gov/{clean_pmid}"
        query = Q("term", ids__pmid=full_pmid)
        s = s.filter(query)
    elif id.startswith("doi:") or ("doi" in id):
        clean_doi = normalize_doi(id, return_none_if_error=True)
        if not clean_doi:
            abort(404)
        full_doi = f"https://doi.org/{clean_doi}"
        query = Q("term", ids__doi=full_doi)
        s = s.filter(query)
    else:
        abort(404)
    response = s.execute()
    if not response:
        abort(404)
    works_schema = WorksSchema(
        context={"display_relevance": False, "single_record": True}, only=only_fields
    )
    return works_schema.dump(response[0])


# Author


@blueprint.route("/authors/RANDOM")
@blueprint.route("/authors/random")
@blueprint.route("/people/random")
def authors_random_get():
    s = Search(index=AUTHORS_INDEX)
    only_fields = process_id_only_fields(request, AuthorsSchema)

    # divide queries into year groups to limit how much work the random function_score has to do
    cited_by_groups = [
        Q("term", cited_by_count=0),
        Q("range", cited_by_count={"gt": 1}),
    ]
    random_query = Q(
        "function_score",
        functions={"random_score": {}},
        query=random.choice(cited_by_groups),
    )
    s = s.query(random_query).extra(size=1)
    response = s.execute()
    authors_schema = AuthorsSchema(
        context={"display_relevance": False}, only=only_fields
    )
    return authors_schema.dump(response[0])


@blueprint.route("/authors/<path:id>")
@blueprint.route("/people/<path:id>")
def authors_id_get(id):
    s = Search(index=AUTHORS_INDEX)
    only_fields = process_id_only_fields(request, AuthorsSchema)

    if is_openalex_id(id):
        clean_id = normalize_openalex_id(id)
        if clean_id != id:
            return redirect(url_for("ids.authors_id_get", id=clean_id, **request.args))
        author_id = int(clean_id[1:])
        if author_id < 5000000000:
            s = Search(index=AUTHORS_INDEX_OLD)
        full_author_id = f"https://openalex.org/A{author_id}"
        query = Q("term", ids__openalex=full_author_id)
        s = s.filter(query)
        if s.count() == 0:
            # check if document is merged
            merged_id = get_merged_id("merge-authors", full_author_id)
            if merged_id:
                return redirect(
                    url_for("ids.authors_id_get", id=merged_id, **request.args),
                    code=301,
                )
    elif id.startswith("mag:"):
        clean_id = id.replace("mag:", "")
        clean_id = f"A{clean_id}"
        return redirect(url_for("ids.authors_id_get", id=clean_id, **request.args))
    elif id.startswith("orcid:") or id.startswith("https://orcid.org"):
        clean_orcid = normalize_orcid(id)
        if not clean_orcid:
            return abort(404)
        full_orcid = f"https://orcid.org/{clean_orcid}"
        query = Q("term", ids__orcid=full_orcid)
        s = s.filter(query)
    else:
        abort(404)
    response = s.execute()
    if not response:
        abort(404)
    authors_schema = AuthorsSchema(
        context={"display_relevance": False}, only=only_fields
    )
    return authors_schema.dump(response[0])


# Institution


@blueprint.route("/institutions/RANDOM")
@blueprint.route("/institutions/random")
def institutions_random_get():
    s = Search(index=INSTITUTIONS_INDEX)
    only_fields = process_id_only_fields(request, InstitutionsSchema)

    random_query = Q("function_score", functions={"random_score": {}})
    s = s.query(random_query).extra(size=1)
    response = s.execute()
    institutions_schema = InstitutionsSchema(
        context={"display_relevance": False}, only=only_fields
    )
    return institutions_schema.dump(response[0])


@blueprint.route("/institutions/<path:id>")
def institutions_id_get(id):
    s = Search(index=INSTITUTIONS_INDEX)
    only_fields = process_id_only_fields(request, InstitutionsSchema)

    if is_openalex_id(id):
        clean_id = normalize_openalex_id(id)
        if clean_id != id:
            return redirect(
                url_for("ids.institutions_id_get", id=clean_id, **request.args)
            )
        clean_id = int(clean_id[1:])
        full_openalex_id = f"https://openalex.org/I{clean_id}"
        query = Q("term", ids__openalex=full_openalex_id)
        s = s.filter(query)
        if s.count() == 0:
            # check if document is merged
            merged_id = get_merged_id("merge-institutions", full_openalex_id)
            if merged_id:
                return redirect(
                    url_for("ids.institutions_id_get", id=merged_id, **request.args),
                    code=301,
                )
    elif id.startswith("mag:"):
        clean_id = id.replace("mag:", "")
        clean_id = f"I{clean_id}"
        return redirect(url_for("ids.institutions_id_get", id=clean_id, **request.args))
    elif id.startswith("ror:") or ("ror.org" in id):
        clean_ror = normalize_ror(id)
        if not clean_ror:
            abort(404)
        full_ror = f"https://ror.org/{clean_ror}"
        query = Q("term", ror=full_ror)
        s = s.filter(query)
    elif id.startswith("wikidata:") or ("wikidata" in id):
        clean_wikidata = normalize_wikidata(id)
        if not clean_wikidata:
            abort(404)
        full_wikidata = f"https://www.wikidata.org/wiki/{clean_wikidata}"
        query = Q("term", ids__wikidata=full_wikidata)
        s = s.filter(query)
    else:
        abort(404)
    response = s.execute()
    if not response:
        abort(404)
    institutions_schema = InstitutionsSchema(
        context={"display_relevance": False}, only=only_fields
    )
    return institutions_schema.dump(response[0])


# Venue (delete after one month)


@blueprint.route("/venues/RANDOM")
@blueprint.route("/venues/random")
def venues_random_get():
    return redirect(url_for("ids.sources_random_get", **request.args), code=301)


@blueprint.route("/venues/<path:id>")
def venues_id_get(id):
    if is_openalex_id(id):
        clean_id = normalize_openalex_id(id)
        if clean_id != id:
            return redirect(url_for("ids.venues_id_get", id=clean_id, **request.args))
        clean_id = int(clean_id[1:])
        full_openalex_id = f"https://openalex.org/S{clean_id}"
        return redirect(
            url_for("ids.sources_id_get", id=full_openalex_id, **request.args), code=301
        )
    else:
        return redirect(url_for("ids.sources_id_get", id=id, **request.args), code=301)


# Concept


@blueprint.route("/concepts/RANDOM")
@blueprint.route("/concepts/random")
def concepts_random_get():
    s = Search(index=CONCEPTS_INDEX)
    only_fields = process_id_only_fields(request, ConceptsSchema)

    random_query = Q("function_score", functions={"random_score": {}})
    s = s.query(random_query).extra(size=1)
    response = s.execute()
    concepts_schema = ConceptsSchema(
        context={"display_relevance": False}, only=only_fields
    )
    return concepts_schema.dump(response[0])


@blueprint.route("/concepts/<path:id>")
def concepts_id_get(id):
    s = Search(index=CONCEPTS_INDEX)
    only_fields = process_id_only_fields(request, ConceptsSchema)

    if is_openalex_id(id):
        clean_id = normalize_openalex_id(id)
        if clean_id != id:
            return redirect(url_for("ids.concepts_id_get", id=clean_id, **request.args))
        clean_id = int(clean_id[1:])
        full_openalex_id = f"https://openalex.org/C{clean_id}"
        query = Q("term", ids__openalex=full_openalex_id)
        s = s.filter(query)
        if s.count() == 0:
            # check if document is merged
            merged_id = get_merged_id("merge-concepts", full_openalex_id)
            if merged_id:
                return redirect(
                    url_for("ids.concepts_id_get", id=merged_id, **request.args),
                    code=301,
                )
    elif id.startswith("mag:"):
        clean_id = id.replace("mag:", "")
        clean_id = f"C{clean_id}"
        return redirect(url_for("ids.concepts_id_get", id=clean_id, **request.args))
    elif id.startswith("wikidata:") or ("wikidata" in id):
        clean_wikidata = normalize_wikidata(id)
        if not clean_wikidata:
            abort(404)
        full_wikidata = f"https://www.wikidata.org/wiki/{clean_wikidata}"
        query = Q("term", wikidata=full_wikidata)
        s = s.filter(query)
    else:
        abort(404)
    response = s.execute()
    if not response:
        abort(404)
    concepts_schema = ConceptsSchema(
        context={"display_relevance": False}, only=only_fields
    )
    return concepts_schema.dump(response[0])


@blueprint.route("/concepts/name/<string:name>")
def concepts_name_get(name):
    s = Search(index=CONCEPTS_INDEX)

    query = Q("match_phrase_prefix", display_name=name)
    s = s.query(query)
    response = s.execute()
    if not response:
        abort(404)
    concepts_schema = ConceptsSchema(context={"display_relevance": False})
    return concepts_schema.dump(response[0])


# Funder


@blueprint.route("/funders/RANDOM")
@blueprint.route("/funders/random")
def funders_random_get():
    s = Search(index=FUNDERS_INDEX)
    only_fields = process_id_only_fields(request, FundersSchema)

    random_query = Q("function_score", functions={"random_score": {}})
    s = s.query(random_query).extra(size=1)
    response = s.execute()
    funders_schema = FundersSchema(
        context={"display_relevance": False}, only=only_fields
    )
    return funders_schema.dump(response[0])


@blueprint.route("/funders/<path:id>")
def funders_id_get(id):
    s = Search(index=FUNDERS_INDEX)
    only_fields = process_id_only_fields(request, FundersSchema)

    if is_openalex_id(id):
        clean_id = normalize_openalex_id(id)
        if clean_id != id:
            return redirect(url_for("ids.funders_id_get", id=clean_id, **request.args))
        clean_id = int(clean_id[1:])
        full_openalex_id = f"https://openalex.org/F{clean_id}"
        query = Q("term", ids__openalex=full_openalex_id)
        s = s.filter(query)
        if s.count() == 0:
            # check if document is merged
            merged_id = get_merged_id("merge-funders", full_openalex_id)
            if merged_id:
                return redirect(
                    url_for("ids.funders_id_get", id=merged_id, **request.args),
                    code=301,
                )
    elif id.startswith("ror:") or ("ror.org" in id):
        clean_ror = normalize_ror(id)
        if not clean_ror:
            abort(404)
        full_ror = f"https://ror.org/{clean_ror}"
        query = Q("term", ids__ror=full_ror)
        s = s.filter(query)

    elif id.startswith("wikidata:") or ("wikidata" in id):
        clean_wikidata = normalize_wikidata(id)
        if not clean_wikidata:
            abort(404)
        full_wikidata = f"https://www.wikidata.org/entity/{clean_wikidata}"
        query = Q("term", ids__wikidata=full_wikidata)
        s = s.filter(query)
    else:
        abort(404)
    response = s.execute()
    if not response:
        abort(404)
    funders_schema = FundersSchema(
        context={"display_relevance": False}, only=only_fields
    )
    return funders_schema.dump(response[0])


# Publisher


@blueprint.route("/publishers/<path:id>")
def publishers_id_get(id):
    s = Search(index=PUBLISHERS_INDEX)
    only_fields = process_id_only_fields(request, PublishersSchema)

    if is_openalex_id(id):
        clean_id = normalize_openalex_id(id)
        if clean_id != id:
            return redirect(
                url_for("ids.publishers_id_get", id=clean_id, **request.args)
            )
        clean_id = int(clean_id[1:])
        full_openalex_id = f"https://openalex.org/P{clean_id}"
        query = Q("term", ids__openalex=full_openalex_id)
        s = s.filter(query)
        if s.count() == 0:
            # check if document is merged
            merged_id = get_merged_id("merge-publishers", full_openalex_id)
            if merged_id:
                return redirect(
                    url_for("ids.publishers_id_get", id=merged_id, **request.args),
                    code=301,
                )
    elif id.startswith("ror:") or ("ror.org" in id):
        clean_ror = normalize_ror(id)
        if not clean_ror:
            abort(404)
        full_ror = f"https://ror.org/{clean_ror}"
        query = Q("term", ids__ror=full_ror)
        s = s.filter(query)
    else:
        abort(404)
    response = s.execute()
    if not response:
        abort(404)
    publishers_schema = PublishersSchema(
        context={"display_relevance": False}, only=only_fields
    )
    return publishers_schema.dump(response[0])


@blueprint.route("/publishers/RANDOM")
@blueprint.route("/publishers/random")
def publishers_random_get():
    s = Search(index=PUBLISHERS_INDEX)
    only_fields = process_id_only_fields(request, PublishersSchema)

    random_query = Q("function_score", functions={"random_score": {}})
    s = s.query(random_query).extra(size=1)
    response = s.execute()
    publishers_schema = PublishersSchema(
        context={"display_relevance": False}, only=only_fields
    )
    return publishers_schema.dump(response[0])


# Source


@blueprint.route("/sources/RANDOM")
@blueprint.route("/sources/random")
@blueprint.route("/journals/random")
def sources_random_get():
    s = Search(index=SOURCES_INDEX)
    only_fields = process_id_only_fields(request, SourcesSchema)

    random_query = Q("function_score", functions={"random_score": {}})
    s = s.query(random_query).extra(size=1)
    response = s.execute()
    sources_schema = SourcesSchema(
        context={"display_relevance": False}, only=only_fields
    )
    return sources_schema.dump(response[0])


@blueprint.route("/sources/<path:id>")
@blueprint.route("/journals/<path:id>", endpoint="journals_id_get")
def sources_id_get(id):
    s = Search(index=SOURCES_INDEX)
    only_fields = process_id_only_fields(request, SourcesSchema)

    if is_openalex_id(id):
        clean_id = normalize_openalex_id(id)
        if clean_id != id:
            return redirect(url_for("ids.sources_id_get", id=clean_id, **request.args))
        clean_id = int(clean_id[1:])
        full_openalex_id = f"https://openalex.org/S{clean_id}"
        query = Q("term", ids__openalex=full_openalex_id)
        s = s.filter(query)
        if s.count() == 0:
            # check if document is merged
            merged_id = get_merged_id("merge-sources", full_openalex_id)
            if merged_id:
                return redirect(
                    url_for("ids.sources_id_get", id=merged_id, **request.args),
                    code=301,
                )

    elif id.startswith("mag:"):
        clean_id = id.replace("mag:", "")
        clean_id = f"S{clean_id}"
        return redirect(url_for("ids.sources_id_get", id=clean_id, **request.args))
    elif id.startswith("issn:"):
        clean_issn = normalize_issn(id)
        if not clean_issn:
            abort(404)
        query = Q("term", ids__issn__lower=clean_issn)
        s = s.filter(query)
        response = s.execute()
        if response:
            record_id = response[0].id
            clean_id = normalize_openalex_id(record_id)
            return redirect(url_for("ids.sources_id_get", id=clean_id, **request.args))
        else:
            abort(404)
    elif id.startswith("issn_l:"):
        clean_issn = normalize_issn(id)
        if not clean_issn:
            abort(404)
        query = Q("term", ids__issn_l__lower=clean_issn)
        s = s.filter(query)
        response = s.execute()
        if response:
            record_id = response[0].id
            clean_id = normalize_openalex_id(record_id)
            return redirect(url_for("ids.sources_id_get", id=clean_id, **request.args))
        else:
            abort(404)
    else:
        abort(404)
    response = s.execute()
    if not response:
        abort(404)
    sources_schema = SourcesSchema(
        context={"display_relevance": False}, only=only_fields
    )
    return sources_schema.dump(response[0])


# Universal


@blueprint.route("/<path:openalex_id>")
def universal_get(openalex_id):
    if not openalex_id:
        return {"message": "Don't panic"}, 404

    if not is_openalex_id(openalex_id):
        return {"message": "OpenAlex ID format not recognized"}, 404

    openalex_id = normalize_openalex_id(openalex_id)
    if is_work_openalex_id(openalex_id):
        return redirect(url_for("ids.works_id_get", id=openalex_id, **request.args))
    elif is_author_openalex_id(openalex_id):
        return redirect(url_for("ids.authors_id_get", id=openalex_id, **request.args))
    elif is_venue_openalex_id(openalex_id):
        return redirect(url_for("ids.venues_id_get", id=openalex_id, **request.args))
    elif is_institution_openalex_id(openalex_id):
        return redirect(
            url_for("ids.institutions_id_get", id=openalex_id, **request.args)
        )
    elif is_concept_openalex_id(openalex_id):
        return redirect(url_for("ids.concepts_id_get", id=openalex_id, **request.args))
    elif is_funder_openalex_id(openalex_id):
        return redirect(url_for("ids.funders_id_get", id=openalex_id, **request.args))
    elif is_publisher_openalex_id(openalex_id):
        return redirect(
            url_for("ids.publishers_id_get", id=openalex_id, **request.args)
        )
    elif is_source_openalex_id(openalex_id):
        return redirect(url_for("ids.sources_id_get", id=openalex_id, **request.args))
    return {"message": "OpenAlex ID format not recognized"}, 404
