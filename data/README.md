# Reference Catalog

`references.json` contains 110 bibliography entries. IDs `R001` through `R109` preserve the order of the source PDF; later additions are appended without renumbering existing entries. Each entry includes a reading collection and source citation. PDF page numbers are recorded when available.

`R110` is Xu et al. (2025), supplied by the maintainer with the BibTeX key `xu2025pose`. It is cited in Section 1 (Introduction), in the second sentence of the opening paragraph, alongside `li2024review` and `11417956`. Its publication metadata and citation location are retained in the catalog; `source_page` is `null` because no updated PDF page number was supplied.

`paper-links.json` maps every reference ID to a verified official paper URL. Prefer a publisher or conference page; use the official preprint or university repository when appropriate. For example:

```json
{
  "R001": "https://www.tandfonline.com/doi/full/10.1080/17538947.2025.2458682",
  "R002": "https://www.mdpi.com/2072-4292/11/19/2219"
}
```

Keep all IDs in the actual manifest. Regenerate the library from the repository root with:

```powershell
python tools/build_library.py
python tools/render_preview.py
```

The generator requires a nonempty HTTP(S) URL for every reference and renders it as an official source, not a guaranteed PDF download. `link-verification.json` records the matching metadata, verification date, and supporting official source or DOI record. If a URL changes, update both files and any corresponding links in the overview or reading guides before regenerating the preview.

All 110 paper links were checked on 2026-09-29. Some sources restrict automated access or require a subscription; matching publisher metadata does not imply that the full text is freely available.
