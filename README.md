# 🐍 Flask Basics

Applied fundamentals of Flask web framework.

---

## 📁 Project Structure

```
├── app.py          # Basic Flask app with simple routes
├── main.py         # Flask app with HTML template rendering
├── getpost.py      # Handling GET and POST requests + forms
├── jinja.py        # Jinja2 templating with dynamic URLs and variable rules
├── api.py          # REST API with GET, POST, PUT, DELETE methods
└── templates/
    ├── index.html  # Home page template
    ├── about.html  # About page template
    ├── form.html   # Form input page
    ├── result.html     # Displays pass/fail result
    └── result1.html    # Displays result using Jinja2 loop
```

---

## 📌 What's Covered

| File | Concept |
|------|---------|
| `app.py` | Creating a Flask app, basic routing |
| `main.py` | Rendering HTML templates |
| `getpost.py` | GET & POST methods, form handling |
| `jinja.py` | Jinja2 templates, variable rules, dynamic URLs |
| `api.py` | Building a REST API (CRUD operations) |

---

## 📚 Concepts Used

- Flask routing & decorators
- Jinja2 template engine (`{{ }}`, `{% %}`, `{# #}`)
- HTTP methods: GET, POST, PUT, DELETE
- `render_template`, `request`, `jsonify`
- Dynamic URL rules with variable types (`<int:score>`)

---

## 👤 Author

Made with ❤️ while learning Flask.
