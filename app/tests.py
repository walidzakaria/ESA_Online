from flask import jsonify
import base64
from app import stores, api


str = '''
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…HHvLa498Pc/mOBrfkf2Y3Jb1xQS3Kv4aE4rTREppx7pVHqCMdSM/Nu+3qGPaeWJxKeDSA6R86UUH82A6fepZ/nF2Vk6OuyO6c3tHa7VMU9ZkNw4LAY6Wem8gkkgx+J/hS17eVLqpk8QUH829nHIfJnvvd3UG4+4XuK1pt4YMbW3S2kmfNdDyrCY4VPA6DI9MAqc9Kdo2zm+WRJ943oxwVqY0CFj8iwXSo+yp+zj1ZrXY+qrsFU42WqIrKrHy0r1kaiM+aSExmZVXhDqN7D6e8kgdJBHkehz1Qb3F0T2b1fn8nJmttZivwjVk81FujE0NTlMbUU5kZoZKtqGOaox9UqWDiRApYXDc2GAHun923nCDfd33zkyAbns91PJN4IZVuYjIxd0KuVEyhidLIxcjDJUVMN8wckblHd3N1tsfj20js2kEa11GpFCe4VOCDX1HQw9M/OzOdYbfx+ztwbewe6cJiIvt6GaDKJt7PU1Mp9MFQZoamkrBCOFLRxSW4Zjb2a8qe9XuzyHt9ly/wA3e3F9eWlrGsSOYJ4JwiAKqswikik0qAoaikgCrMc9Kdu5q5h2iCKz3HZZZY41Cg6XR6DABOllagwDQGnEnown/DlHX4i1NsDPiXRcoNw7cMWr+nm8wYrf86P9h7H8P3nXuAFh9qd9eb0VC2fSojr/AC/Lo5Xn3WKLy/dlvQCv+T/J0lcl/MT3HmyaXr3qQVVVJdYXq8hldxvqIsp+w27iYdRv+POB/j7VH3g9499GjlP2OvI9XCS8Z0QfMhkgX/qp1c8zcy3eNu5UkFfOQkD+YQf8a6QeWx/zW+SC/ZZbF5Xbu1qpgZKCsji2Rt4RM2pRVUavUZ7KIgP6Zw/09k197Z+/vuUvgc+85Wm0bE/xW1t3kr/CyQkK/wBktw49V6TTbHzjvg0bvucdtaHjGmaj0IXj/tnI+XRh+n/gftjatRSZzsjKru/LU7RzxYelhak27TTIQ6mWF3kqckY3HHlbR+dA9yx7f+xnIPt5JDfWFi95vqDF1c6XdD6wxgCOH5FVLj+PoRbPyltGzFZoojLdj/RHoSP9KPhX7QK/PoOfmZ8lqLDRT9K7CrqbGxpClNuvIwTR0mmm0gLgsedUZ0FQPO68W/bH9r3Hn3hOfObIrSfkXkjYdylnnj/xy6htp2VI3H+48MiIQXkB/VdT2IdAOpm0kvOe8bgsb7RtdpOXdf1ZFRiAp/ApA4n8RHAY4k0A/wCKnxzqu189DuXcVLLHsXETxySs6kLn6uJta0UBNhJQxsAZnBIkPpHANwl93f2QltZLbn/nTbmjuI2rY2sqFWQjH1MyMAVYcIEYAj+1IrooXcl8qsjJvG6QEMD+lGwoQR+NgeH9AHh8R8ursKGhpcbSU9DRQR09LSxJDBDEoSOOONQqqqjgAAe80eOTx6lHqX7917qFkqV63H1tJHI0L1NNNAkq/qjaSNkDD/EE+9g0IPXuqCu6+iOyOstx5aoy+3svkcFPW1NTR7nxtHUZOgngmmeVGrWo4556GqVWs/kQISNQbmwwB92vu5c5R8w71zFydbfvPaLy4knMSsouYWlYu6FHKiVNROhkJelAyVFTDnMXJe6JeXN7t0fj20rltII1qWNSKGmoV4EZ9R1m6o72642Xj0we++leud/00MkrR5WSDF4vc0flcu0dZJVUdVBkAjE6S6xSAcFj7X8me+Hub7ebXY8tc3e3t9dWFpGI4nMM8E6xrhUYmJ45Qg7VbtagALNSvTu2c1b3s1vFY7lsskkMY0qdLI4A4AnSQ1OAODTiT0PTfJ34kLHc/GnFLNouI2pNlKha17eQzatN/wA6P9h7kaH70lvcjTbe2m+yT/wrGGz6VAJ/l+XR2vP0L4j2K7ZvQAHpKjvzYu5cpS0/X3w+2NlqQ1EYng/glVuDIVMGsCSOCXC4OChoJ2X6O7TIp+oI9r7b3X97uYLq2PLfspLDt2oamvZWh1LXNGdYVQkcDplp/CeHT0fMPNF7In0HKpWGuTKxWo+RIUA/OjfYerItndMdL7o25is5X9D7W2vW19LHPU4LL7bxJrsdK4u1PM8MJjkKn+0LX/IB495I2U95NaW0t7beBeMgLxhxIEYjK61or0ONQAB406HERdo0aWLRKRlahqH0qMH7elVF8fukIJUmh6p2JHLGweN125jgyMpuGB8HBB9qtTevTlB6dCvSUdLQU8VJRU8NJSwIscNPTxrFDEiiyokaAKqqBwB7r1vqT7917r3v3Xuve/de697917r3v3Xuve/de697917r3v3Xuve/de697917r3v3Xuve/de697917r3v3Xuve/de697917r3v3Xuve/de697917r3v3Xuve/de697917r3v3Xuve/de697917r3v3Xuve/de697917r/1d/j37r3Xvfuvde9+691737r3Xvfuvde9+691737r3Xvfuvde9+691737r3XvfuvdRK+ipsnQ1uNrEMlJkKSpoqqNXeNpKarheCdBJGyyRlopCNSkEfUG/v3Xuq8uxfjjuvas/3e1IandmFqq2aGlo6CmklzOLgKLLTJXRhitXEbSJ5kChdChxqe/t0MDx6ZKEcOgXp9m7vrMpW4Ok2vnqrNY2Npq/FQY6eSupI18Gp5obDSAamMfX6uP6+91Hr1Wh4U6Oh0p8f6naeToN57tqVbM09MJsVhqR5ETEVVXBPT1T5CoV9NdUJSzFFVbRL5GLKzKhFC1RQdOKlMno2HunTnXvfuvde9+691737r3UDKYvH5vHVmJytJBX46vgemq6SpjWSGeFxyrowIuCAQfqrAEcj37r3HqvXsj46bt2zkqmp2hj6vc+2ppojQxUpNTm6H7hpL0VTSj92qho9H/Am/KMmu76iXAw8+PTLIRw4dA3iNlbwz9ZV0GG2zmshV4+pjpMlFBQzH+HTyTy0wWuZlC04WaCQMT+nxsfx7tUevVaH06PB0l0Mmy3Tc+746ar3WDIuPo43SqocDFdkM8MgGipydQv8Au61oozpSxMhajNXA4dOqlMnj0Z33Tq/Xvfuvde9+690wZLau2MzKJsvt7C5OYfSWvxlHVyAf01zwu1v9j7sHdRRWIH29bqRwPTb/AKO9hf8APF7W/wDPDjP/AKm9+8ST/fjftPXqn167Xr7YiMGTZu11YchlwWMBH+sRTe9+JJ/vxv2nr1T69KOkxuOx6COhoKOjQfRKWmhp1H+sIkUD3UknietdTfeuvddMqupVlDKRYqwBUj+hBuCPfuvdIzJdcdf5iY1GV2VtbIzsbtNWYHGTysfrcvJTMxPu4kkUUVyB9p63U+vThitm7Swf/Fm2zgsV/jQYqipT/t4YUPvTOzfExP2nrxJPE9KQAAWAsB9AOB7r1rr3v3XuuDxpIpSREkQixV1DqQfwVYEEe/de6ReT6068zTtJltj7UyMjfqkrMDjJ3a/1Jd6YsSfdxJIuBIwH2nrdT69NtN051PRuJKXrjZUDg3DxbbxSsD9bgimuPe/Fl/3637T16p9elpQYLC4tAmNxGMoEW1lo6GmplFvpYQxJb3QktljU9a6dfeuvde9+690ma3ZWz8jO1TkNrbfral+XnqsRQTzOf6tLLAzsf9c+7B3AoHNPtPW6n16e6KgocdAlNj6OmoqZBZIKSCOnhQD8LHEqoo/1h70SSak5611L96691737r3XvfuvdcJI45VKSxpIjCzJIqupB+oKsCCPfuvdIfK9Xdb5xzJmNibSyUjXLSVmAxk7sT9SXemLEn3cSSAUEjU+09bqfXptpOl+o6CQS0fWuyaeUHUJItuYsMD/UH7Yn34SyDhI37T16pHn0vaHE4vGRiLHY6hoIlFljo6SCmQD6WCwxoALe6kkmpNT1rpw96691737r3Xvfuvde9+691737r3Xvfuvde9+691737r3Xvfuvde9+691737r3Xvfuvde9+691737r3Xvfuvde9+691737r3Xvfuvde9+691737r3Xvfuvde9+691737r3Xvfuvde9+691737r3Xvfuvde9+691737r3Xvfuvde9+691//1t/j37r3Xvfuvde9+691737r3Xvfuvde9+691737r3Xvfuvde9+691737r3Xvfuvde9+691737r3Xvfuvde9+691737r3Xvfuvde9+691737r3Xvfuvde9+691737r3Xvfuvde9+691737r3Xvfuvde9+691737r3Xvfuvde9+691737r3Xvfuvde9+691737r3Xvfuvde9+691737r3Xvfuvde9+691737r3Xvfuvde9+691737r3Xvfuvde9+691737r3Xvfuvde9+691737r3Xvfuvde9+691737r3Xvfuvde9+691737r3Xvfuvde9+691737r3Xvfuvde9+691737r3Xvfuvde9+691737r3Xvfuvde9+691737r3Xvfuvde9+691737r3Xvfuvde9+691737r3Xvfuvde9+691737r3Xvfuvde9+691737r3Xvfuvde9+691737r3X/9ff49+691737r3Xvfuvde9+691737r3Xvfuvde9+691737r3Xvfuvde9+691737r3Xvfuvde9+691737r3Xvfuvde9+691737r3Xvfuvde9+691737r3Xvfuvde9+691737r3Xvfuvde9+691737r3Xvfuvde9+691737r3Xvfuvde9+691737r3Xvfuvde9+691737r3Xvfuvde9+691737r3Xvfuvde9+691737r3Xvfuvde9+691737r3Xvfuvde9+691737r3Xvfuvde9+691737r3Xvfuvde9+691737r3Xvfuvde9+691737r3Xvfuvde9+691737r3Xvfuvde9+691737r3Xvfuvde9+691737r3Xvfuvde9+691737r3Xvfuvde9+691737r3Xvfuvde9+691737r3Xvfuvde9+691737r3Xvfuvde9+691737r3Xvfuvde9+691//Z
'''
image_data = base64.b64decode(str.encode('utf-8'))
image_data = base64.b64
file_name = 'image.jpg'
with open(file_name, 'wb') as f:
    f.write(image_data)
