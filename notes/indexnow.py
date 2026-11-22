# Tell Bing (and the other IndexNow engines) that the site's pages changed, so they're crawled now instead of later.
#   python notes/indexnow.py          (run after a deploy has finished)
# The key file <key>.txt at the site root proves the site is ours. URLs come from sitemap.xml.
import glob, json, re, urllib.request
key = [f[:-4] for f in glob.glob('*.txt') if re.fullmatch(r'[0-9a-f]{32}\.txt', f)][0]
urls = re.findall(r'<loc>([^<]+)</loc>', open('sitemap.xml', encoding='utf-8').read())
body = json.dumps({'host': 'getbrandfig.com', 'key': key, 'keyLocation': f'https://getbrandfig.com/{key}.txt', 'urlList': urls}).encode()
req = urllib.request.Request('https://api.indexnow.org/indexnow', data=body, headers={'Content-Type': 'application/json; charset=utf-8'})
with urllib.request.urlopen(req) as r: print(r.status, len(urls), 'URLs sent')
