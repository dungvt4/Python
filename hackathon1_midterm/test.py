import re

pattern_year = """Popularity in (\d+)"""
pattern_rank = """<td>(\d+)</td><td>([a-zA-Z]+)</td><td>([a-zA-Z]+)</td>"""
year = 0
list_rslt = []
with open("baby1990.html", "r", encoding='utf-8-sig') as f:
    lines = f.readlines()
    for line in lines:
      re_year = re.search(pattern_year, line)
      if re_year:
        year = re_year.groups()[0]
      re_rank = re.findall(pattern_rank, line)
    #   print(re_rank.groups()[1])
      if re_rank:
        list_rslt.append(re_rank[0][1] + " " + re_rank[0][0])
        list_rslt.append(re_rank[0][2] + " " + re_rank[0][0])
    #     list_rslt.append(re_rank.groups()[1] + " " + re_rank.groups()[0])
    #     list_rslt.append(re_rank.groups()[2] + " " + re_rank.groups()[0])
    list_rslt.insert(0, year)
print(list_rslt)     
