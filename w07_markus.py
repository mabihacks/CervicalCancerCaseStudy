"""Week 7 Perform - Part 2"""

# file name: w07_markus.py
#
# Complete the following steps:
#  (1) Complete the following function according to its docstring.
#  (2) Save your file after you make changes, and then run the file by
#      clicking on the green Run button in Wing101. This will let you call your
#      modified function in the Python shell. An asterisk * on the Wing101
#      w07_markus.py tab indicates that modifications have NOT been saved.
#  (3) Test your function in the Wing101 shell by evaluating the examples from
#      the docstring and confirming that the correct result is displayed.
#  (4) Test your function using different function arguments.
#  (5) When you are convinced that your function is correct, submit your
#      modified file to MarkUs. You can find instructions on submitting a file
#      to MarkUs in Week *2* Perform -> Accessing Part 2 of the
#      Week 2 Perform (For Credit) on PCRS.
#  (6) Verify you have submitted the right file to MarkUs by downloading it
#      and checking that the downloaded file is the one you meant to submit.
#  (7) We have also provided a checker test for you to run on MarkUs. Click on
#      the Automated Testing tab and then Run tests to make sure your code
#      passes our simple test case. Go back to step (1) if errors were reported
#      and modify your work.  You may need to click on some arrows to see all
#      of the error report. Note that we will run additional tests when we mark
#      your submission.
#
#      NOTE: To test this function, you will need to have your test .txt files
#      in the same folder, and those .txt files will need to have the same
#      format as the sample_numbers.txt file that you can download from MarkUs.
#
#      You can use the sample_numbers.txt file to test your code, and you should
#      also test with some other files to convince yourself your code is working
#      correctly.
#
#      Tip: some programs like Notepad may show the .txt file all on one line.
#      You can try opening your .txt files in Wing101 instead.
#
#      You do not need to submit your .txt files.

from typing import List, TextIO


def count_odds_from_file(number_file: TextIO) -> List[int]:
    """Return a list of counts of odd numbers in each section of the file
    number_file. Each section in number_file begins with a line that contains
    only START and ends with a line that contains only END.

    Preconditions: each line in number_file is either START, END, or a string
    of digits that can be converted to an int.
    number_file is properly formatted to contain 0 or more sections structured:
    START
    <0 or more lines of numbers>
    END

    >>> f = open('sample_numbers.txt')
    >>> count_odds_from_file(f)
    [1, 0, 2]
    >>> f.close()
    """
    countList = []
    count = 0
  
  
    for line in f:
        line = line.rstrip()
        if line == "START":
            count=0
        elif line == "END":
            countList.append(count)
        elif int(line)%2 == 0:
            count+=1
  
    return countList
  


f = open("sample_numbers.txt")
print(count_evens_from_file(f))
f.close


