# Items Matching a Rule

In this practice, you need to count items matching a specific rule within a 2D list.

You'll use a loop with a complicated condition, and practice accessing items
inside of lists. It will help if you are to be able to visualize the list
structure.

## Your Task

You are given a list of items. 

Each item is a list, with a color, type, and a name, like `["phone", "blue", "pixel"]`.

Your task will be to count how many items in the list match the _rule_.

A rule is represented by two strings: `rule_key` and `rule_value`.

The item matches the rule if the value matches for that type. Here's what would happen for these rules and our example item, `["phone", "blue", "pixel"]` 

| rule_key 	| rule_value 	| match? 	|
|----------	|------------	|--------	|
| "type"   	| "phone"    	| True   	|
| "type"   	| "computer" 	| False  	|
| "color"  	| "blue"     	| True   	|
| "color"  	| "red"      	| False  	|
| "name"   	| "pixel"    	| True   	|
| "name"   	| "lenovo"   	| False  	|

Your program should print out the number of items that match the given rule.

You need to implement your code to run successfully usin both examples in the starter code. Then, try at least 3 more example rules to run using your code. You can leave them as comments.

## Starter Code

Check the file called `main.py` where you a starter code to write your code.
You are given input list examples also.

## Expected Results

### Color Rule

**Input:**  `items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], rule_key = "color", rule_value = "silver"`

**Output:** 1

**Explanation:** There is only one item matching the given rule, which is `["computer","silver","lenovo"]`.

### Type Rule

**Input:** `items = [["phone","blue","pixel"],["computer","silver","lenovo"], ["phone","gold","iphone"]], rule_key = "type", rule_value = "phone"`

**Output:** 2

**Explanation:** There are only two items matching the given rule, which are `["phone","blue","pixel"]` and `["phone","gold","iphone"]`. The item `["computer","silver","lenovo"]` does not match.

## Testing

Run the program manually to check that it has the expected results.
