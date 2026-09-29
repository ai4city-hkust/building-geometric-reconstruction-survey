# Editorial Notes and Manuscript Cross-Check

[Home](../README.md)

These notes record editorial decisions and the cross-check against the maintainer-supplied LaTeX on 29 September 2026. They are separate from the scientific section summaries.

## Review Scope

The active LaTeX body and comparison tables are the reference for the current summaries; commented-out draft paragraphs and tables are excluded. Earlier PDF page ranges have been removed from the reading guide because a revised LaTeX source does not establish the same pagination. The repository remains a section-by-section companion, not a reproduction of the full manuscript or its experimental tables.

| Manuscript section | Coverage checked and updated |
| :--- | :--- |
| 1. Introduction | Application motivation, output/modality taxonomy, literature search and selection, and recurring challenges |
| 2. 2D outlines | Segmentation, all four vector-generation families, LiDAR tracing, feature fusion, and comparisons |
| 3. 2.5D roofs | Primitive parsing, planes/heights, model-driven and bottom-up LiDAR methods, actual inputs and outputs |
| 4. 3D buildings | MVS abstraction, single-image inference, generative inputs, primitive assembly, learned representations, and fusion |
| 5. Datasets and evaluation | All named dataset resources, native versus derived annotations, metric meaning, and comparison protocols |
| 6. Outlook | Boundary/topology challenges, annotation, agents, diffusion, NeRF/3DGS, VLMs/LLMs, fusion, semantics, and temporal monitoring |
| 7. Conclusion | Methodological progression, remaining limitations, and future prospects distinguished from demonstrated capabilities |

Primary sources were consulted for identified ambiguities, notably KIPPI, Sat2City, BuildingWF, and COCO evaluation. This is not an independent replication of every reviewed experiment. No new benchmark results or performance ranking have been inferred from heterogeneous tables.

## Publication Metadata

The PE&RS journal attribution was supplied by the maintainer. No confirmed final publication year, volume, issue, page range, or DOI has been supplied. Those fields remain unset. The README's Publication and Citation section intentionally remains empty, and no final bibliographic record for the survey has been invented.

## Official Paper Links

At the maintainer's request, all 110 entries now link to official paper sources rather than pending maintainer-uploaded PDFs. Publisher-deposited DOI metadata and official conference, journal, preprint, or university records were checked for the matching title, authors, and year. Links and verification sources are retained in `data/paper-links.json` and `data/link-verification.json`. No search-result pages or third-party paper mirrors are used.

These are paper links, not promises of free full-text downloads. Some publisher pages require a subscription, institutional access, or an interactive browser check. The 1987 Marching Cubes paper and the 1998 reprint have separate ACM records and distinct links.

## Bibliography Coverage

All 109 entries in the supplied PDF's bibliography are retained, in stable source order through IDs R001-R109. The reading collections are editorial groupings, not claims that a reference occurs exclusively in one section. The original citation text remains available in `data/references.json`.

The catalog now contains 110 entries. R110, Xu et al. (2025), was added from the maintainer's BibTeX under the key `xu2025pose`. The supplied LaTeX confirms that it is cited only in the Introduction, in the opening paragraph's second sentence. It remains in Background and Related Surveys rather than 3D Building Models, without an added citation paragraph in the summaries. Its volume (225), page range (461-491), and publisher (Elsevier) follow the supplied record and match the publisher's article record.

The pasted LaTeX calls `references.bib` but does not include that file's entries. The existing 110 catalog records and their official links are retained. This body-text review does not establish that every current BibTeX key resolves or that the unseen bibliography has no additions, deletions, or changed metadata.

Titles use matched bibliographic metadata where a title/author/year match was available; other titles are transcribed and lightly normalized. Year suffixes such as 2024a follow the source and are not separate publication years.

## Source Details to Recheck

- **KIPPI (R005), Section 4.2.1 and the LiDAR comparison table:** the cited [2018 paper](https://openaccess.thecvf.com/content_cvpr_2018/papers/Bauchet_KIPPI_KInetic_Polygonal_CVPR_2018_paper.pdf) partitions images using line segments; it does not support the attributed 3D watertight-surface pipeline. The guide preserves the reference but does not repeat that claim. The manuscript needs either the intended 3D reference or a corrected description.
- **Sat2City (R029), Section 4.1.2:** the narrative says single satellite image, while the comparison table identifies a height-field condition. The [original paper's inference pipeline](https://openaccess.thecvf.com/content/ICCV2025/papers/Hua_Sat2City_3D_City_Generation_from_A_Single_Satellite_Image_with_ICCV_2025_paper.pdf) conditions on a height-field representation and evaluates on synthetic city data. The summary makes that input explicit and separates generation from observation-faithful reconstruction.
- **BuildingWF (R055), Section 5.1 and the dataset table:** the source places it among 2.5D roof resources, but the [cited study](https://arxiv.org/abs/2208.11948) supplies synthetic multi-view imagery with ground-truth 3D building wireframes for line-cloud reconstruction. The repository describes the actual annotation dimension instead of implying only planar roof graphs.
- **Loops2Roofs (R023), Section 4.2:** the prose introduces it under primitive assembly, but the table lists it among learned methods with structural conditions. The guide places it with generative roof-loop methods and does not imply that it performs deterministic fitting directly to raw LiDAR.
- **AP / AR, metric table `tab:geom_metrics`:** the displayed TP ratios are precision and recall, not averaged AP/AR. The guide uses the [official COCO evaluation protocol](https://github.com/cocodataset/cocoapi/blob/master/PythonAPI/pycocotools/cocoeval.py). Height RMSE, surface distance, edge matching, and EAAG relationship assessment also need explicit protocols rather than schematic notation alone.
- **Citation placeholders in Section 5.2:** the active source contains literal `[41]`, `[5, 24]`, and `[cite: 3882, 3960, 4151]`. These should be resolved to the intended BibTeX keys; they are not copied into the repository. The last form appears to be an unresolved editing artifact, not a valid scholarly reference.
- **Literature-selection reproducibility, Introduction:** the source now specifies search services, an approximate date range, search topics, and inclusion/exclusion criteria. It does not provide a reproducible search log or screening counts. The repository summarizes the stated process without labeling it a fully documented systematic-review protocol.

## Earlier PDF Notes

The following observations concern the earlier PDF and cannot be assumed resolved by a LaTeX body supplied without its bibliography or figure files:

- **Marching Cubes (R054 and R082):** the bibliography lists both the 1998 reprint and a malformed 1987 record headed "WE, L.". Both source entries are retained. The latter should be corrected against the original publication before a final bibliography release.
- **Figure 4:** "Chen et al. (2024)" appears in the taxonomy, while the corresponding discussion and bibliography identify the multiscale grid study as Chen et al. (2014), R012.
- **Datasets:** roof-graph derivatives are distinguished from original dataset releases, and semantic or instance-segmentation datasets are distinguished from mesh-reconstruction benchmarks.

The summaries also avoid turning heterogeneous reported performance values into a leaderboard or treating generated geometry as automatically faithful to the observed building.
