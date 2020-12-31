import vk_api
import urllib.request


def download(url):
    img = urllib.request.urlopen(url).read()
    out = open("meme.jpg", "wb")
    out.write(img)
    out.close()


vk_session = vk_api.VkApi('+79002355569', 'matrosovaDOM30')
vk_session.auth()

vk = vk_session.get_api()
res = vk.wall.get(count=1, owner_id=-67580761)

sizes = res['items'][0]['attachments'][0]['photo']['sizes']
meme = sizes[len(sizes) - 1]['url']

download(meme)
print(meme)
