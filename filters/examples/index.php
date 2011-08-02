<? require("../../../2041.php");
   echo startPage("Examples","","Filters and Regexps");
?>

This file contains examples of the use of the most common Unix
filter programs (<tt>grep</tt>, <tt>wc</tt>, <tt>head</tt>, etc.)
It also contains solutions to the exercises discussed in lectures.

<ol>

<p><li>

<p>
Consider a a file <a href="./course_codes">course_codes</a>
containing UNSW course codes and names.
</p>
<pre>
<?demo("ls -l course_codes");?>
<?demo("wc course_codes");?>
<?demo("head course_codes");?>
</pre>
<p>
It looks like the code is separated from the title by a number of
spaces. We can check this via <tt>cat -A</tt>:
</p>
<pre>
<?demo("head -5 course_codes | cat -A");?>
</pre>
<p>
This shows us that our initial guess was wrong, and
there's actually a tab character between the course code and title
(shown as <tt>^I</tt> by <tt>cat -A</tt>).
Also, the location of the end-of-line marker (<tt>$</tt>) indicates
that there are no trailing spaces or tabs.
</p>
<p>
If we need to know what COMP courses there are:
</p>
<pre>
<?demo("grep -c COMP course_codes");?>
<?demo("grep COMP course_codes",10);?>
</pre>
<p>
Either of the two commands below tell us which courses
have "comp" in their name or code (in upper or lower case).
</p>
<pre>
<?demo("tr A-Z a-z < course_codes | grep comp",10);?>
<?demo("grep -i comp course_codes",10);?>
</pre>
<p>
The second one looks better because the data itself isn't transformed,
only the internal comparisons.
</p>
<p>
If we want to know how many courses have
"computing" or "computer" in their title,
we have to use <tt>egrep</tt>, which recognises the alternative operator "|",
and <tt>wc</tt> to count the number of matches.
There are a couple of ways to construct the regexp:
</p>
<pre>
<?demo("egrep -i 'computer|computing' course_codes | wc");?>
<?demo("egrep -i 'comput(er|ing)' course_codes | wc");?>
</pre>
<p>
If you don't like the irrelevant word and character counts,
use <tt>wc -l</tt>.
</p>
<p>
Most of these 80 matches were CSE offerings,
whose course codes begin with COMP, SENG or BINF.
Which of the matches were courses offered by other schools?
</p>
<p>
Think about it for a moment.... There's no "but not" regexp operator,
so instead we construct a composite filter with an extra step to deal
with eliminating the CSE courses:
</p>
<pre>
<?demo("egrep -i 'computer|computing' course_codes | egrep -v '^(COMP|SENG|BINF)'",10,5);?>
</pre>
<p>
The last ones are from the Computer Science school at ADFA.
</p>

<p><li>

Consider a file called <a href="./enrolments">enrolments</a>
which contains data about student enrolment in courses.
There is one line for each student enrolled in a course:
<pre>
<?demo("ls -l enrolments");?>
<?demo("wc enrolments");?>
<?demo("head enrolments");?>
</pre>
<p>
The following commands count how many students are enrolled in
COMP2041 or COMP9041.
The course IDs differ only in one character,
so a character class is used instead of alternation.
<p>
The first version below is often preferred because initially you may want
to know "<i>how many xxx</i>", then having found that out
the next question might be, "<i>well give me a sample of 10 or so of them</i>".
Then it's a simple matter of replacing <tt>wc</tt> by <tt>head</tt>.
</p>
<pre>
<?demo("grep '^COMP[29]041' enrolments | wc -l");?>
<?demo("grep -c '^COMP[29]041' enrolments");?>
</pre>
<p>
The last field field in the enrolment file records the student's gender.
This command counts the number of female students enrolled in the courses.
</p>
<pre>
<?demo("grep '^COMP[29]041' enrolments | grep '|F\$' | wc -l");?>
</pre>
<p>
Not a very good gender balance, is it?
</o>
<p>
By the way, the two <tt>grep</tt>s could have been combined into one. How?
</p>
<p>
This command will give a sorted list of course codes:
</p>
<pre>
<?demo("cut -d'|' -f1 enrolments | sort | uniq",5);?>
</pre>
<p>
The student records system known to users as myUNSW is built on top of
a large US product known as PeopleSoft
(the company was taken over by Oracle in 2004).
On a scale of 1 to 10 the quality of the design of this product is about 3.
One of its many flaws is its insistence that everybody must have two names,
a "Last Name" and a "First Name", neither of which can be empty.
To signify that a person has only a single name
(common in Sri Lanka, for example), the system stores a dot character
in the "First Name" field.
The enrolments file shows the data as stored in the system,
with a comma and space separating the component names.
It has some single-named people (note that the names themselves
have been disguised):
</p>
<pre>
<?demo("grep ', \\.' enrolments",10);?>
</pre>
<p>
What would have happened if we forgot the backslash?
</p>
<p>
If we wanted to know how many different students there were of this type
rather than all enrolments,
just cut out the second field (student ID) and use <tt>uniq</tt>.
It's not necessary to sort the data in this case only because
the data is <i><b>clustered,</b></i> that is, all equal values are adjacent
although they're not necessarily sorted.
</p>
<pre>
<?demo("grep ', \\.' enrolments | cut -d'|' -f2 | uniq | wc");?>
</pre>

<p><li>

Now let us turn our attention from students and courses to programs.
The <a href="./enrolments">enrolments</a> file, as well as linking
a student to the courses they're taking, also links them to the
program (degree) that they are currently enrolled in.
Consider that we want to find out the program codes of the students
taking COMP2041.
The following pipeline will do this:
<p>
<pre>
<?demo("grep 'COMP[29]041' enrolments | cut -d'|' -f4 | cut -d/ -f1  |sort | uniq");?>
</pre>
<p>
If we want to know how many students come from each program,
ordered from most common program to least common program, try this:
</p>
<pre>
<?demo("grep COMP[29]041 enrolments | cut -d'|' -f4 | cut -d/ -f1 | sort | uniq -c | sort -nr",15);?>
</pre>
<p>
Note that a tab is usually inserted between the count and the data,
but not all implementations of the <tt>uniq</tt> command ensure this.
</p>

<p><li>

<p>
Consider a file called <a href="./program_codes">program_codes</a>
that contains the code and name of each program offered at UNSW
(excluding research programs):
<p>
<pre>
<?demo("wc program_codes");?>
<?demo("head program_codes");?>
</pre>
<p>
We can use this file to give more details of the programs that COMP2041
students are taking, if some users don't want to deal with just course
codes.
</p>
<pre>
<?demo("grep COMP[29]041 enrolments | cut -d'|' -f4 | cut -d/ -f1 | \n".
	"sort | uniq | join - program_codes",30);?>
</pre>
<p>
We can combine the enrolment counts (for both courses)
with the program titles to produce a self-descriptive tally.
It's even better if it's in decreasing order of popularity,
so after joining the tallies with the program titles,
re-sort the composite data:
</p>
<pre>
<?demo("grep 'COMP[29]041' enrolments | cut -d'|' -f4 | cut -d/ -f1 |\n".
	"sort | uniq -c | join -1 2 -a 1 - program_codes  | sort -k2rn",30);?>
</pre>
<p>
Note the curious extra space before the title of programs 8682 and 8684.
It took me a while to work it out, can you?
(Hint: how are the programs shown in the enrolment file?)
Suggest an appopriate change to the pipeline.
</p>

<p><li>

<p>
Lecture exercise on <tt>ls</tt>, <tt>cat</tt>
</p>
<ol type="a">
<p><li> what files are in the current directory?
(/home/cs2041/web/07s2/lec/A/examples/)
</p>
<pre>
<?demo("ls -lg .");?>
</pre>
<p><li> what files are in the current directory?
</p>
<pre>
<?demo("cat -n count.c");?>
</pre>
<p><li> look for invisible characters? (see example above)
</ol>

<p><li>

<p>
Lecture exercises on <tt>wc</tt>:
</p>
<ol type="a">
<p><li> how many different programs does UNSW offer?
</p>
<pre>
<?demo("wc -l program_codes");?>
</pre>
<p><li> how many times was WebCMS accessed?
</p>
<pre>
<?demo("wc -l access_log");?>
</pre>
<p><li> how many students are studying in CSE?
</p>
<pre>
<?demo("wc -l enrolments");?>
</pre>
<p>
The above solution assume that we're talking about total enrolments.
If the question actually meant how many disctinct indivduals are
studying courses offered by CSE, then we'd answer it as:
</p>
<pre>
<?demo("cut -d'|' -f2 enrolments | sort | uniq | wc -l");?>
</pre>
<p><li> how many words are there in the <a href="./book">book</a>?
</p>
<pre>
<?demo("wc -w book");?>
</pre>
<p><li> how many lines are there in the <a href="./story">story</a>? 
</p>
<pre>
<?demo("wc -l story");?>
</pre>
</ol>

<p><li> More to follow ...

</ol>
</body>
</html>
