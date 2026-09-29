# Preview Editorial Notes

[Home](../README.md)

These notes record decisions for this private preview. They are separate from the scientific section summaries.

## Publication Metadata

The PE&RS journal attribution was supplied by the maintainer. The PDF does not provide a final publication year, volume, issue, page range, or DOI. Those fields remain unset. No final bibliographic record for the survey has been invented.

## Download Links

The maintainer has already downloaded the reviewed papers and will upload them separately. Every entry in the download-link manifest therefore starts empty. No DOI, publisher URL, inferred file path, or search result is used as a substitute download link.

## Bibliography Coverage

All 109 entries in the supplied PDF's bibliography are retained, in stable source order through IDs R001-R109. The reading collections are editorial groupings, not claims that a reference occurs exclusively in one section. The original citation text remains available in `data/references.json`.

The catalog now contains 110 entries. R110, Xu et al. (2025), was added from the maintainer's BibTeX and revised Introduction excerpt under the key `xu2025pose`. It is cited in the opening paragraph's second sentence and grouped under 3D Building Models for reading. Its volume (225), page range (461-491), and publisher (Elsevier) follow the supplied record; no updated source PDF page or download address was supplied.

Titles use matched bibliographic metadata where a title/author/year match was available; other titles are transcribed and lightly normalized. Year suffixes such as 2024a follow the source and are not separate publication years.

## Source Details to Recheck

- **KIPPI (R005):** the cited 2018 title concerns image partitioning, while parts of the manuscript discuss it as a 3D surface-reconstruction method. The summary avoids that unsupported attribution.
- **Marching Cubes (R054 and R082):** the bibliography lists both the 1998 reprint and a malformed 1987 record headed "WE, L.". Both source entries are retained. The latter should be corrected against the original publication before a final bibliography release.
- **Figure 4:** "Chen et al. (2024)" appears in the taxonomy, while the corresponding discussion and bibliography identify the multiscale grid study as Chen et al. (2014), R012.
- **Table 10:** the displayed TP / (TP + FP) and TP / (TP + FN) expressions describe precision and recall, not full AP / AR protocols. The guide describes metric purposes instead of reproducing these expressions.
- **Datasets:** roof-graph derivatives are distinguished from original dataset releases, and semantic or instance-segmentation datasets are distinguished from mesh-reconstruction benchmarks.

The summaries also avoid turning heterogeneous reported performance values into a leaderboard or treating generated geometry as automatically faithful to the observed building.
