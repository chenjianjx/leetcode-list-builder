import leetcode.api.default_api  # type: ignore
import leetcode.api_client  # type: ignore
import leetcode.auth  # type: ignore
import leetcode.configuration  # type: ignore
import os


_api_instance: leetcode.api.default_api.DefaultApi = None
def get_leetcode_api_client() -> leetcode.api.default_api.DefaultApi:
    global _api_instance
    if not _api_instance:
        """
        Copied from https://github.com/prius/leetcode-anki/blob/master/leetcode_anki/helpers/leetcode.py
    
    
        Leetcode API instance constructor.
        This is a singleton, because we don't need to create a separate client each time
        """

        configuration = leetcode.configuration.Configuration()

        session_id = os.environ["LEETCODE_SESSION_ID"]
        csrf_token = leetcode.auth.get_csrf_cookie(session_id)

        configuration.api_key["x-csrftoken"] = csrf_token
        configuration.api_key["csrftoken"] = csrf_token
        configuration.api_key["LEETCODE_SESSION"] = session_id
        configuration.api_key["Referer"] = "https://leetcode.com"
        configuration.debug = False
        _api_instance = leetcode.api.default_api.DefaultApi(
            leetcode.api_client.ApiClient(configuration)
        )

    return _api_instance