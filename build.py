#!/usr/bin/env python3
import argparse
import logging
import time

import leetcode.rest

from io_utils import read_file_as_non_empty_stripped_list
from list_service import checkListExists, add_question_to_list
from question_service import url_to_title_slug, title_slug_to_id, __PROBLEM_URL_PREFIX

logging.getLogger().setLevel(logging.INFO)


def parse_args() -> argparse.Namespace:
    """
    Parse command line arguments for the script
    """
    parser = argparse.ArgumentParser(description="Build a leetcode list from a list of questions")

    parser.add_argument(
        "--list-id", type=str, required=True,
        help="Your favorites list id, such as 'e86yjyq8' in https://leetcode.com/list?selectedList=e86yjyq8"
    )

    parser.add_argument(
        "--question-urls-file", type=argparse.FileType('r'), required=True,
        help="The file containing a list of question urls"
    )

    args = parser.parse_args()

    return args


def build(list_id, question_urls_file):
    urls = read_file_as_non_empty_stripped_list(question_urls_file)
    logging.info('{} urls in total'.format(len(urls)))

    title_slug_set =  set()
    for url in urls:
        slug = url_to_title_slug(url)
        if not slug:
            logging.error("{} does not start with {} . Please fix it".format(url, __PROBLEM_URL_PREFIX))
            return
        else:
            title_slug_set.add(slug)

    logging.info('{} title slugs in total'.format(len(title_slug_set)))
    logging.info('The title slugs are {}'.format(title_slug_set))

    try:
        checkListExists(list_id)
    except leetcode.rest.ApiException as ex:
        logging.error("{} is not a valid list id. The response body is {}".format(list_id, ex.body))
        return
    logging.info("The list id is valid")

    print()

    slug_and_id = {}
    for slug in title_slug_set:
        time.sleep(1)
        question_id = title_slug_to_id(slug)
        if question_id:
            logging.info("question_id for {} is {}".format(slug, question_id))
            slug_and_id[slug] = (question_id)
        else:
            logging.error("no question found with title slug: {}. Please fix it".format(slug))
            return
    print()

    num_of_added = 0
    for slug, question_id in slug_and_id.items():
        time.sleep(1)
        add_question_to_list(list_id, question_id)
        ok, error = add_question_to_list(list_id, question_id)
        if ok:
            num_of_added = num_of_added + 1
            logging.info("Added '{}' to the list".format(slug))
        else:
            logging.error("Failed to add '{}' to the list, because: {}".format(slug, error))
    print()

    logging.info("In total, added (or re-added) {} questions to the list".format(num_of_added))

if __name__ == '__main__':
    args = parse_args()
    build(args.list_id, args.question_urls_file)