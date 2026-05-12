"""
Phone number and email searcher.



REGEX IN PYTHON:
	Regex can be used in many different languages and in any situation where you need to search for or validate certain patterns of text and is included in the search capabilities of many pieces of software.
	Regex in Python is "greedy" by default (will select the longest string in ambiguous situations)
	Use "?" to make it "non-greedy"

BASIC FUNCTIONS AND OPERATORS:
	import re
	re.compile()
	.search()
	.group()
	Grouping with parentheses()
	Matching with Pipe | (OR)
	? matches zero or one of the preceding group
	* matches zero or more of the preceding group
	+ matches one or more of the preceding group
	{n} matches exactly n of the preceding group
	{n,} matches n or more of the preceding group
	{,m} matches 0 to m of the preceding group
	{n,m} matches at least n and at most m of the preceding group
	{n,m}? or *? or +? performs a nongreedy match of the preceding group
	.findall() for returning every match (not just the first one)

CHARACTER CLASSES:
	\d = 0-9
	\D = not \d
	\w = letter, numeric, or _
	\W = not \w
	\s = space, tab, newline
	\S = not \s
	[abcde] or [^abcde] (^ is the opposite)

START OR END:
	^ = begins with eg. re.compile(r'^Hello') means the text has to begin with 'Hello'
	$ = ends with eg. re.compile(r'\d$') means the text has to end with a digit
	Begin AND end with: eg. re.compile(r'^\d$') means it has to begin and end with a digit

WILDCARD:
	. = anything (except newline)
	.* = anything

IGNORE CASE:
	re.compile(r'mickey mouse', re.I) will search for Mickey Mouse but ignore the case

SUBSTITUTION:
	Regex can find and replace using regex.sub([what to replace with], [the string])


"""

# Import re and pyperclip


# Get text from clipboard
# pyperclip.paste() will be the text in your clipboard


# Search for phone numbers + emails


# Replace text in keyboard with found phone numbers and email
# pyperclip.copy() will put the new text back onto the clipboard
