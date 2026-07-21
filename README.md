# CourseFuzz Demo Target

This public repository is the dedicated, non-production destination for CourseFuzz's verified
autograder-repair demonstration. It contains a correct triangle reference and the instructor's
original test suite. CourseFuzz may create run-specific branches and draft pull requests that add
one execution-backed regression under `tests/coursefuzz/`.

The product repository is deliberately not used as a write target. No student data, credentials,
or real course material belongs here.

Run the suite with:

```bash
python -m pip install pytest
python -m pytest
```
