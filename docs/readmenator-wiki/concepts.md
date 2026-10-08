# Concepts

Second-brain semantic layer: nouns map atomically to file sets (EXTRACTED); verbs aggregate structural edges (INFERRED).

| Concept | Files | Mentions | Top Files |
|---------|-------|----------|-----------|
| `lazy` | 2 | 13 | `adapter.py`, `config.py` |
| `own` | 2 | 13 | `adapter.py`, `config.py` |
| `adapter` | 2 | 10 | `adapter.py`, `config.py` |
| `mcp` | 2 | 9 | `adapter.py`, `config.py` |
| `open` | 2 | 7 | `adapter.py`, `config.py` |
| `app` | 2 | 4 | `adapter.py`, `app.py` |
| `config` | 2 | 4 | `adapter.py`, `config.py` |
| `dir` | 2 | 4 | `adapter.py`, `config.py` |
| `all` | 2 | 3 | `adapter.py`, `config.py` |
| `code` | 2 | 3 | `adapter.py`, `config.py` |
| `configuration` | 2 | 2 | `adapter.py`, `config.py` |

## Verb Edges

| Source | Verb | Target | Strength |
|--------|------|--------|----------|
| `adapter` | `depends_on` | `all` | 1.00 |
| `adapter` | `depends_on` | `code` | 1.00 |
| `adapter` | `depends_on` | `config` | 1.00 |
| `adapter` | `depends_on` | `configuration` | 1.00 |
| `adapter` | `depends_on` | `dir` | 1.00 |
| `adapter` | `depends_on` | `lazy` | 1.00 |
| `adapter` | `depends_on` | `mcp` | 1.00 |
| `adapter` | `depends_on` | `open` | 1.00 |
| `adapter` | `depends_on` | `own` | 1.00 |
| `all` | `depends_on` | `adapter` | 1.00 |
| `all` | `depends_on` | `code` | 1.00 |
| `all` | `depends_on` | `config` | 1.00 |
| `all` | `depends_on` | `configuration` | 1.00 |
| `all` | `depends_on` | `dir` | 1.00 |
| `all` | `depends_on` | `lazy` | 1.00 |
| `all` | `depends_on` | `mcp` | 1.00 |
| `all` | `depends_on` | `open` | 1.00 |
| `all` | `depends_on` | `own` | 1.00 |
| `app` | `depends_on` | `adapter` | 1.00 |
| `app` | `depends_on` | `all` | 1.00 |
| `app` | `depends_on` | `code` | 1.00 |
| `app` | `depends_on` | `config` | 1.00 |
| `app` | `depends_on` | `configuration` | 1.00 |
| `app` | `depends_on` | `dir` | 1.00 |
| `app` | `depends_on` | `lazy` | 1.00 |
| `app` | `depends_on` | `mcp` | 1.00 |
| `app` | `depends_on` | `open` | 1.00 |
| `app` | `depends_on` | `own` | 1.00 |
| `code` | `depends_on` | `adapter` | 1.00 |
| `code` | `depends_on` | `all` | 1.00 |
| `code` | `depends_on` | `config` | 1.00 |
| `code` | `depends_on` | `configuration` | 1.00 |
| `code` | `depends_on` | `dir` | 1.00 |
| `code` | `depends_on` | `lazy` | 1.00 |
| `code` | `depends_on` | `mcp` | 1.00 |
| `code` | `depends_on` | `open` | 1.00 |
| `code` | `depends_on` | `own` | 1.00 |
| `config` | `depends_on` | `adapter` | 1.00 |
| `config` | `depends_on` | `all` | 1.00 |
| `config` | `depends_on` | `code` | 1.00 |
| `config` | `depends_on` | `configuration` | 1.00 |
| `config` | `depends_on` | `dir` | 1.00 |
| `config` | `depends_on` | `lazy` | 1.00 |
| `config` | `depends_on` | `mcp` | 1.00 |
| `config` | `depends_on` | `open` | 1.00 |
| `config` | `depends_on` | `own` | 1.00 |
| `configuration` | `depends_on` | `adapter` | 1.00 |
| `configuration` | `depends_on` | `all` | 1.00 |
| `configuration` | `depends_on` | `code` | 1.00 |
| `configuration` | `depends_on` | `config` | 1.00 |

## Dialectic Prompts

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
