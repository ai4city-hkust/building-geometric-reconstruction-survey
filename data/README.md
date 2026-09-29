# Reference Catalog

`references.json` contains all 109 bibliography entries. IDs `R001` through `R109` preserve the order of the source PDF. Each entry includes a reading collection, the original citation, and the PDF page on which the reference starts.

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
