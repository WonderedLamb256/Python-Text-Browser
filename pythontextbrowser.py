print("Python Text Browser")
from urllib.request import urlopen
def search(site):
	with urlopen(site) as page:
		for text in page:
			text = text.decode('utf-8') # Decodes to UTF8
			if '<title>' in text or 'href=' in text or 'content=' in text: # These are common prefixes found in HTML related to text.
				print(text)
