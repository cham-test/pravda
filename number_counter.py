fixture = "163234693s2942384e72198g3746s1237846§6217984610"
fixture = list(fixture)
for item in fixture:
    if item.isdigit():
        print(item, fixture.count(item))