# Test cases


## Positive case - add to a blank list

* Input
  * A blank list
  * All question urls are valid, but there are duplicates, spaces around urls, and empty lines

* Expectations
  * The console outputs how many questions are added
  * The list contains all the questions

## Positive case - add to a non-blank list

* Input
  * An non-blank list which contains question 1,2
  * The question urls are 2,3

* Expectations
  * The console outputs how many questions are added (existing ones are also considered added) 
  * The list contains 1,2,3


## Negative case

* An invalid list id
* The question urls file doesn't exist
* An empty question urls file
* A list id that doesn't belong to current user
* Some question urls don't even belong to leetcode.com
* Some question urls contain invalid title slugs