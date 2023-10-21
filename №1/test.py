import pytest
from data import courses, mentors, durations
from main import unique_names, max_course_durations, popular_name


class TestPytest:
    @pytest.mark.parametrize(
        "mentors, expected", [
            (
                mentors,
                33
            )
        ]
    )
    def test_unique_names(self, mentors, expected):
        result = unique_names(mentors)

        assert result == expected

    @pytest.mark.parametrize(
        "courses, mentors, durations, expected", [
            (
                courses,
                mentors,
                durations,
                '20'
            )
        ]
    )
    def test_max_course_durations(self, courses, mentors, durations, expected):
        res = max_course_durations(courses, mentors, durations)

        assert expected in res

    @pytest.mark.parametrize(
        "mentors, expected", [
            (
                mentors,
                10
            )
        ]
    )
    def test_popular_name(self, mentors, expected):
        res = popular_name(mentors)

        assert res == expected