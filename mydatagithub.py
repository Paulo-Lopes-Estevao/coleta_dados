import requests,bs4

userfollower = "Antonio-Gabriel"

requiri = requests.get(f'https://github.com/{userfollower}')

try:

    requiri.raise_for_status()

except Exception as e:
    print("erro : %s" %(e))


requiri.status_code == requests.codes.ok

elemn = bs4.BeautifulSoup(requiri.text)
following=elemn.select(f'a[href="/{userfollower}?tab=following"]')[0].getText()
followers=elemn.select(f'a[href="/{userfollower}?tab=followers"]')[0].getText()
stars=elemn.select(f'a[href="/{userfollower}?tab=stars"]')[0].getText()

print(f"""
{followers}
{following}
{stars}
""")