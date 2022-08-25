import logging
from typing import Tuple

import leetcode
from leetcode import GraphqlData

from leetcode_client import get_leetcode_api_client


def checkListExists(list_id: str) -> bool:
    api = get_leetcode_api_client()

    auth_settings = [
        "cookieCSRF",
        "cookieSession",
        "headerCSRF",
        "referer",
    ]
    auth_settings = auth_settings

    api.api_client.call_api(
        "/api/progress/favorite/{}/".format(list_id),
        "GET",
        auth_settings=auth_settings
    )


def add_question_to_list(list_id, question_id) -> Tuple[bool, str]:
    """

    :param list_id:
    :param question_id:
    :return:  [successful:boolean, error:str]
    """
    api = get_leetcode_api_client()

    graphql_request = leetcode.GraphqlQuery(
        query="""
            mutation addQuestionToFavorite($favoriteIdHash: String!, $questionId: String!) {
              addQuestionToFavorite(favoriteIdHash: $favoriteIdHash, questionId: $questionId) {
                ok
                error
              }
            }
        """,
        variables={"favoriteIdHash": list_id, "questionId": question_id},
        operation_name="addQuestionToFavorite"
    )

    auth_settings = [
        "cookieCSRF",
        "cookieSession",
        "headerCSRF",
        "referer",
    ]

    response = api.api_client.call_api(
        "/graphql",
        "POST",
        auth_settings=auth_settings,
        body=graphql_request,
        response_type=object
    )

    body = response[0]

    bizResult = body["data"]["addQuestionToFavorite"]
    successful = bizResult["ok"]
    error = bizResult["error"]
    if error == "No such list exist!":
        error = error + " - does this list belong to you? "
    return successful, error
