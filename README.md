# Env File Policy Check

Parse `.env`-style text and report missing, forbidden, blank, and duplicate keys without printing values.

```bash
cat policy.json | python tool.py
python -m unittest -v
```

Use safe non-production fixture data in tests. This utility does not manage secrets or read environment files unless passed explicitly.
