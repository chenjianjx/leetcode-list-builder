Input: a list of question urls, the id of the list

Output:
 * On console, successful with N failures
 * On leetcode list, the list has been filled

Acceptance criteria:
 * new questions will be there
 * old questions will still be there
 
-----
Program:
 * Parse and validate parameters
 * Check if the list exists
 * Load the file and make it a list of urls
 * For each url
    * get the id of the question
    * if the questions is not in this list, add the question to the specified list
 * output   
 
