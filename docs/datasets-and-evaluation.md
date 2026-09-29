# Datasets and Evaluation

[Home](../README.md) · [Section summaries](section-summaries.md#s5) · [Paper library](../PAPERS.md)

## Dataset Map

The resources below are named in Section 5 or in the related roof-reconstruction discussion. A dataset may support a pipeline component without supplying every annotation needed for end-to-end geometric reconstruction. Paper links point directly to official publication pages or repositories.

| Resource | Primary role in the survey | Relevant annotations or evidence | Related paper entries |
| :--- | :--- | :--- | :--- |
| **CrowdAI** | Footprint extraction | Overhead images and building polygons | [RoIPoly](https://linkinghub.elsevier.com/retrieve/pii/S0924271625001364), [PolyBuilding](https://linkinghub.elsevier.com/retrieve/pii/S0924271623000813) |
| **WHU Building Dataset** | Building extraction and vectorization | Building masks / footprints, depending on subset and preparation | [VectorLLM](https://linkinghub.elsevier.com/retrieve/pii/S0924271626000250), [CNN review](https://www.dqxxkx.cn/EN/10.12082/dqxxkx.2024.240057) |
| **Inria Aerial Image Labeling** | Building segmentation and derived vectorization | Aerial images and building labels | [PolyR-CNN](https://linkinghub.elsevier.com/retrieve/pii/S0924271624003824) |
| **SpaceNet** | Overhead mapping and source imagery for derived structure benchmarks | Satellite imagery and release-specific mapping annotations | [Conv-MPN](https://ieeexplore.ieee.org/document/9156819/), [HEAT](https://ieeexplore.ieee.org/document/9878511/) |
| **Deventer-512** | Multiclass polygonal mapping | Land-cover polygons and shared-boundary topology | [ACPV-Net](https://openaccess.thecvf.com/content/CVPR2026/html/Jiao_ACPV-Net_All-Class_Polygonal_Vectorization_for_Seamless_Vector_Map_Generation_from_CVPR_2026_paper.html) |
| **VWB** | Roof graph reconstruction | Junctions, edges, and planar structural relationships | [Vectorizing World Buildings](https://link.springer.com/chapter/10.1007/978-3-030-58598-3_42) |
| **Enschede** | Fine-grained roof topology | Aerial imagery and roof structure graphs | [RSGNN](https://linkinghub.elsevier.com/retrieve/pii/S092427162200065X) |
| **BuildingWF** | Synthetic 3D building wireframe learning | Rendered multi-view images and ground-truth 3D wireframes for reconstruction from 3D line clouds | [Luo et al.](https://arxiv.org/abs/2208.11948) |
| **Roof3D** | Roof-plane and building-section learning | RGB / DSM inputs with roof plane and section labels | [Roof3D](https://isprs-annals.copernicus.org/articles/X-1-W1-2023/971/2023/) |
| **Boston / BONAI** | Off-nadir building geometry | Roof / footprint correspondence and height-related annotations | [DG-BRF](https://linkinghub.elsevier.com/retrieve/pii/S0924271625004563) |
| **BuildingWorld** | Diverse structured 3D reconstruction | Building models and real / simulated LiDAR | [BuildingWorld](https://ojs.aaai.org/index.php/AAAI/article/view/37422) |
| **Building3D** | Roof structure reconstruction from points | Point clouds, meshes, and wireframes | [Building3D](https://ieeexplore.ieee.org/document/10376547/) |
| **Map2ImLas** | Multimodal scene understanding | Aligned aerial imagery, LiDAR, and semantic labels | [Map2ImLas](https://linkinghub.elsevier.com/retrieve/pii/S2667393225000316) |
| **City-BIS** | Building instance segmentation before reconstruction | Instance-level labels for LiDAR point clouds | [Li et al.](https://linkinghub.elsevier.com/retrieve/pii/S1569843226000026) |
| **Structured3D** | Synthetic structured scene modeling | Junctions, lines, planes, and other structural primitives | [Structured3D](https://link.springer.com/chapter/10.1007/978-3-030-58545-7_30) |

Dataset sizes and annotation formats vary by release and preprocessing. In particular, annotations in roof-graph derivatives should not be assumed to exist in every original SpaceNet release; semantic labels in Map2ImLas or City-BIS should not be treated as watertight mesh ground truth.

## Annotation Scope

- **Masks versus polygons:** WHU and Inria segmentation labels may require vectorization or instance preparation. A paper's derived polygon benchmark is not automatically the original dataset format.
- **Roof graphs versus roof surfaces:** VWB and Enschede emphasize image-plane structural relationships. Metric roof reconstruction additionally needs elevation. BuildingWF is discussed alongside these resources in the manuscript, but its cited source provides 3D building wireframes and multi-view observations.
- **Single-building versus all-class maps:** Deventer-512 includes multiple land-cover classes. Its total polygon count must not be described as a count of building instances alone.
- **Off-nadir geometry:** Boston and the refined BONAI annotations support roof/footprint correspondence and height-related learning. They are distinct resources; a combined row does not establish identical image counts, splits, or annotations.
- **Supporting tasks versus final reconstruction:** Map2ImLas supports aligned 2D/3D semantics, City-BIS supports building instances, and Structured3D supplies synthetic scene structure. The required outputs and acquisition domains must be checked before treating them as interchangeable building-mesh benchmarks.

## Metric Map

| Evaluation level | Measures discussed in the survey | What they tell you | What they do not establish alone |
| :--- | :--- | :--- | :--- |
| Region / instance | IoU, AP / AR, FCSP, AFI | Coverage, instance detection, and region agreement | Sharp corners or valid polygon topology |
| Boundary / polygon | PoLiS, boundary AP | Boundary displacement and localization quality | Correct 3D roof height |
| Regularity / complexity | Maximum tangent angle error, vertex redundancy, complexity-aware IoU | Shape regularity and representation economy | Whether simplification removed meaningful structure |
| Line evidence | Number of False Alarms (NFA) | Statistical support for detected line features | Complete building structure |
| Wireframe | Corner / edge precision, recall, F1, structural overlap measures | Recovery of primitives and connectivity under a matching protocol | Watertightness or complete surface geometry |
| 3D geometry / height | RMSE, height-threshold coverage, distance measures | Agreement with reference geometry or elevation | Topological validity |
| Structural relationships | Graph / adjacency consistency and geometric integrity | Preservation of meaningful structural relationships | Accuracy of every surface point |

## Metric Definitions and Protocols

**Region and instance agreement.** IoU measures overlap relative to union. FCSP and AFI describe coverage or area agreement under the source's segmentation convention; area agreement alone can conceal misplaced boundaries. Precision `TP / (TP + FP)` and recall `TP / (TP + FN)` at one operating point are **not AP and AR**. COCO-style AP aggregates interpolated precision over recall levels and IoU thresholds; AR aggregates achieved recall under specified IoU thresholds and detection limits. Report AP50 separately from AP averaged over thresholds. See the [official COCO evaluator](https://github.com/cocodataset/cocoapi/blob/master/PythonAPI/pycocotools/cocoeval.py).

**Polygon boundaries and complexity.** PoLiS measures symmetric vertex-to-boundary discrepancy. Boundary AP changes the matching criterion to boundary agreement. Maximum tangent-angle error assesses orientation mismatch; vertex-count ratios and complexity-aware IoU quantify aspects of representation economy. These depend on the reference geometry, tolerance, and sampling convention. A low vertex count is not beneficial if it erases real corners or roof features.

**Lines and wireframes.** NFA evaluates statistical evidence for a line under an a-contrario null model; it is not an overall reconstruction-accuracy score. Corner/edge precision, recall, and F1 require an explicit matching rule and spatial tolerance. Structural IoU (`sIoU`) is representation- and protocol-specific. Approximate geometric matches, rather than literal equality of floating-point edge coordinates, determine true positives.

**Heights and surfaces.** Height RMSE summarizes squared differences over matched height samples; surface-distance RMSE answers a different question and must be identified as such. The manuscript's `e_0.5` measures building-area coverage with absolute height error below 0.5 m. Chamfer and Hausdorff distances also occur in the method comparisons, but depend on sampling, normalization, directionality, and units. They do not by themselves certify watertightness or connectivity.

**Structural relationships.** Extended Attribute Adjacency Graphs (EAAG) encode relationships among geometric components for abstraction and simplification. Writing `G = (F, E, A)` defines a graph representation, not a complete numerical metric. A reproducible evaluation must state how retained or violated relationships are scored.

## Reading Reported Results

The comparison tables in the survey combine results reported by different studies. They are a map of method characteristics, not a controlled benchmark.

When interpreting a result, keep the following conditions together:

1. **Output:** mask, polygon, roof graph, wireframe, surface, or closed mesh.
2. **Input:** image count, resolution, DSM availability, point density, and occlusion.
3. **Data:** geographic domain, split, annotation convention, and preprocessing.
4. **Protocol:** metric definition, matching tolerance, units, and aggregation.
5. **Practical cost:** runtime, memory, manual intervention, and post-processing.

AP summarizes a precision-recall evaluation protocol; it is not simply the ratio TP / (TP + FP). Likewise, edge accuracy and region overlap cannot replace explicit checks of polygon or mesh validity.

## Output-Specific Checks

The following checklist translates the survey's geometric and topological concerns into practical evaluation questions; it is not a new benchmark claimed by the manuscript.

| Output | Checks beyond aggregate accuracy |
| :--- | :--- |
| Footprint polygon | Closed boundary, self-intersections, duplicate vertices, holes where annotated, and correct instance separation |
| Roof graph or surface | Junction-edge incidence, missing or spurious connections, roof-plane adjacency, and reliable elevations |
| Building mesh | Surface closure where required, manifoldness, self-intersections, facade coverage, and consistency with observed points |
| Generated or updated model | Separation of observed and inferred geometry, uncertainty, temporal alignment, and repeatability |
