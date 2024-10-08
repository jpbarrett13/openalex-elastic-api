import pytest


class TestGroupBySearchBasics:
    def test_group_by_search_q_field(self, client):
        """Test that the q param is displayed in the meta section of the response."""
        res = client.get("/works?group-by=concept.id&q=comp")
        json_data = res.get_json()
        assert json_data["meta"]["q"] == "comp"

    def test_group_by_search_empty_q(self, client):
        """Test that an empty q param shows regular group-by results."""
        res = client.get("/works?group-by=concept.id&q=")
        json_data = res.get_json()
        first_result = json_data["group_by"][0]
        assert json_data["meta"]["q"] == ""
        assert first_result == {
            "key": "https://openalex.org/C41008148",
            "key_display_name": "Computer science",
            "count": 3176,
        }


class TestAuthorsGroupBySearch:
    def test_group_by_search_last_known_institution_country_code(self, client):
        res = client.get("/authors?group-by=last_known_institution.country_code&q=uni")
        json_data = res.get_json()
        first_result = json_data["group_by"][0]
        second_result = json_data["group_by"][1]
        assert len(json_data["group_by"]) == 3
        assert first_result == {
            "key": "US",
            "key_display_name": "United States of America",
            "count": 1048,
        }
        assert second_result == {
            "key": "GB",
            "key_display_name": "United Kingdom of Great Britain and Northern Ireland",
            "count": 184,
        }

    def test_group_by_search_last_known_institution_continent(self, client):
        res = client.get("/authors?group-by=last_known_institution.continent&q=afr")
        json_data = res.get_json()
        first_result = json_data["group_by"][0]
        assert len(json_data["group_by"]) == 1
        assert first_result == {
            "key": "Q15",
            "key_display_name": "Africa",
            "count": 104,
        }

    def test_group_by_search_last_known_institution_id(self, client):
        res = client.get("/authors?group-by=last_known_institution.id&q=tr")
        json_data = res.get_json()
        first_result = json_data["group_by"][0]
        second_result = json_data["group_by"][1]
        assert len(json_data["group_by"]) == 4
        assert first_result == {
            "key": "https://openalex.org/I70931966",
            "key_display_name": "University of Montreal",
            "count": 8,
        }
        assert second_result == {
            "key": "https://openalex.org/I107639228",
            "key_display_name": "University of Notre Dame",
            "count": 5,
        }

    def test_group_by_search_last_known_institution_type(self, client):
        res = client.get("/authors?group-by=last_known_institution.type&q=edu")
        json_data = res.get_json()
        first_result = json_data["group_by"][0]
        assert len(json_data["group_by"]) == 1
        assert first_result == {
            "key": "education",
            "key_display_name": "education",
            "count": 3261,
        }


class TestConceptsGroupBySearch:
    def test_concepts_group_by_search_ancestors_id(self, client):
        res = client.get("/concepts?group-by=ancestors.id&q=comp")
        json_data = res.get_json()
        first_result = json_data["group_by"][0]
        assert len(json_data["group_by"]) == 6
        assert first_result == {
            "key": "https://openalex.org/C41008148",
            "key_display_name": "Computer science",
            "count": 2240,
        }


class TestInstitutionsGroupBySearch:
    def test_institutions_group_by_search_continent(self, client):
        res = client.get("/institutions?group-by=continent&q=North Am")
        json_data = res.get_json()
        first_result = json_data["group_by"][0]
        assert len(json_data["group_by"]) == 1
        assert first_result == {
            "key": "Q49",
            "key_display_name": "North America",
            "count": 3164,
        }

    def test_institutions_group_by_search_country_code(self, client):
        res = client.get("/institutions?group-by=country_code&q=uni")
        json_data = res.get_json()
        first_result = json_data["group_by"][0]
        second_result = json_data["group_by"][1]
        assert len(json_data["group_by"]) == 3
        assert first_result == {
            "key": "US",
            "key_display_name": "United States of America",
            "count": 2786,
        }
        assert second_result == {
            "key": "GB",
            "key_display_name": "United Kingdom of Great Britain and Northern Ireland",
            "count": 528,
        }

    def test_institutions_group_by_search_type(self, client):
        res = client.get("/institutions?group-by=type&q=edu")
        json_data = res.get_json()
        first_result = json_data["group_by"][0]
        assert len(json_data["group_by"]) == 1
        assert first_result == {
            "key": "education",
            "key_display_name": "education",
            "count": 5312,
        }


class TestSourcesGroupBySearch:
    def test_sources_group_by_search_publisher(self, client):
        res = client.get("/sources?group-by=publisher&q=els")
        json_data = res.get_json()
        first_result = json_data["group_by"][0]
        assert len(json_data["group_by"]) == 2
        assert first_result == {
            "key": "Elsevier BV",
            "key_display_name": "Elsevier BV",
            "count": 1071,
        }

    def test_sources_group_by_search_type(self, client):
        res = client.get("/sources?group-by=type&q=journ")
        json_data = res.get_json()
        first_result = json_data["group_by"][0]
        assert len(json_data["group_by"]) == 1
        assert first_result == {
            "key": "journal",
            "key_display_name": "journal",
            "count": 8548,
        }


class TestWorksGroupBySearch:
    @pytest.mark.skip(
        reason="This test is failing because we need to reindex alternate_host_venues.display_name as fulltext."
    )
    def test_works_group_by_search_alternate_host_venues_id(self, client):
        res = client.get("/works?group-by=alternate_host_venues.id&q=urol")
        json_data = res.get_json()
        first_result = json_data["group_by"][0]
        assert len(json_data["group_by"]) == 1
        assert first_result == {
            "key": "https://openalex.org/V30525748",
            "key_display_name": "The Journal of Urology",
            "count": 2,
        }

    def test_works_group_by_search_alternate_host_venues_license(self, client):
        res = client.get("/works?group-by=alternate_host_venues.license&q=cc-b")
        json_data = res.get_json()
        first_result = json_data["group_by"][0]
        assert len(json_data["group_by"]) == 6
        assert first_result == {
            "key": "cc-by",
            "key_display_name": "cc-by",
            "count": 288,
        }

    def test_works_group_by_search_alternate_host_venues_version(self, client):
        res = client.get("/works?group-by=alternate_host_venues.version&q=puBl")
        json_data = res.get_json()
        first_result = json_data["group_by"][0]
        assert len(json_data["group_by"]) == 1
        assert first_result == {
            "key": "publishedVersion",
            "key_display_name": "publishedVersion",
            "count": 893,
        }

    @pytest.mark.skip("no longer working")
    def test_works_group_by_search_author_id(self, client):
        res = client.get("/works?group-by=author.id&q=a")
        json_data = res.get_json()
        first_result = json_data["group_by"][0]
        assert len(json_data["group_by"]) == 1
        assert first_result == {
            "key": "https://openalex.org/A1382709",
            "key_display_name": "Alejandro López-Ortiz",
            "count": 1,
        }

    def test_works_group_by_search_concept_id(self, client):
        res = client.get("/works?group-by=concept.id&q=comp")
        json_data = res.get_json()
        first_result = json_data["group_by"][0]
        second_result = json_data["group_by"][1]
        assert len(json_data["group_by"]) == 6
        assert first_result == {
            "key": "https://openalex.org/C41008148",
            "key_display_name": "Computer science",
            "count": 3176,
        }
        assert second_result == {
            "key": "https://openalex.org/C38652104",
            "key_display_name": "Computer security",
            "count": 153,
        }

    @pytest.mark.skip("no longer working")
    def test_works_group_by_search_host_venue_id(self, client):
        res = client.get("/works?group-by=host_venue.id&q=urol")
        json_data = res.get_json()
        first_result = json_data["group_by"][0]
        assert len(json_data["group_by"]) == 1
        assert first_result == {
            "key": "https://openalex.org/V30525748",
            "key_display_name": "The Journal of Urology",
            "count": 2,
        }

    def test_works_group_by_search_host_venue_license(self, client):
        res = client.get("/works?group-by=host_venue.license&q=cc-b")
        json_data = res.get_json()
        first_result = json_data["group_by"][0]
        second_result = json_data["group_by"][1]
        assert len(json_data["group_by"]) == 6
        assert first_result == {
            "key": "cc-by",
            "key_display_name": "cc-by",
            "count": 261,
        }
        assert second_result == {
            "key": "cc-by-nc-nd",
            "key_display_name": "cc-by-nc-nd",
            "count": 120,
        }

    def test_works_group_by_search_host_venue_version(self, client):
        res = client.get("/works?group-by=host_venue.version&q=puBl")
        json_data = res.get_json()
        first_result = json_data["group_by"][0]
        assert len(json_data["group_by"]) == 1
        assert first_result == {
            "key": "publishedVersion",
            "key_display_name": "publishedVersion",
            "count": 844,
        }

    def test_works_group_by_search_institutions_id(self, client):
        res = client.get("/works?group-by=institutions.id&q=har")
        json_data = res.get_json()
        first_result = json_data["group_by"][0]
        assert len(json_data["group_by"]) == 3
        assert first_result == {
            "key": "https://openalex.org/I136199984",
            "key_display_name": "Harvard University",
            "count": 9,
        }

    def test_works_group_by_search_institutions_continent(self, client):
        res = client.get("/works?group-by=institutions.continent&q=eur")
        json_data = res.get_json()
        first_result = json_data["group_by"][0]
        assert len(json_data["group_by"]) == 1
        assert first_result == {
            "key": "Q46",
            "key_display_name": "Europe",
            "count": 1027,
        }

    def test_works_group_by_search_institutions_country_code(self, client):
        res = client.get("/works?group-by=institutions.country_code&q=uni")
        json_data = res.get_json()
        first_result = json_data["group_by"][0]
        second_result = json_data["group_by"][1]
        assert len(json_data["group_by"]) == 3
        assert first_result == {
            "key": "US",
            "key_display_name": "United States of America",
            "count": 804,
        }
        assert second_result == {
            "key": "GB",
            "key_display_name": "United Kingdom of Great Britain and Northern Ireland",
            "count": 159,
        }

    def test_works_group_by_search_institutions_type(self, client):
        res = client.get("/works?group-by=institutions.type&q=Heal")
        json_data = res.get_json()
        first_result = json_data["group_by"][0]
        assert first_result == {
            "key": "healthcare",
            "key_display_name": "healthcare",
            "count": 328,
        }

    def test_works_group_by_search_open_access_status(self, client):
        res = client.get("/works?group-by=open_access.oa_status&q=gOl")
        json_data = res.get_json()
        first_result = json_data["group_by"][0]
        assert first_result == {
            "key": "gold",
            "key_display_name": "gold",
            "count": 416,
        }

    def test_works_group_by_search_publication_year(self, client):
        res = client.get("/works?group-by=publication_year&q=201")
        json_data = res.get_json()
        assert len(json_data["group_by"]) == 10
        for result in json_data["group_by"]:
            assert result["key"].startswith("201")

    def test_works_group_by_search_version(self, client):
        res = client.get("/works?group-by=version&q=puBl")
        json_data = res.get_json()
        assert len(json_data["group_by"]) == 1
        first_result = json_data["group_by"][0]
        assert first_result == {
            "key": "publishedVersion",
            "key_display_name": "publishedVersion",
            "count": 894,
        }
