# Concepts

Nouns map atomically to file sets (EXTRACTED); verbs aggregate structural edges (INFERRED).

- `lazy` | files=2 | mentions=13 | `adapter.py`, `config.py`
- `own` | files=2 | mentions=13 | `adapter.py`, `config.py`
- `adapter` | files=2 | mentions=10 | `adapter.py`, `config.py`
- `mcp` | files=2 | mentions=9 | `adapter.py`, `config.py`
- `open` | files=2 | mentions=7 | `adapter.py`, `config.py`
- `app` | files=2 | mentions=4 | `adapter.py`, `app.py`
- `config` | files=2 | mentions=4 | `adapter.py`, `config.py`
- `dir` | files=2 | mentions=4 | `adapter.py`, `config.py`
- `all` | files=2 | mentions=3 | `adapter.py`, `config.py`
- `code` | files=2 | mentions=3 | `adapter.py`, `config.py`
- `configuration` | files=2 | mentions=2 | `adapter.py`, `config.py`

## Verb Edges

- `adapter` --depends_on--> `all` (strength 1.00)
- `adapter` --depends_on--> `code` (strength 1.00)
- `adapter` --depends_on--> `config` (strength 1.00)
- `adapter` --depends_on--> `configuration` (strength 1.00)
- `adapter` --depends_on--> `dir` (strength 1.00)
- `adapter` --depends_on--> `lazy` (strength 1.00)
- `adapter` --depends_on--> `mcp` (strength 1.00)
- `adapter` --depends_on--> `open` (strength 1.00)
- `adapter` --depends_on--> `own` (strength 1.00)
- `all` --depends_on--> `adapter` (strength 1.00)
- `all` --depends_on--> `code` (strength 1.00)
- `all` --depends_on--> `config` (strength 1.00)
- `all` --depends_on--> `configuration` (strength 1.00)
- `all` --depends_on--> `dir` (strength 1.00)
- `all` --depends_on--> `lazy` (strength 1.00)
- `all` --depends_on--> `mcp` (strength 1.00)
- `all` --depends_on--> `open` (strength 1.00)
- `all` --depends_on--> `own` (strength 1.00)
- `app` --depends_on--> `adapter` (strength 1.00)
- `app` --depends_on--> `all` (strength 1.00)
- `app` --depends_on--> `code` (strength 1.00)
- `app` --depends_on--> `config` (strength 1.00)
- `app` --depends_on--> `configuration` (strength 1.00)
- `app` --depends_on--> `dir` (strength 1.00)
- `app` --depends_on--> `lazy` (strength 1.00)
- `app` --depends_on--> `mcp` (strength 1.00)
- `app` --depends_on--> `open` (strength 1.00)
- `app` --depends_on--> `own` (strength 1.00)
- `code` --depends_on--> `adapter` (strength 1.00)
- `code` --depends_on--> `all` (strength 1.00)
- `code` --depends_on--> `config` (strength 1.00)
- `code` --depends_on--> `configuration` (strength 1.00)
- `code` --depends_on--> `dir` (strength 1.00)
- `code` --depends_on--> `lazy` (strength 1.00)
- `code` --depends_on--> `mcp` (strength 1.00)
- `code` --depends_on--> `open` (strength 1.00)
- `code` --depends_on--> `own` (strength 1.00)
- `config` --depends_on--> `adapter` (strength 1.00)
- `config` --depends_on--> `all` (strength 1.00)
- `config` --depends_on--> `code` (strength 1.00)
- `config` --depends_on--> `configuration` (strength 1.00)
- `config` --depends_on--> `dir` (strength 1.00)
- `config` --depends_on--> `lazy` (strength 1.00)
- `config` --depends_on--> `mcp` (strength 1.00)
- `config` --depends_on--> `open` (strength 1.00)
- `config` --depends_on--> `own` (strength 1.00)
- `configuration` --depends_on--> `adapter` (strength 1.00)
- `configuration` --depends_on--> `all` (strength 1.00)
- `configuration` --depends_on--> `code` (strength 1.00)
- `configuration` --depends_on--> `config` (strength 1.00)

## Dialectic

- Thesis: `adapter` centralizes 2 files; Antithesis: `all` pulls 2 files with 2 shared (Jaccard 1.00); Synthesis: should they merge, split by layer, or keep `depends_on` explicit?
- Thesis: `adapter` centralizes 2 files; Antithesis: `code` pulls 2 files with 2 shared (Jaccard 1.00); Synthesis: should they merge, split by layer, or keep `depends_on` explicit?
- Thesis: `adapter` centralizes 2 files; Antithesis: `config` pulls 2 files with 2 shared (Jaccard 1.00); Synthesis: should they merge, split by layer, or keep `depends_on` explicit?
- Thesis: `adapter` centralizes 2 files; Antithesis: `configuration` pulls 2 files with 2 shared (Jaccard 1.00); Synthesis: should they merge, split by layer, or keep `depends_on` explicit?
- Thesis: `adapter` centralizes 2 files; Antithesis: `dir` pulls 2 files with 2 shared (Jaccard 1.00); Synthesis: should they merge, split by layer, or keep `depends_on` explicit?
- Thesis: `adapter` centralizes 2 files; Antithesis: `lazy` pulls 2 files with 2 shared (Jaccard 1.00); Synthesis: should they merge, split by layer, or keep `depends_on` explicit?
- Thesis: `adapter` centralizes 2 files; Antithesis: `mcp` pulls 2 files with 2 shared (Jaccard 1.00); Synthesis: should they merge, split by layer, or keep `depends_on` explicit?
- Thesis: `adapter` centralizes 2 files; Antithesis: `open` pulls 2 files with 2 shared (Jaccard 1.00); Synthesis: should they merge, split by layer, or keep `depends_on` explicit?
- Thesis: `adapter` centralizes 2 files; Antithesis: `own` pulls 2 files with 2 shared (Jaccard 1.00); Synthesis: should they merge, split by layer, or keep `depends_on` explicit?
- Thesis: `all` centralizes 2 files; Antithesis: `code` pulls 2 files with 2 shared (Jaccard 1.00); Synthesis: should they merge, split by layer, or keep `depends_on` explicit?
