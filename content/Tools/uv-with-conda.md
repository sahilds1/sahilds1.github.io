Title: TIL: Integrating  `uv`  with Conda using  `uv`'s pip interface
Date: 2025-02-24
Tags: python
Summary: Today I Learned: Small tools and facts I've learned
Status: published

`uv` has a [pip interface](https://docs.astral.sh/uv/getting-started/features/#the-pip-interface) that you can use to still manage virtual environments with `conda`:


Install `uv` inside your conda environment and then use it just like pip

```
pip install uv
uv pip install requests numpy pandas
```