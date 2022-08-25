import logging

import leetcode

from leetcode_client import get_leetcode_api_client


def url_to_title_slug(url: str):
    return url[len("https://leetcode.com/problems/"):].rstrip("/")


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


