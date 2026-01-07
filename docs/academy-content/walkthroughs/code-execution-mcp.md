# Code Execution MCP Integration Guide

> **Support Forge AI Launchpad Academy**
> Run Python and JavaScript through Claude with Zapier's Code by Zapier

---

## Overview

Sometimes you need to process data, perform calculations, or transform information in ways that require actual code execution. With Zapier's Code by Zapier MCP tools, Claude can write and execute Python or JavaScript code to accomplish complex tasks.

**What you'll learn:**
- Execute Python code through Claude
- Run JavaScript/Node.js scripts
- Process data and transform formats
- Build complex automation logic

---

## Prerequisites

- [ ] Zapier MCP configured ([see setup guide](./zapier-mcp-setup.md))
- [ ] Code by Zapier enabled in your Zapier account
- [ ] Understanding of Python or JavaScript basics

---

## Available Tools

| Tool | Description |
|------|-------------|
| `code_by_zapier_run_python` | Execute Python code |
| `code_by_zapier_run_javascript` | Execute JavaScript code |

---

## Python Code Execution

### Example: Basic Calculation

```
Calculate the compound interest on $10,000 at 5% annual rate for 10 years
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__code_by_zapier_run_python",
  "parameters": {
    "instructions": "Calculate compound interest",
    "code": "principal = 10000\nrate = 0.05\ntime = 10\ncompound_interest = principal * (1 + rate) ** time\nresult = round(compound_interest, 2)\noutput = {'final_amount': result, 'interest_earned': round(result - principal, 2)}"
  }
}
```

### Example: Data Processing

```
Parse a CSV string and calculate the total sales
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__code_by_zapier_run_python",
  "parameters": {
    "instructions": "Parse CSV and calculate totals",
    "code": "import csv\nfrom io import StringIO\n\ncsv_data = input_data.get('csv_string')\nreader = csv.DictReader(StringIO(csv_data))\n\ntotal_sales = 0\nitems = []\nfor row in reader:\n    amount = float(row['amount'])\n    total_sales += amount\n    items.append({'product': row['product'], 'amount': amount})\n\noutput = {'total_sales': round(total_sales, 2), 'item_count': len(items), 'items': items}",
    "input": "{\"csv_string\": \"product,amount\\nWidget A,150.00\\nWidget B,250.00\\nWidget C,100.00\"}"
  }
}
```

### Example: Date Calculations

```
Calculate the number of business days between two dates
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__code_by_zapier_run_python",
  "parameters": {
    "instructions": "Calculate business days between dates",
    "code": "from datetime import datetime, timedelta\n\nstart = datetime.strptime(input_data['start_date'], '%Y-%m-%d')\nend = datetime.strptime(input_data['end_date'], '%Y-%m-%d')\n\nbusiness_days = 0\ncurrent = start\nwhile current <= end:\n    if current.weekday() < 5:  # Monday = 0, Friday = 4\n        business_days += 1\n    current += timedelta(days=1)\n\noutput = {'start_date': input_data['start_date'], 'end_date': input_data['end_date'], 'business_days': business_days}",
    "input": "{\"start_date\": \"2026-01-05\", \"end_date\": \"2026-01-31\"}"
  }
}
```

### Example: JSON Transformation

```
Transform a nested JSON structure into a flat format
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__code_by_zapier_run_python",
  "parameters": {
    "instructions": "Flatten nested JSON",
    "code": "import json\n\ndef flatten_dict(d, parent_key='', sep='_'):\n    items = []\n    for k, v in d.items():\n        new_key = f'{parent_key}{sep}{k}' if parent_key else k\n        if isinstance(v, dict):\n            items.extend(flatten_dict(v, new_key, sep=sep).items())\n        elif isinstance(v, list):\n            for i, item in enumerate(v):\n                if isinstance(item, dict):\n                    items.extend(flatten_dict(item, f'{new_key}_{i}', sep=sep).items())\n                else:\n                    items.append((f'{new_key}_{i}', item))\n        else:\n            items.append((new_key, v))\n    return dict(items)\n\nnested_data = json.loads(input_data['json_string'])\noutput = flatten_dict(nested_data)",
    "input": "{\"json_string\": \"{\\\"user\\\": {\\\"name\\\": \\\"John\\\", \\\"address\\\": {\\\"city\\\": \\\"NYC\\\", \\\"zip\\\": \\\"10001\\\"}}, \\\"orders\\\": [{\\\"id\\\": 1, \\\"total\\\": 99.99}]}\"}"
  }
}
```

### Example: Text Processing

```
Extract all email addresses from a block of text
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__code_by_zapier_run_python",
  "parameters": {
    "instructions": "Extract emails from text",
    "code": "import re\n\ntext = input_data.get('text', '')\nemail_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}'\nemails = re.findall(email_pattern, text)\n\noutput = {'emails': list(set(emails)), 'count': len(set(emails))}",
    "input": "{\"text\": \"Contact us at support@example.com or sales@example.com. For billing: billing@example.com\"}"
  }
}
```

### Example: API Data Processing

```
Process a list of items and calculate statistics
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__code_by_zapier_run_python",
  "parameters": {
    "instructions": "Calculate statistics from item list",
    "code": "import json\nfrom statistics import mean, median, stdev\n\nitems = json.loads(input_data['items'])\nprices = [item['price'] for item in items]\n\nstats = {\n    'count': len(prices),\n    'total': round(sum(prices), 2),\n    'average': round(mean(prices), 2),\n    'median': round(median(prices), 2),\n    'min': min(prices),\n    'max': max(prices)\n}\n\nif len(prices) > 1:\n    stats['std_dev'] = round(stdev(prices), 2)\n\noutput = stats",
    "input": "{\"items\": \"[{\\\"name\\\": \\\"A\\\", \\\"price\\\": 10.50}, {\\\"name\\\": \\\"B\\\", \\\"price\\\": 25.00}, {\\\"name\\\": \\\"C\\\", \\\"price\\\": 15.75}, {\\\"name\\\": \\\"D\\\", \\\"price\\\": 30.00}]\"}"
  }
}
```

---

## JavaScript Code Execution

### Example: Basic Calculation

```
Calculate the total with tax for a shopping cart
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__code_by_zapier_run_javascript",
  "parameters": {
    "instructions": "Calculate cart total with tax",
    "code": "const items = JSON.parse(inputData.items);\nconst taxRate = parseFloat(inputData.taxRate) || 0.08;\n\nconst subtotal = items.reduce((sum, item) => sum + (item.price * item.quantity), 0);\nconst tax = subtotal * taxRate;\nconst total = subtotal + tax;\n\noutput = {\n  subtotal: subtotal.toFixed(2),\n  tax: tax.toFixed(2),\n  total: total.toFixed(2),\n  itemCount: items.reduce((sum, item) => sum + item.quantity, 0)\n};",
    "input": "{\"items\": \"[{\\\"name\\\": \\\"Widget\\\", \\\"price\\\": 25.00, \\\"quantity\\\": 2}, {\\\"name\\\": \\\"Gadget\\\", \\\"price\\\": 50.00, \\\"quantity\\\": 1}]\", \"taxRate\": \"0.0825\"}"
  }
}
```

### Example: String Manipulation

```
Convert a title to URL-friendly slug
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__code_by_zapier_run_javascript",
  "parameters": {
    "instructions": "Convert title to slug",
    "code": "const title = inputData.title;\n\nconst slug = title\n  .toLowerCase()\n  .trim()\n  .replace(/[^\\w\\s-]/g, '')\n  .replace(/[\\s_-]+/g, '-')\n  .replace(/^-+|-+$/g, '');\n\noutput = { original: title, slug: slug };",
    "input": "{\"title\": \"How to Build Amazing Web Apps in 2026!\"}"
  }
}
```

### Example: Date Formatting

```
Format a date in multiple formats
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__code_by_zapier_run_javascript",
  "parameters": {
    "instructions": "Format date in multiple ways",
    "code": "const dateStr = inputData.date;\nconst date = new Date(dateStr);\n\nconst formats = {\n  iso: date.toISOString(),\n  us: date.toLocaleDateString('en-US'),\n  eu: date.toLocaleDateString('en-GB'),\n  long: date.toLocaleDateString('en-US', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' }),\n  time: date.toLocaleTimeString('en-US'),\n  relative: getRelativeTime(date)\n};\n\nfunction getRelativeTime(date) {\n  const now = new Date();\n  const diff = now - date;\n  const days = Math.floor(diff / (1000 * 60 * 60 * 24));\n  if (days === 0) return 'Today';\n  if (days === 1) return 'Yesterday';\n  if (days < 7) return `${days} days ago`;\n  if (days < 30) return `${Math.floor(days / 7)} weeks ago`;\n  return `${Math.floor(days / 30)} months ago`;\n}\n\noutput = formats;",
    "input": "{\"date\": \"2026-01-04T10:30:00Z\"}"
  }
}
```

### Example: Array Operations

```
Group items by category and sum their values
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__code_by_zapier_run_javascript",
  "parameters": {
    "instructions": "Group and sum items by category",
    "code": "const items = JSON.parse(inputData.items);\n\nconst grouped = items.reduce((acc, item) => {\n  const category = item.category;\n  if (!acc[category]) {\n    acc[category] = { total: 0, count: 0, items: [] };\n  }\n  acc[category].total += item.amount;\n  acc[category].count += 1;\n  acc[category].items.push(item.name);\n  return acc;\n}, {});\n\n// Round totals\nObject.keys(grouped).forEach(key => {\n  grouped[key].total = Math.round(grouped[key].total * 100) / 100;\n});\n\noutput = grouped;",
    "input": "{\"items\": \"[{\\\"name\\\": \\\"Coffee\\\", \\\"category\\\": \\\"Food\\\", \\\"amount\\\": 4.50}, {\\\"name\\\": \\\"Sandwich\\\", \\\"category\\\": \\\"Food\\\", \\\"amount\\\": 8.00}, {\\\"name\\\": \\\"Notebook\\\", \\\"category\\\": \\\"Office\\\", \\\"amount\\\": 12.00}]\"}"
  }
}
```

### Example: Data Validation

```
Validate a user registration object
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__code_by_zapier_run_javascript",
  "parameters": {
    "instructions": "Validate user registration data",
    "code": "const user = JSON.parse(inputData.user);\nconst errors = [];\n\n// Email validation\nconst emailRegex = /^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/;\nif (!user.email || !emailRegex.test(user.email)) {\n  errors.push('Invalid email address');\n}\n\n// Password validation\nif (!user.password || user.password.length < 8) {\n  errors.push('Password must be at least 8 characters');\n}\nif (user.password && !/[A-Z]/.test(user.password)) {\n  errors.push('Password must contain uppercase letter');\n}\nif (user.password && !/[0-9]/.test(user.password)) {\n  errors.push('Password must contain a number');\n}\n\n// Name validation\nif (!user.name || user.name.trim().length < 2) {\n  errors.push('Name must be at least 2 characters');\n}\n\n// Age validation\nif (user.age && (user.age < 13 || user.age > 120)) {\n  errors.push('Age must be between 13 and 120');\n}\n\noutput = {\n  valid: errors.length === 0,\n  errors: errors,\n  user: errors.length === 0 ? user : null\n};",
    "input": "{\"user\": \"{\\\"email\\\": \\\"test@example.com\\\", \\\"password\\\": \\\"SecurePass1\\\", \\\"name\\\": \\\"John Doe\\\", \\\"age\\\": 25}\"}"
  }
}
```

### Example: Generate HTML

```
Generate an HTML email template from data
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__code_by_zapier_run_javascript",
  "parameters": {
    "instructions": "Generate HTML email template",
    "code": "const data = JSON.parse(inputData.data);\n\nconst html = `\n<!DOCTYPE html>\n<html>\n<head>\n  <style>\n    body { font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; }\n    .header { background: #333; color: white; padding: 20px; text-align: center; }\n    .content { padding: 20px; }\n    .item { border-bottom: 1px solid #eee; padding: 10px 0; }\n    .total { font-weight: bold; font-size: 1.2em; margin-top: 20px; }\n    .footer { background: #f5f5f5; padding: 15px; text-align: center; font-size: 0.9em; }\n  </style>\n</head>\n<body>\n  <div class=\"header\">\n    <h1>Order Confirmation</h1>\n  </div>\n  <div class=\"content\">\n    <p>Thank you for your order, ${data.customerName}!</p>\n    <h3>Order Details:</h3>\n    ${data.items.map(item => `\n      <div class=\"item\">\n        <strong>${item.name}</strong> x ${item.quantity}<br>\n        $${(item.price * item.quantity).toFixed(2)}\n      </div>\n    `).join('')}\n    <div class=\"total\">\n      Total: $${data.items.reduce((sum, item) => sum + (item.price * item.quantity), 0).toFixed(2)}\n    </div>\n  </div>\n  <div class=\"footer\">\n    Questions? Contact support@example.com\n  </div>\n</body>\n</html>\n`;\n\noutput = { html: html };",
    "input": "{\"data\": \"{\\\"customerName\\\": \\\"John Doe\\\", \\\"items\\\": [{\\\"name\\\": \\\"Widget Pro\\\", \\\"price\\\": 29.99, \\\"quantity\\\": 2}, {\\\"name\\\": \\\"Widget Basic\\\", \\\"price\\\": 14.99, \\\"quantity\\\": 1}]}\"}"
  }
}
```

---

## Input/Output Patterns

### Input Data Structure

Input data is passed as a JSON string in the `input` parameter:

```json
{
  "input": "{\"key1\": \"value1\", \"key2\": \"value2\"}"
}
```

**Accessing in Python:**
```python
value = input_data.get('key1')
# or
value = input_data['key1']
```

**Accessing in JavaScript:**
```javascript
const value = inputData.key1;
// or
const value = inputData['key1'];
```

### Output Structure

**Python:**
```python
output = {'result': 'value', 'count': 42}
```

**JavaScript:**
```javascript
output = { result: 'value', count: 42 };
```

---

## Common Errors and Fixes

### Error: "Code execution timeout"

**Cause:** Code takes too long to execute (limit ~30 seconds)

**Fix:**
- Optimize loops and reduce complexity
- Process smaller data batches
- Avoid synchronous delays

### Error: "Memory limit exceeded"

**Cause:** Working with too much data

**Fix:**
- Process data in chunks
- Avoid loading large arrays into memory
- Use generators in Python

### Error: "Module not found"

**Cause:** Trying to import unavailable library

**Fix:**
Python available modules:
- `json`, `re`, `datetime`, `math`
- `csv`, `hashlib`, `base64`
- `collections`, `itertools`
- `urllib` (limited)

JavaScript: Only standard Node.js built-ins

### Error: "Syntax error"

**Cause:** Invalid code syntax

**Fix:**
- Validate code before submitting
- Check for proper escaping in JSON
- Watch for quotes within strings

### Error: "input_data / inputData is undefined"

**Cause:** Input not properly formatted

**Fix:**
- Ensure `input` parameter is valid JSON string
- Check for proper escaping of nested JSON
- Use `input_data.get('key', default)` in Python

---

## Pro Tips

### 1. Escape Nested JSON Properly

When passing JSON inside JSON:
```json
{
  "input": "{\"data\": \"{\\\"nested\\\": \\\"value\\\"}\"}"
}
```

### 2. Use Error Handling

**Python:**
```python
try:
    value = int(input_data.get('number', '0'))
except ValueError:
    value = 0
output = {'value': value}
```

**JavaScript:**
```javascript
try {
  const value = JSON.parse(inputData.data);
  output = { success: true, data: value };
} catch (e) {
  output = { success: false, error: e.message };
}
```

### 3. Debug with Output

Include debug information:
```python
output = {
    'result': calculated_value,
    'debug': {
        'input_received': input_data,
        'intermediate_value': step1_result
    }
}
```

### 4. Keep Code Concise

Zapier has character limits. Write efficient code:
```python
# Concise
output = {'sum': sum(float(x) for x in input_data['values'].split(','))}

# Instead of verbose loops
```

### 5. Format Output for Next Steps

Return data in formats useful for downstream actions:
```python
# For Google Sheets
output = {
    'row1_col_a': value1,
    'row1_col_b': value2,
    'row1_col_c': value3
}
```

### 6. Use Python for Complex Math

Python has better numeric handling:
```python
from decimal import Decimal, ROUND_HALF_UP

price = Decimal(input_data['price'])
tax = price * Decimal('0.0825')
total = (price + tax).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
output = {'total': str(total)}
```

---

## Workflow Examples

### Data Transformation Workflow

```
1. Get data from Google Sheets (rows)
2. Run Python to calculate aggregations
3. Generate summary report
4. Create new Sheet with results
```

### Email Processing Workflow

```
1. Find emails in Gmail
2. Run JavaScript to extract key data
3. Validate with code
4. Add to CRM spreadsheet
```

### Report Generation Workflow

```
1. Query multiple data sources
2. Run Python to combine and analyze
3. Generate HTML report
4. Send via email
```

### API Data Processing

```
1. Receive webhook data
2. Validate with JavaScript
3. Transform data structure
4. Forward to destination system
```

---

## Integration Scenarios

### Code + Google Sheets

```python
# Process spreadsheet data
rows = json.loads(input_data['rows'])
processed = [
    {
        'name': row['name'].upper(),
        'value': float(row['value']) * 1.1
    }
    for row in rows
]
output = {'processed_rows': processed}
```

### Code + Gmail

```javascript
// Parse email for order data
const emailBody = inputData.email_body;
const orderMatch = emailBody.match(/Order #(\d+)/);
const amountMatch = emailBody.match(/\$(\d+\.\d{2})/);

output = {
  orderNumber: orderMatch ? orderMatch[1] : null,
  amount: amountMatch ? parseFloat(amountMatch[1]) : null
};
```

### Code + AI Studio

```python
# Post-process AI response
ai_response = input_data['gemini_response']
# Extract structured data
lines = ai_response.split('\n')
bullets = [line.strip('- ').strip() for line in lines if line.startswith('-')]
output = {'key_points': bullets, 'count': len(bullets)}
```

---

## Next Steps

- [Google Workspace MCP Guide](./google-workspace-mcp.md) - Store processed data
- [AI Studio MCP Guide](./ai-studio-mcp.md) - Generate data to process
- [GitHub MCP Guide](./github-mcp.md) - Automate code workflows

---

*Support Forge AI Launchpad Academy - Building the Future of AI Integration*
