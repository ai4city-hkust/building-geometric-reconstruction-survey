# Reference Catalog

`references.json` contains 110 bibliography entries. IDs `R001` through `R109` preserve the order of the source PDF; later additions are appended without renumbering existing entries. Each entry includes a reading collection and source citation. PDF page numbers are recorded when available.

`R110` is Xu et al. (2025), supplied by the maintainer with the BibTeX key `xu2025pose`. It is cited in Section 1 (Introduction), in the second sentence of the opening paragraph, alongside `li2024review` and `11417956`. Its publication metadata and citation location are retained in the catalog; `source_page` is `null` because no updated PDF page number was supplied.

`download-links.json` is the only source of download addresses. Every value is initially empty. When the maintainer supplies an uploaded-paper link, assign it to the matching reference ID, for example:

```json
{
  "R001": "",
  "R002": ""
}
```

Keep all IDs in the actual manifest. Regenerate the library from the repository root with:

```powershell
python tools/build_library.py
```

The generator never infers a download URL from a paper title, DOI, or publisher record. Empty values render as `Pending`. The manifest is the single source of download links.
