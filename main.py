items = [
  ["phone","blue","pixel"],
  ["computer","silver","lenovo"],
  ["phone","gold","iphone"],
  ["peripheral","black","lenovo"],
  ["phone","black","pinephone"],
  ["computer","orange","macbook"],
]

# Example 1
# rule_key = "color"
# rule_value = "silver"

# Example 2
rule_key = "type"
rule_value = "phone"

count = 0
for item in items:
    if rule_key == 'type':
        if item[0] == rule_value:
            count = count + 1
    elif rule_key == 'color':
        if item[1] == rule_value:
            count = count + 1
    else:
        if item[2] == rule_value:
            count = count + 1

print(count)
