## Adding Whitespace to Strings with Tabs or Newlines

print("Python")
print("\tPython")

print("Languages:\nPython\nC\nJavaScript")

print("Languages:\n\tPython\n\tC\n\tJavascript")


## Stripping Whitespace

favorite_language = 'python '
favorite_language
# 'python '
favorite_language.rstrip()
# 'python'
favorite_language
# 'python '

favorite_language = 'python '
favorite_languag = favorite_languag.rstrip()
favorite_languag
# 'python'

favorite_language = ' python '
favorite_language.rstrip()
# ' python'
favorite_language.lstrip()
# 'python '
favorite_language.strip()
# 'python'
