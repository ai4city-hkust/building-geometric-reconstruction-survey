# Datasets and Evaluation

[Home](../README.md) · [Section summaries](section-summaries.md#s5) · [Paper library](../PAPERS.md)

## Dataset Map

The resources below are named in Section 5 or in the related roof-reconstruction discussion. A dataset may support a pipeline component without supplying every annotation needed for end-to-end geometric reconstruction. Paper links point to entries in this repository; maintainer-provided downloads are pending.

| Resource | Primary role in the survey | Relevant annotations or evidence | Related paper entries |
| :--- | :--- | :--- | :--- |
| **CrowdAI** | Footprint extraction | Overhead images and building polygons | [RoIPoly](../PAPERS.md#r034), [PolyBuilding](../PAPERS.md#r026) |
| **WHU Building Dataset** | Building extraction and vectorization | Building masks / footprints, depending on subset and preparation | [VectorLLM](../PAPERS.md#r098), [CNN review](../PAPERS.md#r091) |
| **Inria Aerial Image Labeling** | Building segmentation and derived vectorization | Aerial images and building labels | [PolyR-CNN](../PAPERS.md#r036) |
| **SpaceNet** | Overhead mapping and source imagery for derived structure benchmarks | Satellite imagery and release-specific mapping annotations | [Conv-MPN](../PAPERS.md#r096), [HEAT](../PAPERS.md#r011) |
| **Deventer-512** | Multiclass polygonal mapping | Land-cover polygons and shared-boundary topology | [ACPV-Net](../PAPERS.md#r035) |
| **VWB** | Roof graph reconstruction | Junctions, edges, and planar structural relationships | [Vectorizing World Buildings](../PAPERS.md#r064) |
| **Enschede** | Fine-grained roof topology | Aerial imagery and roof structure graphs | [RSGNN](../PAPERS.md#r102) |
| **BuildingWF** | Synthetic wireframe learning | Building models, rendered observations, and structural graphs | [Luo et al.](../PAPERS.md#r055) |
| **Roof3D** | Roof-plane and building-section learning | RGB / DSM inputs with roof plane and section labels | [Roof3D](../PAPERS.md#r069) |
| **Boston / BONAI** | Off-nadir building geometry | Roof / footprint correspondence and height-related annotations | [DG-BRF](../PAPERS.md#r027) |
| **BuildingWorld** | Diverse structured 3D reconstruction | Building models and real / simulated LiDAR | [BuildingWorld](../PAPERS.md#r033) |
| **Building3D** | Roof structure reconstruction from points | Point clouds, meshes, and wireframes | [Building3D](../PAPERS.md#r076) |
| **Map2ImLas** | Multimodal scene understanding | Aligned aerial imagery, LiDAR, and semantic labels | [Map2ImLas](../PAPERS.md#r003) |
| **City-BIS** | Building instance segmentation before reconstruction | Instance-level labels for LiDAR point clouds | [Li et al.](../PAPERS.md#r041) |
| **Structured3D** | Synthetic structured scene modeling | Junctions, lines, planes, and other structural primitives | [Structured3D](../PAPERS.md#r103) |

Dataset sizes and annotation formats vary by release and preprocessing. In particular, annotations in roof-graph derivatives should not be assumed to exist in every original SpaceNet release; semantic labels in Map2ImLas or City-BIS should not be treated as watertight mesh ground truth.

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

## Reading Reported Results

The comparison tables in the survey combine results reported by different studies. They are a map of method characteristics, not a controlled benchmark.

When interpreting a result, keep the following conditions together:

1. **Output:** mask, polygon, roof graph, wireframe, surface, or closed mesh.
2. **Input:** image count, resolution, DSM availability, point density, and occlusion.
3. **Data:** geographic domain, split, annotation convention, and preprocessing.
4. **Protocol:** metric definition, matching tolerance, units, and aggregation.
5. **Practical cost:** runtime, memory, manual intervention, and post-processing.

AP summarizes a precision-recall evaluation protocol; it is not simply the ratio TP / (TP + FP). Likewise, edge accuracy and region overlap cannot replace explicit checks of polygon or mesh validity.
