import leetcode

from leetcode_client import get_leetcode_api_client

__PROBLEM_URL_PREFIX = "https://leetcode.com/problems/"


def url_to_title_slug(url: str):
    """
    :param url:
    :return: None if the url is invalid
    """
    if not url.startswith(__PROBLEM_URL_PREFIX):
        return None
    return url[len(__PROBLEM_URL_PREFIX):].rstrip("/")


def title_slug_to_id(title_slug: str) -> int:
    api = get_leetcode_api_client()
    graphql_request = leetcode.GraphqlQuery(
        query="""
            query getQuestionDetail($titleSlug: String!) {
              question(titleSlug: $titleSlug) {                
                questionId                                   
              }
            }
        """,
        variables=leetcode.GraphqlQueryGetQuestionDetailVariables(title_slug=title_slug),
        operation_name="getQuestionDetail",
    )

    response = api.graphql_post(body=graphql_request)
    question = response.data.question
    return int(question.question_id) if question else None


