<div align="center">

# Automatic Geometric Structure Reconstruction of Buildings from Remote Sensing Data

### A Comprehensive Survey

**Wufan Zhao · Tengxi Wang · Shuai Zhang · Tongyan Hua · Zhuoxiao Li · Claudio Persello · Rongjun Qin**

*Photogrammetric Engineering & Remote Sensing (PE&RS)*

**2D footprints &nbsp; / &nbsp; 2.5D roofs &nbsp; / &nbsp; 3D buildings**

[Overview](#overview) &nbsp; · &nbsp; [Section Summaries](docs/section-summaries.md) &nbsp; · &nbsp; [Paper Library](PAPERS.md) &nbsp; · &nbsp; [Datasets & Evaluation](docs/datasets-and-evaluation.md)

</div>

<p align="center">
  <img src="assets/survey-framework.png" alt="Survey framework connecting remote sensing data, reconstruction methods, 2D footprints, 2.5D roofs, 3D models, and future research directions" width="100%">
</p>

<p align="center"><sub>Figure 1 from the survey. From remote sensing observations to structured building geometry.</sub></p>

> **Central question:** How can remote sensing observations be converted into building models that are geometrically accurate, topologically consistent, and compact enough to use?

## Overview

Buildings are more than foreground pixels. Urban mapping, simulation, and digital twins require explicit boundaries, connected roof structures, and usable 3D geometry. This survey examines the transition from raster segmentation and handcrafted fitting to direct vector prediction, graph reasoning, and generative reconstruction.

The literature is organized along two complementary axes: **the geometry to be reconstructed** and **the evidence provided by the sensor**. Across these axes, the recurring challenge is to balance measured detail, architectural regularity, and structural completeness.

| Geometry | What is reconstructed? | What makes it difficult? |
| :--- | :--- | :--- |
| **2D** | Closed footprint polygons with ordered corners and clean boundaries | Boundary localization, instance separation, and valid polygon topology |
| **2.5D** | Roof facets, ridges, junctions, and elevation | Recovering both height and the relationships between roof planes |
| **3D** | Building wireframes, polyhedral surfaces, and meshes | Facade completion, surface closure, connectivity, and compactness |

**Reading map**

[1. Introduction](#1-introduction) · [2. 2D Outlines](#2-2d-building-outline-reconstruction) · [3. 2.5D Roofs](#3-25d-building-roof-reconstruction) · [4. 3D Models](#4-3d-building-model-and-wireframe-reconstruction) · [5. Datasets & Evaluation](#5-datasets-and-evaluation) · [6. Future Outlook](#6-discussion-and-future-outlook) · [7. Conclusion](#7-conclusion)

## 1. Introduction

The opening section motivates a shift from recognizing buildings to reconstructing their geometric structure. It defines the progression from planar outlines to roofs and full 3D models, and explains why an output-centered taxonomy is useful for urban applications.

Optical imagery contributes appearance and boundary cues; stereo imagery adds geometry through correspondence; LiDAR supplies direct spatial measurements. These differences determine where a method must rely on observation, regularization, or learned priors. The survey also positions model-driven, data-driven, and hybrid approaches within this common framework.

**Takeaway:** Select a reconstruction strategy by the required output and available geometric evidence, not by architecture alone.

[Detailed summary](docs/section-summaries.md#s1) · [Background literature](PAPERS.md#background)

## 2. 2D Building Outline Reconstruction

The objective is a clean, valid polygon for each building. Optical methods increasingly predict vertices and connectivity directly, while LiDAR methods recover continuous outlines from irregular point distributions.

| Route | Core idea | Representative studies |
| :--- | :--- | :--- |
| Segmentation and polygonization | Add directional or boundary supervision before vectorization | [Frame Field Learning](PAPERS.md#r021), [HiSup](PAPERS.md#r085) |
| Sequential prediction | Generate an ordered sequence of corners | [PolyMapper](PAPERS.md#r048), [Zhao et al., 2021](PAPERS.md#r101), [VectorLLM](PAPERS.md#r098) |
| Graphs and matching | Detect corners and infer their connections | [PolyWorld](PAPERS.md#r108), [Re:PolyWorld](PAPERS.md#r109), [ABCNet](PAPERS.md#r016) |
| RoI and query architectures | Predict and refine instance polygons in parallel | [PolyR-CNN](PAPERS.md#r036), [RoIPoly](PAPERS.md#r034), [PolyBuilding](PAPERS.md#r026) |
| LiDAR tracing and regularization | Trace projected points and enforce geometric consistency | [RMBR](PAPERS.md#r039), [GMDL](PAPERS.md#r037), [ATAS](PAPERS.md#r051) |

**Takeaway:** Good segmentation scores do not, by themselves, establish polygon quality. Sharp corners, sensible vertex counts, and correct connectivity must also be assessed.

<details>
<summary><strong>What each subsection covers</strong></summary>

- **2.1 Optical imagery:** segmentation-based methods; sequential, graph-based, query-based, and hybrid vector generation; their different failure modes.
- **2.2 LiDAR point clouds:** local tracing, global regularization, adaptive boundaries, and point/grid feature fusion.
- **2.3 Synthesis:** the trade-off between preserving observed boundary detail and enforcing architectural regularity.

</details>

[Detailed summary](docs/section-summaries.md#s2) · [2D paper collection](PAPERS.md#footprints)

## 3. 2.5D Building Roof Reconstruction

Roof reconstruction adds elevation and internal structure to the building outline. A useful representation must recover roof facets and their adjacency, including ridges, valleys, and height discontinuities.

| Route | Core idea | Representative studies |
| :--- | :--- | :--- |
| Image-based primitive parsing | Detect junctions and edges, then reason about roof graphs | [HEAT](PAPERS.md#r011), [Conv-MPN](PAPERS.md#r096), [RSGNN](PAPERS.md#r102), [Roof-Former](PAPERS.md#r100) |
| Plane and height inference | Infer plane parameters, roof sections, or height from imagery | [PlaneRCNN](PAPERS.md#r050), [Boundary-aware reconstruction](PAPERS.md#r060), [KIBS](PAPERS.md#r056) |
| Model-driven LiDAR reconstruction | Fit templates or discover shared geometric regularities | [RMBR](PAPERS.md#r039), [Global regularities](PAPERS.md#r105) |
| Data-driven LiDAR reconstruction | Assemble planes or learn roof vertices and edges | [Cycle graph analysis](PAPERS.md#r066), [Point2Roof](PAPERS.md#r042), [RR-Net](PAPERS.md#r086) |

**Takeaway:** A correct roof graph and an accurate roof surface are related but distinct achievements. Topology must be paired with reliable elevation.

<details>
<summary><strong>What each subsection covers</strong></summary>

- **3.1 Optical imagery:** primitive graphs, segmentation-guided vectorization, direct plane estimation, and learned height cues.
- **3.2 LiDAR point clouds:** top-down templates and global priors versus bottom-up plane extraction, graph assembly, and learned edge prediction.
- **3.3 Synthesis:** roof models need metric accuracy and structural consistency, particularly for complex roof configurations.

</details>

[Detailed summary](docs/section-summaries.md#s3) · [Roof paper collection](PAPERS.md#roofs)

## 4. 3D Building Model and Wireframe Reconstruction

Full 3D reconstruction must organize vertices, edges, and faces into a coherent building representation. The section compares image-derived geometry, directly measured point clouds, and their fusion, while distinguishing structural reconstruction from plausible scene generation.

| Evidence / representation | Reconstruction strategy | Representative studies |
| :--- | :--- | :--- |
| Stereo imagery and DSMs | Recover depth, then fit or assemble structured surfaces | [SAT2LOD2](PAPERS.md#r022), [PLANES4LOD2](PAPERS.md#r070) |
| Single-image inference | Use structural and learned priors to resolve missing depth | [3D Manhattan wireframes](PAPERS.md#r106), [DG-BRF](PAPERS.md#r027), [Sat2City](PAPERS.md#r029) |
| Primitive assembly | Select and regularize candidate planes and faces | [PolyFit](PAPERS.md#r063), [City3D](PAPERS.md#r030), [SimpliCity](PAPERS.md#r006) |
| Learned wireframes and meshes | Predict edges, autoregressive meshes, or implicit fields | [PBWR](PAPERS.md#r032), [Point2Building](PAPERS.md#r052), [Deep implicit fields](PAPERS.md#r014) |
| Generative completion | Recover missing structure using learned shape priors | [EdgeDiff](PAPERS.md#r053), [BuildAnyPoint](PAPERS.md#r028), [ArcPro](PAPERS.md#r031) |
| Image-LiDAR fusion | Combine sharp visual boundaries with metric surface measurements | [Cheng et al., 2011](PAPERS.md#r015), [Cheng et al., 2013](PAPERS.md#r017), [Awrangjeb et al.](PAPERS.md#r004) |

<details>
<summary><strong>Example: from heterogeneous point clouds to a structured mesh</strong></summary>

<p align="center"><img src="assets/buildanypoint.png" alt="BuildAnyPoint pipeline: diffusion-based point recovery followed by Transformer-based mesh generation" width="90%"></p>

*Figure 7 from the survey, presenting BuildAnyPoint (Hua et al., 2026). The method recovers an intermediate point representation before conditional mesh generation.*

</details>

**Takeaway:** Geometric fidelity, structural completeness, and model compactness must be considered together. A visually plausible completion still needs validation against the observations.

[Detailed summary](docs/section-summaries.md#s4) · [3D paper collection](PAPERS.md#models) · [Fusion studies](PAPERS.md#fusion)

## 5. Datasets and Evaluation

Training and evaluation must reflect the intended geometric output. Footprint masks, roof graphs, and building meshes supply different supervision and support different claims about reconstruction quality.

| Task | Representative resources | Evaluation emphasis |
| :--- | :--- | :--- |
| Building footprints | CrowdAI, WHU, Inria, SpaceNet, Deventer-512 | Instance coverage, polygon boundaries, corners, and complexity |
| Roof structure | VWB, Enschede, BuildingWF, Roof3D, Boston / BONAI | Junctions, edge connectivity, roof facets, and height |
| 3D reconstruction and supporting tasks | BuildingWorld, Building3D, Map2ImLas, City-BIS, Structured3D | Surface fit, wireframes, topology, and structural completeness |

The survey discusses region and instance metrics, boundary measures such as PoLiS, angle and complexity measures, edge precision/recall, and 3D geometric errors. Segmentation or semantic datasets can support a reconstruction pipeline without providing a complete reconstruction benchmark.

**Takeaway:** Report geometric quality and topology alongside coverage. Results from different datasets, input conditions, and evaluation protocols should not be treated as a single leaderboard.

[Dataset and metric guide](docs/datasets-and-evaluation.md) · [Detailed summary](docs/section-summaries.md#s5)

## 6. Discussion and Future Outlook

| Research direction | Opportunity | Open question |
| :--- | :--- | :--- |
| Topology and geometric regularity | Recover usable polygons, wireframes, and surfaces | How can valid structure be enforced without erasing real architectural detail? |
| Sparse and occluded observations | Combine measurements with structural completion | Which parts are measured, and which are inferred? |
| Annotation-efficient learning | Use self-supervision and aligned geographic data | How can noisy pseudo-labels and geographic domain shifts be controlled? |
| Foundation and generative models | Transfer semantic knowledge and learned shape priors | How can coordinate accuracy, topology, and uncertainty be validated? |
| Multimodal and semantic modeling | Connect appearance, geometry, and urban meaning | How can alignment and temporal inconsistencies be managed? |
| Scalable, dynamic digital twins | Update city models through time | How can efficiency, provenance, and reliable change tracking be maintained? |

**Takeaway:** The next step is dependable reconstruction at urban scale. New model families are promising, but reliable deployment also requires geometric checks, uncertainty awareness, and reproducible workflows.

[Detailed summary](docs/section-summaries.md#s6) · [Outlook literature](PAPERS.md#outlook)

## 7. Conclusion

Building reconstruction is progressing from masks and isolated primitives toward explicit, connected geometric representations. Optical imagery, LiDAR, and multimodal fusion provide complementary evidence, while learned methods expand the range of structures that can be recovered.

The survey's central conclusion is that automation must be judged by the usability of the resulting geometry. Accurate observations, appropriate structural priors, topology-aware modeling, and scalable processing remain essential for building dependable urban digital twins.

[Detailed summary](docs/section-summaries.md#s7)

---

## Paper Library and Downloads

The [paper library](PAPERS.md) contains **110 bibliography entries**, including the original manuscript bibliography and the maintainer-supplied addition, organized into reading collections with stable reference IDs.

**Download links will be supplied by the repository maintainer after the papers are uploaded.** A `Pending` label means that no download address has been provided yet. Publisher pages and DOI records are not substituted for those download links.

## Publication and Citation
